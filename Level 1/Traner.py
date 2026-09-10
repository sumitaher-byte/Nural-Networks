import json

hour_dataset = [
    0.5, 0.8, 1.0, 1.2, 1.4,
    1.6, 1.8, 2.0, 2.2, 2.4,
    2.5, 2.6, 2.7, 2.8, 2.9,
    3.0, 3.1, 3.2, 3.3, 3.4,
    3.5, 3.6, 3.7, 3.8, 3.9,
    4.0, 4.1, 4.2, 4.3, 4.4,
    4.5, 4.6, 4.7, 4.8, 4.9,
    5.0, 5.1, 5.2, 5.3, 5.4,
    5.5, 5.6, 5.8, 6.0, 6.5,
    7.0, 7.5, 8.0, 9.0, 10.0
]
result_dataset = [
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1
]

with open(r"D:\Work\Projects\Nural Networks\Level 1\dic.json", "r") as file:
    data = json.load(file)

weight = data["weight"]
bias = data["bias"]
lerning_rate = 0.01

for i in range(100000):
    for x, y in zip(hour_dataset, result_dataset):

        result = x * weight + bias
        error = y - result
        weight = weight + lerning_rate * error * x
        bias = bias + lerning_rate * error

with open(r"D:\Work\Projects\Nural Networks\Level 1\dic.json", "w") as file:
    json.dump({"weight": weight, "bias": bias}, file, indent=4)