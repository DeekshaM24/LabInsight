
# main.py

from reference_ranges import TEST_PANELS, REFERENCE_RANGES

from analyzer import analyze_result

from report_generator import print_report

from history import (
    initialize_storage,
    generate_report_id,
    save_report,
    get_previous_report,
    display_history
)


def get_patient_details():

    print("\n========== PATIENT DETAILS ==========")

    patient_id = input("Enter Patient ID: ").strip()

    if not patient_id:
        print("Patient ID cannot be empty.")
        return None

    patient_name = input("Enter Patient Name: ").strip()

    if not patient_name:
        print("Patient name cannot be empty.")
        return None

    while True:

        gender = input(
            "Enter Gender (Male/Female): "
        ).strip().lower()

        if gender in ["male", "female"]:
            break

        print("Please enter Male or Female.")

    return patient_id, patient_name, gender


def select_test_panel():

    print("\n========== SELECT TEST PANEL ==========")

    panels = list(TEST_PANELS.items())

    for index, (panel, tests) in enumerate(panels, 1):

        print(f"{index}. {panel}")

    print(f"{len(panels) + 1}. All Tests")

    while True:

        try:

            choice = int(input("\nSelect panel: "))

            if 1 <= choice <= len(panels):

                return panels[choice - 1][1]

            elif choice == len(panels) + 1:

                return list(REFERENCE_RANGES.keys())

            else:

                print("Invalid choice.")

        except ValueError:

            print("Please enter a valid number.")


def enter_results(gender):

    selected_tests = select_test_panel()

    results = []

    print("\n========== ENTER TEST RESULTS ==========")

    for test in selected_tests:

        while True:

            try:

                value = float(
                    input(f"Enter {test} value: ")
                )

                if value < 0:
                    print("Value cannot be negative.")
                    continue

                result = analyze_result(
                    test, value, gender
                )

                results.append(result)

                print(
                    "Analysis:",
                    result["status"]
                )

                break

            except ValueError:

                print("Please enter a valid numeric value.")

    return results


def create_new_report():

    patient_details = get_patient_details()

    if patient_details is None:
        return

    patient_id, patient_name, gender = patient_details

    previous_report = get_previous_report(patient_id)

    report_id = generate_report_id()

    results = enter_results(gender)

    print_report(
        patient_id,
        patient_name,
        gender,
        report_id,
        results,
        previous_report
    )

    save_report(
        patient_id,
        patient_name,
        report_id,
        results
    )

    print("\nReport saved successfully!")


def main():

    initialize_storage()

    while True:

        print("\n")
        print("=" * 50)
        print("              LABINSIGHT")
        print("    DIAGNOSTIC REPORT ANALYSIS SYSTEM")
        print("=" * 50)

        print("1. Enter New Patient Report")
        print("2. View Previous Patient Reports")
        print("3. Exit")

        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            create_new_report()

        elif choice == "2":

            patient_id = input(
                "\nEnter Patient ID: "
            ).strip()

            if patient_id:
                display_history(patient_id)
            else:
                print("Patient ID cannot be empty.")

        elif choice == "3":

            print("\nThank you for using LabInsight!")
            print("Application closed.")
            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":

    main()
