
# analyzer.py

from reference_ranges import (
    REFERENCE_RANGES,
    get_reference_range
)


def analyze_result(test_name, value, gender):

    minimum, maximum = get_reference_range(
        test_name, gender
    )

    if value < minimum:
        status = "LOW"

    elif value > maximum:
        status = "HIGH"

    else:
        status = "NORMAL"

    result = {
        "test": test_name,
        "value": value,
        "unit": REFERENCE_RANGES[test_name]["unit"],
        "minimum": minimum,
        "maximum": maximum,
        "status": status
    }

    return result
