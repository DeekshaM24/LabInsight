
# reference_ranges.py

REFERENCE_RANGES = {
    "Hemoglobin": {
        "unit": "g/dL",
        "gender_ranges": {
            "male": (13.0, 17.0),
            "female": (12.0, 16.0)
        }
    },

    "Glucose": {
        "unit": "mg/dL",
        "min": 70,
        "max": 100,
        "gender_ranges": None
    },

    "Total Cholesterol": {
        "unit": "mg/dL",
        "min": 0,
        "max": 200,
        "gender_ranges": None
    },

    "Platelets": {
        "unit": "10^3/uL",
        "min": 150,
        "max": 450,
        "gender_ranges": None
    },

    "WBC": {
        "unit": "10^3/uL",
        "min": 4,
        "max": 11,
        "gender_ranges": None
    }
}


TEST_PANELS = {
    "Complete Blood Count": [
        "Hemoglobin",
        "Platelets",
        "WBC"
    ],

    "Blood Sugar": [
        "Glucose"
    ],

    "Lipid Profile": [
        "Total Cholesterol"
    ]
}


def get_reference_range(test_name, gender):

    test = REFERENCE_RANGES[test_name]

    if test["gender_ranges"]:
        return test["gender_ranges"][gender]

    return test["min"], test["max"]
