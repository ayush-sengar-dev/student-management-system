from database import connect_database


def fees(student):

    print("\n" + "=" * 90)
    print("                                      FEES")
    print("=" * 90)

    connection = connect_database()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            fee_id,
            fee_type,
            amount,
            paid_amount,
            amount - paid_amount AS remaining,
            due_date,
            payment_status,
            fee_category
        FROM fees
        WHERE student_id = %s
        ORDER BY
            CASE
                WHEN fee_category = 'Mandatory' THEN 1
                ELSE 2
            END,
            fee_id
    """, (student["student_id"],))

    fee_records = cursor.fetchall()

    cursor.close()
    connection.close()

    if not fee_records:
        print("No fee records found.")
        return

    mandatory_total = 0
    mandatory_paid = 0
    mandatory_remaining = 0

    optional_total = 0
    optional_paid = 0
    optional_remaining = 0

    # --------------------------------------------------------
    # MANDATORY FEES
    # --------------------------------------------------------

    print("\nMANDATORY FEES")
    print("-" * 90)

    print(
        f"{'Fee Type':<25}"
        f"{'Amount':>12}"
        f"{'Paid':>12}"
        f"{'Remaining':>14}"
        f"{'Status':>12}"
    )

    print("-" * 90)

    for fee in fee_records:

        if fee["fee_category"] == "Mandatory":

            amount = float(fee["amount"])
            paid = float(fee["paid_amount"])
            remaining = float(fee["remaining"])

            print(
                f"{fee['fee_type']:<25}"
                f"₹{amount:>10.2f}"
                f"₹{paid:>10.2f}"
                f"₹{remaining:>12.2f}"
                f"{fee['payment_status']:>12}"
            )

            mandatory_total += amount
            mandatory_paid += paid
            mandatory_remaining += remaining

    # --------------------------------------------------------
    # OPTIONAL SERVICES
    # --------------------------------------------------------

    print("\nOPTIONAL SERVICES")
    print("-" * 90)

    optional_found = False

    print(
        f"{'Service':<25}"
        f"{'Amount':>12}"
        f"{'Paid':>12}"
        f"{'Remaining':>14}"
        f"{'Status':>12}"
    )

    print("-" * 90)

    for fee in fee_records:

        if fee["fee_category"] == "Optional":

            optional_found = True

            amount = float(fee["amount"])
            paid = float(fee["paid_amount"])
            remaining = float(fee["remaining"])

            print(
                f"{fee['fee_type']:<25}"
                f"₹{amount:>10.2f}"
                f"₹{paid:>10.2f}"
                f"₹{remaining:>12.2f}"
                f"{fee['payment_status']:>12}"
            )

            optional_total += amount
            optional_paid += paid
            optional_remaining += remaining

    if not optional_found:
        print("No optional services.")

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    total_amount = mandatory_total + optional_total
    total_paid = mandatory_paid + optional_paid
    total_remaining = mandatory_remaining + optional_remaining

    print("\n" + "=" * 90)
    print("                                  FEE SUMMARY")
    print("=" * 90)

    print(f"Mandatory Fees : ₹{mandatory_total:,.2f}")
    print(f"Optional Fees  : ₹{optional_total:,.2f}")
    print("-" * 90)
    print(f"Total Fee      : ₹{total_amount:,.2f}")
    print(f"Total Paid     : ₹{total_paid:,.2f}")
    print(f"Remaining      : ₹{total_remaining:,.2f}")
    print("=" * 90)