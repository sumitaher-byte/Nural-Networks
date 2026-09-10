import json

with open(r"D:\Work\Projects\Nural Networks\Level 2\data_set.json", "r") as data_set:
    data = json.load(data_set)

hours = data["hours_dataset"]
practices = data["practice_dataset"]
results = data["result_dataset"]

with open(r"D:\Work\Projects\Nural Networks\Level 2\weight.json", "r") as file:
    weight_data = json.load(file)
weight_1 = weight_data["weight_1"]
weight_2 = weight_data["weight_2"]
bias = weight_data["bias"]
lerning_rate = 0.001



for times in range(100000):
    for hour, practice, result in zip(hours, practices, results):
        output = (hour * weight_1) + (practice * weight_2) + bias
        error = result - output
        weight_1 = weight_1 + error * lerning_rate * hour
        weight_2 = weight_2 + error * lerning_rate * practice
        bias = bias + lerning_rate * error

with open(r"D:\Work\Projects\Nural Networks\Level 2\weight.json", "w") as file:
    json.dump({"weight_1" : weight_1, "weight_2" : weight_2, "bias" : bias}, file, indent=4)