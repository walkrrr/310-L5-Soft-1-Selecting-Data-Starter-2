import csv
import numpy as np
import matplotlib.pyplot as plt

with open("titanic.csv", "r") as file:
  data = csv.reader(file, delimiter=",")
  headers = next(data)
  data = list(data)
  data = np.array(data)
  

survived = np.array (data[:,[0]], dtype = int).flatten()
fare = np.array(data[:,[7]], dtype = float).flatten()

#empty lists to hold data from  the for loop
fare_survived = []
fare_not_survived = []

#ADD CODE: for lfare_survived.append(fare[index])oop and if/else statements
for index in range(0, len(fare)):
  if survived[index] == 1:
    fare_survived.append(fare[index])
  else:
    fare_not_survived.append(fare[index])

bins = range(0,240,15)
plt.hist(fare_not_survived, bins, histtype="bar", color="#460cbb", alpha=0.5)
plt.hist(fare_survived, bins, histtype="bar", color="#e02067", alpha=0.5)
plt.xticks(range(0,240,20))
plt.yticks(range(0,360,25))
plt.xlabel("Fare")
plt.ylabel("Passengers")
plt.title("Titanic Fares and Survival Rates")
plt.gca().legend(("Did Not Survive","Survived"))

plt.savefig("titanic_fares_and_survival_rates.png")
