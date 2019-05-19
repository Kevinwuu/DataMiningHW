import json
with open('data.json', 'r') as f:
    data = json.load(f)

for i in range(len(data)):
    for value in data[i].values():
        if '中東' in value:
            # print(data[i])
            print(json.dumps(data[i], indent=4, sort_keys=True))



# print(data[0])
