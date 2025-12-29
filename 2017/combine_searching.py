import json
import os

output_file = 'd:/gatetutor/all Q/2017/all_searching_problems.json'
base_path = 'd:/gatetutor/all Q/2017/'
all_problems = []

for i in range(1, 7):
    file_name = f'2017-search-{i}.json'
    file_path = os.path.join(base_path, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if 'problems' in data and len(data['problems']) > 0:
                all_problems.append(data['problems'][0])

combined_data = {"problems": all_problems}

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, indent=4)

print(f"Successfully combined {len(all_problems)} problems into {output_file}")
