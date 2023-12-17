library(readr)
library(tidyr)
library(ggplot2)
library(ggsci)

d <- read_csv("../data/卸売市場経由率の推移.csv")

d_long <- pivot_longer(d, cols = -年度, names_to = "name", values_to = "value")
d_long$name <- factor(d_long$name, levels = unique(d_long$name))
year_2010 <- d_long |> dplyr::filter(年度 == 2010)

g <- ggplot(data = d_long, aes(x = 年度, y = value, group = name, colour = name)) +
  geom_line() +
  geom_point() +
  geom_text(data = year_2010, aes(x = 年度, y = value, label = name, colour = name), 
            nudge_x = 0.5, nudge_y = 2.5, check_overlap = FALSE) +
  scale_y_continuous(limits = c(0, 100)) +
  labs(title = "卸売市場経由率の推移",
       x = "年度", 
       y = "%",
       caption = "農林水産省(2022)「令和3年度 卸売市場データ集」") +
  theme_bw() +
  theme(
    text = element_text(family = "Hiragino Sans"),
    legend.position = "none"
  ) +
  scale_color_d3()

ggsave("wholesale_market_trends.pdf", plot = g, device = cairo_pdf, path = ".", width = 10, height = 5)
