setwd("~/code/")

# Cargar librerías
library(ggplot2)

# Fijar semilla para reproducibilidad
set.seed(123)

# Definir parámetros de las distribuciones
mu_b1 <- 10
sigma_b1 <- 2

mu_b2 <- 10
sigma_b2 <- 4

mu_b3 <- 7
sigma_b3 <- 2

# Generar muestras aleatorias para cada distribución
n <- 1000  # tamaño de la muestra

b1 <- rnorm(n, mean = mu_b1, sd = sigma_b1)
b2 <- rnorm(n, mean = mu_b2, sd = sigma_b2)
b3 <- rnorm(n, mean = mu_b3, sd = sigma_b3)

# Crear un dataframe con todas las distribuciones
data <- data.frame(
  value = c(b1, b2, b3),
  group = factor(rep(c("b1", "b2", "b3"), each = n))
)

# Generar violin plot
ggplot(data, aes(x = group, y = value, fill = group)) +
    geom_violin(trim = FALSE) +
    geom_point(stat = "summary", fun = "mean", color = "black", size = 2) +
    theme_minimal() +
    labs(
        x = "",
        y = "Premio"
    ) +
    scale_x_discrete(labels = c("b1" = "Bandit 1", "b2" = "Bandit 2", "b3" = "Bandit 3")) +
    theme_linedraw() + 
    theme(
        legend.position = "none",
        axis.title = element_text(size = 20),
        axis.text = element_text(size = 18)
    )

# Guardar la imagen en alta calidad
ggsave("violin_plot.png", dpi = 300, width = 8, height = 10)
