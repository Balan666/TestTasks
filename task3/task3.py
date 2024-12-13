import json
import sys
import re

def convert_to_json(input_file):
    try:
        with open(input_file, 'r') as f:
            content = f.read()

        # Attempt to parse the content as JSON
        data = json.loads(content)

        # Save the parsed content back to a JSON file
        output_file = input_file.rsplit('.', 1)[0] + ".json"
        with open(output_file, 'w') as out_f:
            json.dump(data, out_f, indent=4)

        print(f"File converted and saved as {output_file}")
        return data
    except json.JSONDecodeError as e:
        print("Failed to parse JSON. Please check the input file format.")
        print(f"Error details: {e}")
        sys.exit(1)

def fill_values(tests, values_map):
    for test in tests:
        if "id" in test and test["id"] in values_map:
            test["value"] = values_map[test["id"]]
        if "values" in test:
            fill_values(test["values"], values_map)


def validate_values(values):
    if not isinstance(values, list):
        raise ValueError("Values file should contain a list of objects.")
    for item in values:
        if not isinstance(item, dict) or "id" not in item or "value" not in item:
            raise ValueError("Each item in values must be a dictionary with 'id' and 'value' keys.")


def main(tests_file, values_file, report_file):
    try:
        if not re.search(r"\.json$", tests_file):
            print(f"Converting {tests_file} to json...")
            tests = convert_to_json(tests_file)
        else:
            with open(tests_file, 'r') as f:
                tests = json.load(f)

        if not re.search(r"\.json$", values_file):
            print(f"Converting {values_file} to json...")
            values_data = convert_to_json(values_file)
        else:
            with open(values_file, 'r') as f:
                values_data = json.load(f)

        if "values" not in values_data:
            raise ValueError("Values file must contain a 'values' key with a list of objects.")
        values = values_data["values"]

        # Validate the values structure
        validate_values(values)

        # Create a map of id to value
        values_map = {value["id"]: value["value"] for value in values}

        # Fill the 'value' fields in the tests structure
        fill_values(tests["tests"], values_map)

        # Write the updated tests structure to the report file
        with open(report_file, 'w') as f:
            json.dump(tests, f, indent=4)

        print(f"Report successfully written to {report_file}")
    except Exception as e:
        print(f"Error processing files: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 task3.py <tests_file> <values_file> <report_file>")
        sys.exit(1)

    tests_file = sys.argv[1]
    values_file = sys.argv[2]
    report_file = sys.argv[3]

    main(tests_file, values_file, report_file)
