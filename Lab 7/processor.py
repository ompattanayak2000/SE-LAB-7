
import json
import math


def calculate_dimensional_weight(dimensions_str):
    try:
        if not isinstance(dimensions_str, str):
            return 0.0

        dims = dimensions_str.lower().split('x')

        if len(dims) != 3:
            return 0.0

        length, width, height = map(float, dims)

        if not all(math.isfinite(d) and d > 0 for d in (length, width, height)):
            return 0.0

        return round((length * width * height) / 5000.0, 2)

    except (ValueError, TypeError, OverflowError):
        return 0.0


def format_tracking_label(raw_code):
    try:
        if not isinstance(raw_code, str) or len(raw_code) < 2:
            return "INVALID"

        prefix = raw_code[0]

        if not prefix.isalpha() or not raw_code[1:].isdigit():
            return "INVALID"

        tracking_num = int(raw_code[1:])

        return f"{prefix.upper()}-{tracking_num:06d}"

    except (ValueError, TypeError, OverflowError):
        return "INVALID"


def parse_package_manifest(json_payload):
    try:
        if not isinstance(json_payload, str):
            return 0.0

        data = json.loads(json_payload)

        if not isinstance(data, dict) or "weight" not in data:
            return 0.0

        weight = data["weight"]

        if isinstance(weight, bool):
            return 0.0

        weight = float(weight)

        if not math.isfinite(weight) or weight <= 0:
            return 0.0

        return weight

    except (ValueError, TypeError, OverflowError):
        return 0.0


def main():
    print("==== Running calculate_dimensional_weight ====")
    dims_input = input("Enter dimensions LxWxH in cm (e.g. 20x30x10): ")
    dim_weight = calculate_dimensional_weight(dims_input)
    print("Dimensional Weight (kg):", dim_weight)

    print("\n==== Running format_tracking_label ====")
    code_input = input("Enter raw code (e.g. E123): ")
    label = format_tracking_label(code_input)
    print("Formatted Label:", label)

    print("\n==== Running parse_package_manifest ====")
    json_input = input('Enter manifest JSON (e.g. {"weight": 12.5}): ')
    weight = parse_package_manifest(json_input)
    print("Manifest Weight:", weight)


if __name__ == "__main__":
    main()
