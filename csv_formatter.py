import json
import csv

def convert_json_to_csv(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        data = json.load(input_file)

    with open(output_file_path, 'w', newline='') as output_file:
        csvwriter = csv.writer(output_file)
        csvwriter.writerow(['title', 'url'])

        for item in data:
            csvwriter.writerow([item["_str.title"], item["_str.url"]])

input_file_path = 'output.json'
output_file_path = 'csv_output.csv'

convert_json_to_csv(input_file_path, output_file_path)
