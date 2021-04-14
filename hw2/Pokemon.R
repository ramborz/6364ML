library(party)
library(rpart)
library(rpart.plot)
library(ISLR)
require(tree)
library(partykit)
myfile2=read.csv("Pokemon.csv", stringsAsFactors = TRUE)

png(file = "decision.png", width = 1920, height = 1080)

output.tree <- ctree(Legendary ~ Speed + Sp..Def + Sp..Atk + Defense + Attack + HP + Type.1 + Type.2, data = myfile2)

plot(as.simpleparty(output.tree))

dev.off()