import json
import math

def sigmoid(value):
    output = 1/(1 + math.exp(-value))
    return(output)

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

hour = float(input("Hours:-"))
attendance = float(input("Attendance:-"))

# calculating output
n1 = sigmoid((hour * n1w1) + (attendance * n1w2) + n1b)
n2 = sigmoid((hour * n2w1) + (attendance * n2w2) + n2b)
output = sigmoid((n1 * nw1) + (n2 * nw2) + nb)

print(output)
if output <= 0.5:
        print("Fail")
elif output > 0.5:
    print("pass")
else:
    print("Something is Wrong")