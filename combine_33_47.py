#!/usr/bin/env python3
"""Combine Bit Manipulation problems 33-47 into a single JSON file"""
import json
import os

# Get the absolute path
base_dir = r"d:\gatetutor\all Q"
folder_path = os.path.join(base_dir, "Data Structure", "20255", "Bit Manipulation")
all_problems = []

# Read problems 33 to 47
for i in range(33, 48):
    file_path = os.path.join(folder_path, f"{i}.json")
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "problems" in data and len(data["problems"]) > 0:
                    all_problems.append(data["problems"][0])
                    title = data['problems'][0].get('title', 'Unknown')
                    print(f"Added problem {i}: {title}")
        except Exception as e:
            print(f"Error reading {i}.json: {e}")
    else:
        print(f"Warning: File {file_path} not found")

# Create combined JSON
combined_data = {
    "problems": all_problems
}

# Write to file
output_file = os.path.join(folder_path, "33-47_combined.json")
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, indent=4, ensure_ascii=False)

print(f"\nCombined {len(all_problems)} problems into {output_file}")

