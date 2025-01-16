library(tidyverse)

data <- read.csv("monitor.csv")

air_temperature_cols <- data %>%
    select(month, day_of_month, hour, starts_with("air_temperature_"))

data_long <- air_temperature_cols %>%
    pivot_longer(cols = -c(month, day_of_month, hour), names_to = "Variable", values_to = "Valor")

data_long <- data_long %>% filter(month %in% c(10, 11, 12, 1, 2, 3))

data_long <- data_long %>%
    mutate(
        Year = ifelse(month >= 9, 2023, 2024),
        Date = as.POSIXct(paste(Year, month, day_of_month, hour, sep = "-"), format = "%Y-%m-%d-%H")
    )

p <- ggplot(data_long, aes(x = Date, y = Valor, color = Variable)) +
    geom_line(alpha=0.5) +
    geom_hline(yintercept = 19, linetype = "dashed", color = "blue") +
    geom_hline(yintercept = 21, linetype = "dashed", color = "red") +
    labs(
        title = "Temperatures",
        x = "Time",
        y = "Temperature (ºC)"
    ) +
    theme_linedraw()

p <- p + scale_x_datetime(date_breaks = "1 month", date_labels = "%b %Y")
p <- p + scale_y_continuous(breaks = seq(0, 30, by = 1))
p

ggsave("temperatures.png", plot = p, width = 12, height = 4.8, dpi = 400, bg = "white")

######################################################################

# air_temperature_cols <- data %>%
#     select(ends_with("_air_temperature"))

# data_long <- air_temperature_cols %>%
#     select(-starts_with("people_")) %>%
#     pivot_longer(everything(), names_to = "Variable", values_to = "Valor")

# p <- ggplot(data_long, aes(x = Variable, y = Valor)) +
#     geom_violin() +
#     labs(
#         title = "Temperature variation",
#         x = "Variable",
#         y = "Temperature (ºC)"
#     ) +
#     theme_linedraw()

# p <- p + scale_y_continuous(breaks = seq(0, 30, by = 1))
# p

# ggsave("temp_variation.png", plot = p, width = 12, height = 6, dpi = 400, bg = "white")

######################################################################

# energy_cols <- data %>%
#     select(month, day_of_month, hour, starts_with("HVAC_electricity_demand_rate"))

# data_long <- energy_cols %>%
#     pivot_longer(cols = -c(month, day_of_month, hour), names_to = "Variable", values_to = "Valor")

# data_long <- data_long %>%
#     mutate(
#         Year = ifelse(month >= 9, 2023, 2024),
#         Date = as.POSIXct(paste(Year, month, day_of_month, hour, sep = "-"), format = "%Y-%m-%d-%H")
#     )

# p <- ggplot(data_long, aes(x = Date, y = Valor, color = Variable)) +
#     geom_line() +
#     labs(
#         title = "Demand rate",
#         x = "Time",
#         y = "HVAC electricity demand rate (w)"
#     ) +
#     theme_linedraw() +
#     guides(color = "none")

# p <- p + scale_x_datetime(date_breaks = "1 month", date_labels = "%b %Y")
# p

# ggsave("demand.png", plot = p, width = 12, height = 4.8, dpi = 400, bg = "white")
