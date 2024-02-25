import json
import pandas as pd

input_filepath = 'testset_answer_finding_impression.jsonl'
output_filepath = 'test_ids.csv'

# for extracting the test set ids
with open(input_filepath, 'r') as input_file, open(output_filepath, 'w') as output_file:
    output_file.write('id\n')
    
    for line in input_file:
        try:
            data = json.loads(line)
            output_file.write(f"{data['question_id']}\n")
        except json.JSONDecodeError:
            print("Error decoding JSON")
        except KeyError:
            print("Key 'id' not found in JSON object")


# for getting the original reports for the test set data
df = pd.read_csv('test_ids.csv')
json_filepath = 'patient_finding_impression.json'

with open(json_filepath, 'r') as f:
    data = json.load(f)
    
original_reports = []
for patient in data:
    if patient['id'] in df['id']:
        for convo in patient['conversations']:
            if convo['from'] == 'gpt':
                original_reports.append({'id': patient['id'], 'report': convo['value']})

report_df = pd.DataFrame(original_reports)

report_df.to_csv('testset.csv', index=False)