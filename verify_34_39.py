#!/usr/bin/env python3
"""Verify JSON files 34-39 are valid"""
import json
import os
import sys

# Set UTF-8 encoding for output
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

folder_path = os.path.join("Data Structure", "20255", "Bit Manipulation")

for i in range(34, 40):
    file_path = os.path.join(folder_path, f"{i}.json")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if "problems" in data and len(data["problems"]) > 0:
                title = data["problems"][0].get("title", "Unknown")
                print(f"OK {i}.json: {title}")
            else:
                print(f"ERROR {i}.json: Invalid structure")
    except Exception as e:
        print(f"ERROR {i}.json: {e}")

print("\nAll files verified!")

