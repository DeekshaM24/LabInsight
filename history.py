
# history.py

import csv
import os
from datetime import datetime

REPORT_FOLDER = "reports"

CSV_FILE = os.path.join(
    REPORT_FOLDER, "patient_reports.csv"
)

HEADERS = [
    "patient_id",
    "patient_name",
    "report_id",
    "date",
    "test",
    "value",
    "unit",
    "status"
]


def initialize_storage():

    os.makedirs(REPORT_FOLDER, exist_ok=True)

    if not os.path.exists(CSV_FILE):

        with open(CSV_FILE, "w", newline="") as file:

            writer = csv.DictWriter(
                file, fieldnames=HEADERS
            )

            writer.writeheader()


def generate_report_id():

    return datetime.now().strftime(
        "%Y%m%d%H%M%S%f"
    )


def save_report(patient_id, patient_name,
                report_id, results):

    initialize_storage()

    report_date = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.DictWriter(
            file, fieldnames=HEADERS
        )

        for result in results:

            writer.writerow({
                "patient_id": patient_id,
                "patient_name": patient_name,
                "report_id": report_id,
                "date": report_date,
                "test": result["test"],
                "value": result["value"],
                "unit": result["unit"],
                "status": result["status"]
            })


def get_patient_reports(patient_id):

    initialize_storage()

    reports = {}

    with open(CSV_FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["patient_id"] == patient_id:

                report_id = row["report_id"]

                if report_id not in reports:

                    reports[report_id] = {
                        "date": row["date"],
                        "patient_name": row["patient_name"],
                        "results": {}
                    }

                reports[report_id]["results"][row["test"]] = {
                    "value": float(row["value"]),
                    "unit": row["unit"],
                    "status": row["status"]
                }

    return reports


def get_previous_report(patient_id):

    reports = get_patient_reports(patient_id)

    if not reports:
        return None

    latest_report_id = max(
        reports,
        key=lambda rid: (
            reports[rid]["date"], rid
        )
    )

    return reports[latest_report_id]


def display_history(patient_id):

    reports = get_patient_reports(patient_id)

    if not reports:

        print("\nNo previous reports found.")
        return

    print("\n========== PATIENT HISTORY ==========")

    for report_id, report in sorted(reports.items()):

        print("\nReport ID:", report_id)
        print("Date:", report["date"])

        for test, result in report["results"].items():

            print(
                f"{test}: {result['value']} "
                f"{result['unit']} "
                f"[{result['status']}]"
            )

    print("\n=====================================")
