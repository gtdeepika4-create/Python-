def read_float(prompt):
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Enter a value such as 8.5.")

try:
    farmer_id = input("Enter Farmer ID: ").strip()
    litres = read_float("Enter milk quantity in litres: ")
    fat = read_float("Enter fat percentage: ")
    snf = read_float("Enter SNF percentage: ")

    if not farmer_id:
        print("Invalid entry: Farmer ID cannot be blank.")
    elif litres < 0:
        print("Invalid entry: Milk quantity cannot be negative.")
    elif not 2.0 <= fat <= 7.0:
        print("Invalid entry: Fat must be between 2.0 and 7.0.")
    elif snf <= 0:
        print("Invalid entry: SNF must be positive.")
    else:
        print(f"Farmer ID: {farmer_id}")
        print(f"Litres: {litres:8.2f}")
        print(f"Fat: {fat:8.2f}")
        print(f"SNF: {snf:8.2f}")
except KeyboardInterrupt:
    print("\nInput cancelled.")
