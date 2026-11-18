
# report_generator.py


def print_report(patient_id, patient_name,
                 gender, report_id, results,
                 previous_report=None):

    print("\n")
    print("=" * 65)
    print("             LABINSIGHT")
    print("    DIAGNOSTIC REPORT ANALYSIS SYSTEM")
    print("=" * 65)

    print("Patient ID :", patient_id)
    print("Patient Name:", patient_name)
    print("Gender     :", gender.capitalize())
    print("Report ID  :", report_id)

    print("-" * 65)

    print(
        f"{'TEST':<20}"
        f"{'RESULT':<13}"
        f"{'REFERENCE':<17}"
        f"{'STATUS':<12}"
    )

    print("-" * 65)

    for result in results:

        test = result["test"]
        value = result["value"]
        unit = result["unit"]
        minimum = result["minimum"]
        maximum = result["maximum"]
        status = result["status"]

        reference = f"{minimum}-{maximum}"

        flag = "!" if status in ["LOW", "HIGH"] else ""

        print(
            f"{test:<20}"
            f"{str(value) + ' ' + unit:<13}"
            f"{reference:<17}"
            f"{flag + ' ' + status:<12}"
        )

    print("-" * 65)

    print("\nRESULT SUMMARY")

    low = sum(1 for r in results if r["status"] == "LOW")
    high = sum(1 for r in results if r["status"] == "HIGH")
    normal = sum(1 for r in results if r["status"] == "NORMAL")

    print("Low Results   :", low)
    print("Normal Results:", normal)
    print("High Results  :", high)

    print("\n========== TREND COMPARISON ==========")

    if previous_report is None:

        print("No previous report available.")
        print("This is the patient's first report.")

    else:

        print("Previous report date:",
              previous_report["date"])

        previous_results = previous_report["results"]

        for result in results:

            test = result["test"]

            if test in previous_results:

                old_value = previous_results[test]["value"]
                new_value = result["value"]

                difference = new_value - old_value

                if difference > 0:
                    change = "INCREASED"

                elif difference < 0:
                    change = "DECREASED"

                else:
                    change = "UNCHANGED"

                print(
                    f"{test}: {old_value} -> {new_value} "
                    f"({change}, difference: {difference:+.2f})"
                )

            else:

                print(
                    f"{test}: No previous value available."
                )

    print("=" * 65)

    print("\nNote: This report uses configured sample ranges.")
    print("It does not provide a medical diagnosis.")
    print("=" * 65)
