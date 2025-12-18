from datetime import datetime
from pathlib import Path
from typing import Dict, cast

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Global plotting style for publication-quality figures
plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update(
    {
        "figure.dpi": 120,
        "savefig.dpi": 400,  # high resolution for papers
        "font.size": 10,
        "axes.labelsize": 11,
        "axes.titlesize": 11,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.fontsize": 9,
        "lines.linewidth": 1.0,
    }
)

ROOT = Path(__file__).resolve().parents[1]


CASE_CONFIG = {
    1: {
        "name": "Case 1",
        "agent": "PPO",
        "dir": "Eval-DRL-Baseline-2026-case-1_2025-12-16_12:59-res1",
    },
    2: {
        "name": "Case 2",
        "agent": "TQC",
        "dir": "Eval-DRL-Baseline-2026-case-2_2025-12-16_13:05-res1",
    },
    3: {
        "name": "Case 3",
        "agent": "TQC",
        "dir": "Eval-DRL-Baseline-2026-case-3_2025-12-16_13:08-res1",
    },
}


def load_progress_metrics(case_cfg: Dict) -> pd.DataFrame:
    """Load raw evaluation metrics from progress.csv for a given case."""
    progress_path = ROOT / case_cfg["dir"] / "progress.csv"
    df = pd.read_csv(progress_path)
    return df


def plot_progress_comparison(output_dir: Path) -> None:
    """Create one boxplot per metric to compare cases."""
    output_dir.mkdir(parents=True, exist_ok=True)

    case_labels = [f'{cfg["name"]} ({cfg["agent"]})' for cfg in CASE_CONFIG.values()]

    # Load dataframes per case
    dfs = {case_id: load_progress_metrics(cfg) for case_id, cfg in CASE_CONFIG.items()}

    # (column_name, label, filename, y_label)
    metrics_spec = [
        ("mean_reward", "Episode mean reward", "box_mean_reward.png", "Reward"),
        (
            "mean_temperature_violation",
            "Episode mean temperature violation",
            "box_mean_temperature_violation.png",
            "Temperature violation (°C)",
        ),
        (
            "mean_power_demand",
            "Episode mean power demand",
            "box_mean_power_demand.png",
            "Power demand (kW)",
        ),
        (
            "mean_compressor_starts_per_day",
            "Episode mean compressor starts per day",
            "box_mean_compressor_starts_per_day.png",
            "Starts per day",
        ),
    ]

    for col, title, filename, y_label in metrics_spec:
        data = [dfs[c][col].to_numpy() for c in CASE_CONFIG.keys()]

        fig, ax = plt.subplots(figsize=(6, 4))
        bp = ax.boxplot(
            data,
            patch_artist=True,
            medianprops={"color": "black", "linewidth": 1.5},
        )

        # Minimalist coloring
        colors = ["#4c72b0", "#55a868", "#c44e52"]
        for patch, color in zip(bp["boxes"], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.4)

        ax.set_xticks(np.arange(1, len(case_labels) + 1))
        ax.set_xticklabels(case_labels, rotation=15, ha="right")

        ax.set_title(title)
        ax.set_ylabel(y_label)
        ax.grid(axis="y", alpha=0.2)

        fig.tight_layout()
        fig.savefig(output_dir / filename, dpi=200)
        plt.close(fig)


def plot_flow_and_water_violin(output_dir: Path) -> None:
    """Create violin plots for flow rates (per room and per case) and water temperature."""
    output_dir.mkdir(parents=True, exist_ok=True)

    case_labels = [f'{cfg["name"]} ({cfg["agent"]})' for cfg in CASE_CONFIG.values()]
    colors = ["#4c72b0", "#55a868", "#c44e52"]

    flow_cols = [
        "flow_rate_living",
        "flow_rate_kitchen",
        "flow_rate_bed1",
        "flow_rate_bed2",
        "flow_rate_bed3",
    ]

    flow_data: list[np.ndarray] = []
    water_data: list[np.ndarray] = []

    # Map case index to label to keep ordering consistent
    case_items = list(CASE_CONFIG.items())

    for _, cfg in case_items:
        monitor_dir = ROOT / cfg["dir"] / "episode-20" / "monitor"
        obs_path = monitor_dir / "observations.csv"
        infos_path = monitor_dir / "infos.csv"

        obs = pd.read_csv(obs_path)
        infos = pd.read_csv(infos_path)

        # Align and restrict to Oct–Apr window using same logic as temperatures
        min_len = min(len(obs), len(infos))
        obs = obs.iloc[:min_len].reset_index(drop=True)
        infos = infos.iloc[:min_len].reset_index(drop=True)

        dt_index = build_datetime_index(infos)
        obs.index = dt_index

        start = datetime(2026, 11, 15)
        end = datetime(2027, 3, 15)
        mask = (obs.index >= start) & (obs.index <= end)
        obs = obs.loc[mask]

        # Aggregate flow over all rooms into a single distribution per case
        flow_vals = obs[flow_cols].to_numpy().ravel().astype(float)
        flow_data.append(flow_vals)

        # Water temperature distribution per case
        water_vals = obs["water_temperature"].to_numpy().astype(float)
        water_data.append(water_vals)

    # Water temperature violins (global comparison across cases)
    fig, ax_water = plt.subplots(figsize=(6, 3))
    vp_water = ax_water.violinplot(
        [arr for arr in water_data], showmeans=True, showextrema=False
    )
    for body, color in zip(vp_water["bodies"], colors):
        body.set_facecolor(color)
        body.set_alpha(0.4)
    ax_water.set_xticks(np.arange(1, len(case_labels) + 1))
    ax_water.set_xticklabels(case_labels, rotation=15, ha="right")
    ax_water.set_ylabel("Water temperature (°C)")
    ax_water.set_title("Water temperature distribution")
    ax_water.grid(axis="y", alpha=0.2)

    fig.tight_layout()
    fig.savefig(output_dir / "violin_water_temperature.png", dpi=200)
    plt.close(fig)

    # Flow-rate violins per room and per case (one figure per case)
    room_labels = ["Living room", "Kitchen", "Bedroom 1", "Bedroom 2", "Bedroom 3"]

    for idx, (_, cfg) in enumerate(case_items):
        # Re-load and filter observations for this specific case
        monitor_dir = ROOT / cfg["dir"] / "episode-20" / "monitor"
        obs_path = monitor_dir / "observations.csv"
        infos_path = monitor_dir / "infos.csv"

        obs = pd.read_csv(obs_path)
        infos = pd.read_csv(infos_path)

        min_len = min(len(obs), len(infos))
        obs = obs.iloc[:min_len].reset_index(drop=True)
        infos = infos.iloc[:min_len].reset_index(drop=True)

        dt_index = build_datetime_index(infos)
        obs.index = dt_index

        start = datetime(2026, 11, 15)
        end = datetime(2027, 3, 15)
        mask = (obs.index >= start) & (obs.index <= end)
        obs = obs.loc[mask]

        room_flows = [obs[col].to_numpy().astype(float) for col in flow_cols]

        fig_f, ax_f = plt.subplots(figsize=(6, 3))
        vp_f = ax_f.violinplot(
            [arr for arr in room_flows],
            showmeans=True,
            showextrema=False,
        )
        for body in vp_f["bodies"]:
            body.set_facecolor(colors[idx])
            body.set_alpha(0.4)

        ax_f.set_xticks(np.arange(1, len(room_labels) + 1))
        ax_f.set_xticklabels(room_labels, rotation=15, ha="right")
        ax_f.set_ylabel("Flow rate")
        ax_f.set_title(f'{cfg["name"]} – Flow rate per room')
        ax_f.grid(axis="y", alpha=0.2)

        fig_f.tight_layout()
        fig_f.savefig(
            output_dir / f'violin_flow_case{idx + 1}.png',
            dpi=200,
        )
        plt.close(fig_f)


def build_datetime_index(
    infos: pd.DataFrame, base_year: int = 2026
) -> pd.DatetimeIndex:
    """Build a continuous datetime index from October to April.

    Months 10, 11 and 12 belong to the base year, and months 1–4 to base_year + 1.
    """
    months = infos["month"].astype(int).to_numpy()
    days = infos["day"].astype(int).to_numpy()
    hours = infos["hour"].astype(int).to_numpy()

    years = np.where(months >= 10, base_year, base_year + 1)

    datetimes = pd.to_datetime(
        {
            "year": years,
            "month": months,
            "day": days,
            "hour": hours,
        }
    )
    # pd.to_datetime devuelve un DatetimeIndex cuando se le pasa un dict de arrays
    # pero lo anotamos explícitamente para contentar al analizador estático.
    return pd.DatetimeIndex(datetimes)


TEMP_COLS = [
    "air_temperature_living",
    "air_temperature_kitchen",
    "air_temperature_bed1",
    "air_temperature_bed2",
    "air_temperature_bed3",
]

SETPOINT_COLS = [
    "heating_setpoint_living",
    "heating_setpoint_kitchen",
    "heating_setpoint_bed1",
    "heating_setpoint_bed2",
    "heating_setpoint_bed3",
]


def plot_case_temperatures(
    case_id: int, case_cfg: Dict, output_dir: Path, daily_date: pd.Timestamp
) -> None:
    """Plot indoor air temperatures and setpoints (Oct–Apr) for a given case."""
    monitor_dir = ROOT / case_cfg["dir"] / "episode-20" / "monitor"
    obs_path = monitor_dir / "observations.csv"
    infos_path = monitor_dir / "infos.csv"

    obs = pd.read_csv(obs_path)
    infos = pd.read_csv(infos_path)

    # Alineamos por índice por si hubiera pequeñas diferencias de longitud
    min_len = min(len(obs), len(infos))
    obs = obs.iloc[:min_len].reset_index(drop=True)
    infos = infos.iloc[:min_len].reset_index(drop=True)

    dt_index = build_datetime_index(infos)
    obs.index = dt_index

    # Temporal crop
    start = datetime(2026, 11, 15)
    end = datetime(2027, 3, 15)
    mask = (obs.index >= start) & (obs.index <= end)
    obs = obs.loc[mask]

    # Masks for the selected daily, weekly and monthly windows
    daily_date_norm = daily_date.normalize()
    daily_mask = obs.index.normalize() == daily_date_norm
    obs_daily = obs.loc[daily_mask]

    week_start = daily_date_norm
    week_end = week_start + pd.Timedelta(days=6)
    week_mask = (obs.index >= week_start) & (obs.index <= week_end)
    obs_week = obs.loc[week_mask]

    month_start = daily_date_norm.replace(day=1)
    month_end = month_start + pd.offsets.MonthEnd(0)
    month_mask = (obs.index >= month_start) & (obs.index <= month_end)
    obs_month = obs.loc[month_mask]

    n_rooms = len(TEMP_COLS)
    ncols = 2
    nrows = int(np.ceil(n_rooms / ncols))

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(12, 6), sharex=True)
    axes = np.array(axes).reshape(-1)

    for i, (temp_col, sp_col) in enumerate(zip(TEMP_COLS, SETPOINT_COLS)):
        ax = axes[i]

        # Indoor temperature
        ax.plot(obs.index, obs[temp_col], label="Indoor temperature", linewidth=0.8)

        # Setpoint as ±1 °C band
        sp = obs[sp_col]
        ax.fill_between(
            obs.index,
            sp - 1.0,
            sp + 1.0,
            color="tab:orange",
            alpha=0.2,
            label="Setpoint ±1 °C band",
        )
        base_name = temp_col.replace("air_temperature_", "")
        if base_name == "living":
            room_name = "Living room"
        elif base_name == "kitchen":
            room_name = "Kitchen"
        elif base_name.startswith("bed"):
            idx = base_name.replace("bed", "")
            room_name = f"Bedroom {idx}"
        else:
            room_name = base_name.capitalize()

        ax.set_title(room_name)
        # Only label Y-axis once (first column)
        if i % ncols == 0:
            ax.set_ylabel("Temperature (°C)")
        ax.grid(alpha=0.3)

        if i == 0:
            # Place legend below the axes to avoid overlapping with title and data
            ax.legend(
                fontsize=8,
                loc="upper center",
                bbox_to_anchor=(0.5, -0.25),
                ncol=2,
                frameon=False,
            )

    # Eliminar ejes vacíos si los hubiera
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    fig.suptitle(f'{case_cfg["name"]} – {case_cfg["agent"]}')
    fig.autofmt_xdate(rotation=15)

    output_dir.mkdir(parents=True, exist_ok=True)
    fig.tight_layout(rect=(0.0, 0.05, 1.0, 0.95))
    fig.savefig(
        output_dir / f'case{case_id}_temperatures.png',
        dpi=200,
        bbox_inches="tight",
    )
    plt.close(fig)

    # Save individual room plots in subfolders (e.g. case1/living_room)
    for i, temp_col in enumerate(TEMP_COLS):
        base_name = temp_col.replace("air_temperature_", "")
        if base_name == "living":
            room_slug = "living_room"
            room_title = "Living room"
        elif base_name == "kitchen":
            room_slug = "kitchen"
            room_title = "Kitchen"
        elif base_name.startswith("bed"):
            idx = base_name.replace("bed", "")
            room_slug = f"bedroom_{idx}"
            room_title = f"Bedroom {idx}"
        else:
            room_slug = base_name
            room_title = base_name.capitalize()

        fig_r, ax_r = plt.subplots(figsize=(10, 3))
        # Indoor temperature
        ax_r.plot(obs.index, obs[temp_col], label="Indoor temperature", linewidth=0.8)
        # Setpoint band
        sp = obs[SETPOINT_COLS[i]]
        ax_r.fill_between(
            obs.index,
            sp - 1.0,
            sp + 1.0,
            color="tab:orange",
            alpha=0.2,
            label="Setpoint ±1 °C band",
        )
        ax_r.set_title(f'{case_cfg["name"]} – {room_title}')
        ax_r.set_ylabel("Temperature (°C)")
        ax_r.grid(alpha=0.3)
        ax_r.legend(
            fontsize=8,
            loc="upper center",
            bbox_to_anchor=(0.5, -0.25),
            ncol=2,
            frameon=False,
        )
        fig_r.autofmt_xdate(rotation=15)

        room_dir = output_dir / f"case{case_id}" / room_slug
        room_dir.mkdir(parents=True, exist_ok=True)
        fig_r.tight_layout(rect=(0.0, 0.05, 1.0, 0.95))
        fig_r.savefig(room_dir / "temperature.png", dpi=200, bbox_inches="tight")
        plt.close(fig_r)

        # Daily zoom plot for the same random day across all rooms and cases
        if not obs_daily.empty:
            fig_d, ax_d = plt.subplots(figsize=(10, 3))
            ax_d.plot(
                obs_daily.index,
                obs_daily[temp_col],
                label="Indoor temperature",
                linewidth=0.8,
            )
            sp_d = obs_daily[SETPOINT_COLS[i]]
            ax_d.fill_between(
                obs_daily.index,
                sp_d - 1.0,
                sp_d + 1.0,
                color="tab:orange",
                alpha=0.2,
                label="Setpoint ±1 °C band",
            )
            ax_d.set_title(
                f'{case_cfg["name"]} – {room_title} (daily sample: {daily_date.date()})'
            )
            ax_d.set_ylabel("Temperature (°C)")
            ax_d.grid(alpha=0.3)
            ax_d.legend(
                fontsize=8,
                loc="upper center",
                bbox_to_anchor=(0.5, -0.25),
                ncol=2,
                frameon=False,
            )
            fig_d.autofmt_xdate(rotation=15)

            fig_d.tight_layout(rect=(0.0, 0.05, 1.0, 0.95))
            fig_d.savefig(
                room_dir / "daily_temperature.png", dpi=200, bbox_inches="tight"
            )
            plt.close(fig_d)

        # Weekly zoom plot
        if not obs_week.empty:
            fig_w, ax_w = plt.subplots(figsize=(10, 3))
            ax_w.plot(
                obs_week.index,
                obs_week[temp_col],
                label="Indoor temperature",
                linewidth=0.8,
            )
            sp_w = obs_week[SETPOINT_COLS[i]]
            ax_w.fill_between(
                obs_week.index,
                sp_w - 1.0,
                sp_w + 1.0,
                color="tab:orange",
                alpha=0.2,
                label="Setpoint ±1 °C band",
            )
            ax_w.set_title(
                f'{case_cfg["name"]} – {room_title} '
                f'(weekly sample: {week_start.date()} to {week_end.date()})'
            )
            ax_w.set_ylabel("Temperature (°C)")
            ax_w.grid(alpha=0.3)
            ax_w.legend(
                fontsize=8,
                loc="upper center",
                bbox_to_anchor=(0.5, -0.25),
                ncol=2,
                frameon=False,
            )
            fig_w.autofmt_xdate(rotation=15)

            fig_w.tight_layout(rect=(0.0, 0.05, 1.0, 0.95))
            fig_w.savefig(
                room_dir / "weekly_temperature.png", dpi=200, bbox_inches="tight"
            )
            plt.close(fig_w)

        # Monthly zoom plot
        if not obs_month.empty:
            fig_m, ax_m = plt.subplots(figsize=(10, 3))
            ax_m.plot(
                obs_month.index,
                obs_month[temp_col],
                label="Indoor temperature",
                linewidth=0.8,
            )
            sp_m = obs_month[SETPOINT_COLS[i]]
            ax_m.fill_between(
                obs_month.index,
                sp_m - 1.0,
                sp_m + 1.0,
                color="tab:orange",
                alpha=0.2,
                label="Setpoint ±1 °C band",
            )
            ax_m.set_title(
                f'{case_cfg["name"]} – {room_title} '
                f'(monthly sample: {month_start.date()} to {month_end.date()})'
            )
            ax_m.set_ylabel("Temperature (°C)")
            ax_m.grid(alpha=0.3)
            ax_m.legend(
                fontsize=8,
                loc="upper center",
                bbox_to_anchor=(0.5, -0.25),
                ncol=2,
                frameon=False,
            )
            fig_m.autofmt_xdate(rotation=15)

            fig_m.tight_layout(rect=(0.0, 0.05, 1.0, 0.95))
            fig_m.savefig(
                room_dir / "monthly_temperature.png", dpi=200, bbox_inches="tight"
            )
            plt.close(fig_m)


def main() -> None:
    """Main entry point."""
    output_dir = ROOT / "eval_plots"

    # 1) Comparativa de métricas de evaluación entre agentes
    plot_progress_comparison(output_dir)

    # 1b) Violin plots for flow rate and water temperature per case
    plot_flow_and_water_violin(output_dir)

    # 2) Series temporales de temperaturas y setpoints por estancia para cada Case
    #    y gráficos diarios para un mismo día aleatorio en todas las salas y casos
    #    (semilla fija para reproducibilidad).
    first_case = next(iter(CASE_CONFIG.values()))
    first_infos_path = ROOT / first_case["dir"] / "episode-20" / "monitor" / "infos.csv"
    first_infos = pd.read_csv(first_infos_path)
    first_dt_index = build_datetime_index(first_infos)
    first_mask = (first_dt_index >= datetime(2026, 10, 15)) & (
        first_dt_index <= datetime(2027, 4, 15, 23)
    )
    valid_dates = pd.to_datetime(first_dt_index[first_mask]).normalize().unique()
    if len(valid_dates) == 0:
        raise RuntimeError("No valid dates found in the selected Oct–Apr window.")

    rng = np.random.default_rng(seed=0)
    # rng.choice sobre un array de Timestamps no debería producir NaT si valid_dates
    # no lo contiene, pero anotamos explícitamente el tipo para el analizador.
    # rng.choice sobre valid_dates (sin NaT) garantiza un Timestamp válido,
    # pero para el analizador estático evitamos el tipo union usando un índice entero.
    idx = int(rng.integers(low=0, high=len(valid_dates)))
    daily_raw = valid_dates[idx]
    # Convertimos explícitamente a datetime.date para evitar tipos unión con NaT
    if isinstance(daily_raw, pd.Timestamp):
        daily_core = daily_raw.to_pydatetime().date()
    else:
        daily_core = pd.to_datetime(daily_raw).date()
    daily_date = pd.Timestamp(daily_core)

    for case_id, cfg in CASE_CONFIG.items():
        plot_case_temperatures(
            case_id,
            cfg,
            output_dir,
            cast(pd.Timestamp, daily_date),
        )

    print(f"Gráficas guardadas en: {output_dir}")


if __name__ == "__main__":
    main()
