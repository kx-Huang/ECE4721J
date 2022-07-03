# load the package ggplot
require(ggplot2)

# read the CSV file into RStudio
df <- read.csv("/data/variation.csv")

# Plot the temperature variation for each continent
ggplot(data = df, aes(x = factor(month), y = temperature / 10, color = continent)) +
    geom_line(aes(group = continent)) +
    geom_point() +
    xlab("Month") +
    ylab("Average Temperature (°C)")

# Plot the the average temperature for each continent
ggplot(df, aes(continent, temperature / 10, fill = continent)) +
    geom_bar(position = "dodge", stat = "summary", fun = "mean") +
    xlab("Continent") +
    ylab("Average Temperature (°C)")
