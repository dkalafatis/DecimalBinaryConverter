def decimal_to_binary(decimal):
    """Converts a decimal number to binary."""
    if decimal >= 0:
        return bin(decimal).replace("0b", "")
    else:
        return "Invalid input. Decimal number must be non-negative."


def binary_to_decimal(binary):
    """Converts a binary number to decimal."""
    try:
        return int(binary, 2)
    except ValueError:
        return "Invalid input. Binary number must contain only 0s and 1s."


def main():
    while True:
        print("\nChoose the type of conversion:")
        print("1. Decimal to Binary")
        print("2. Binary to Decimal")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            decimal = input("Enter a non-negative decimal number: ")
            if decimal.isdigit():
                decimal = int(decimal)
                print(f"Binary equivalent: {decimal_to_binary(decimal)}")
            else:
                print("Invalid input. Please enter a non-negative integer.")
        elif choice == '2':
            binary = input("Enter a binary number (only 0s and 1s): ")
            if all(c in '01' for c in binary):
                print(f"Decimal equivalent: {binary_to_decimal(binary)}")
            else:
                print("Invalid input. Binary number must contain only 0s and 1s.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
