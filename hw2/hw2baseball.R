library(plyr)
library(ggplot2)

myfile=read.csv("baseball-9192.csv", header = TRUE, stringsAsFactors = FALSE)

ggplot(myfile,  aes(x=Salary, y=BattingAvg)) + 
  geom_point() +
  geom_smooth()
ggplot(myfile,  aes(x=Salary, y=OnBasePct)) + 
  geom_point() +
  geom_smooth()
ggplot(myfile,  aes(x=Salary, y=Runs)) + 
  geom_point() +
  geom_smooth()
ggplot(myfile,  aes(x=Salary, y=Hits)) + 
  geom_point() +
  geom_smooth()
ggplot(myfile,  aes(x=Salary, y=Doubles)) + 
  geom_point() +
  geom_smooth()
ggplot(myfile,  aes(x=Salary, y=Triples)) + 
  geom_point() +
  geom_smooth()
ggplot(myfile,  aes(x=Salary, y=HomeRuns)) + 
  geom_point() +
  geom_smooth(method = 'loess')
ggplot(myfile,  aes(x=Salary, y=RBI)) + 
  geom_point() +
  geom_smooth()
ggplot(myfile,  aes(x=Salary, y=Walks)) + 
  geom_point() +
  geom_smooth()
ggplot(myfile,  aes(x=Salary, y=Strikeouts)) + 
  geom_point() +
  geom_smooth()
ggplot(myfile,  aes(x=Salary, y=StolenBases)) + 
  geom_point() +
  geom_smooth()

fit <- lm(Salary ~ BattingAvg + OnBasePct + Runs + Hits + Doubles + Triples
          + HomeRuns + RBI + Walks + Strikeouts + StolenBases, data=myfile)
summary(fit)
