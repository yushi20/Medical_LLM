import json
import random

with open('patient_data.json') as file:
	data = json.load(file)

random.shuffle(data)

num_train = int(0.8 * len(data))
num_val = int(0.1 * len(data))

train = data[:num_train]
val = data[num_train:num_train+num_val]
test = data[num_train+num_val:]

with open('train_80', 'w') as file:
	json.dump(train, file, indent=4)
with open('val_10', 'w') as file:
	json.dump(val, file, indent=4)
with open('test_10', 'w') as file:
	json.dump(test, file, indent=4)
