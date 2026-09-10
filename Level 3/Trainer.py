#imports
import json 
import math

#function for sigmoid
def sigmoid(value):
    output = 1/(1 + math.exp(-value))
    return(output)

#load training data
with open(r"D:\Work\Projects\Nural Networks\Level 3\data_set.json" , "r") as file:
    data = json.load(file)

#load values data
with open(r"D:\Work\Projects\Nural Networks\Level 3\Values.json" , "r") as file:
    values = json.load(file)


# store weights and biases
n1w1 = values["n1w1"]
n1w2 = values["n1w2"]
n1b = values["n1b"]

n2w1 = values["n2w1"]
n2w2 = values["n2w2"]
n2b = values["n2b"]

nw1 = values["nw1"]
nw2 = values["nw2"]
nb = values["nb"]

lr = 0.001

# no. of epochs
for i in range(5000000):
    for hour, attendance, result in zip(
        data["hours_dataset"],
        data["attendance_dataset"],
        data["result_dataset"]
    ):
        # normalize input values
        hour = hour / 10
        attendance = attendance / 100

        # calculating output
        n1 = sigmoid((hour * n1w1) + (attendance * n1w2) + n1b)
        n2 = sigmoid((hour * n2w1) + (attendance * n2w2) + n2b)
        output = sigmoid((n1 * nw1) + (n2 * nw2) + nb)

        error = result - output

        #error in hidden nuron

        error1 = error * nw1 * n1 *(1-n1)
        error2 = error * nw2 * n2 *(1-n2)

        # changing weights
        nw1 = nw1 + lr * error * n1
        nw2 = nw2 + lr * error * n2
        nb = nb + lr * error

        #changing hidden layers weight
        n1w1 = n1w1 + error1 * lr * hour
        n1w2 = n1w2 + error1 * lr * attendance
        n1b = n1b + lr * error1

        n2w1 = n2w1 + error2 * lr * hour
        n2w2 = n2w2 + error2 * lr * attendance
        n2b = n2b + lr * error2
        
with open(r"D:\Work\Projects\Nural Networks\Level 3\Values.json" , "w") as file:
    json.dump({
    "n1w1" : n1w1,
    "n1w2" : n1w2,
    "n1b" : n1b,
    "n2w1" : n2w1,
    "n2w2" : n2w2,
    "n2b" : n2b,
    "nw1" : nw1,
    "nw2" : nw2,
    "nb" : nb
    },
    file,
    indent=4
    )

