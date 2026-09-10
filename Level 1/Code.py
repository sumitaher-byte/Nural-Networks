import json

with open(r"D:\Work\Projects\Nural Networks\Level 1\dic.json", "r") as file:
    data = json.load(file)


weight = data["weight"]
bias = data["bias"]

while True:
    hour = float(input("Entre Hour you Studied:-"))

    result = hour * weight + bias

    if result <= 0.5:
        print("Fail")
    elif result > 0.5:
        print("pass")
    else:
        print("Something is Wrong")