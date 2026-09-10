import json

with open(r"D:\Work\Projects\Nural Networks\Level 2\weight.json", "r") as file:
    weight_data = json.load(file)
weight_1 = weight_data["weight_1"]
weight_2 = weight_data["weight_2"]
bias = weight_data["bias"]



while True:
    hour = float(input("Hours:-"))
    practice = float(input("Practice:-"))
    output = (hour * weight_1) + (practice * weight_2) + bias
    print(output)
    if output <= 0.5:
            print("Fail")
    elif output > 0.5:
        print("pass")
    else:
        print("Something is Wrong")