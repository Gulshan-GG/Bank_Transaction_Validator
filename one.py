"""Bank Transaction Validator.

The program accepts transactions from the user, saves them in
transactions.txt, then reads that file to validate them.
"""

OPENING_BALANCE = 10_000
MAX_TRANSACTION_AMOUNT = 100_000
INPUT_FILE = "transaction.txt"
VALID_OUTPUT_FILE = "valid_transactions.txt"


def validate_transaction(transaction_type, amount_text, balance):
    """Return (is_valid, message, amount) for one transaction."""
    transaction_type = transaction_type.strip()
    amount_text = amount_text.strip()

    try:
        amount = int(amount_text)
    except ValueError:
        return False, f"amount '{amount_text}' is not a number.", None

    if transaction_type not in ("Deposit", "Withdraw"):
        return False, f"unknown type '{transaction_type}'.", None
    if amount <= 0:
        return False, "amount must be positive.", None
    if amount > MAX_TRANSACTION_AMOUNT:
        return False, f"exceeds limit of {MAX_TRANSACTION_AMOUNT}.", None
    if transaction_type == "Withdraw" and amount > balance:
        return False, "insufficient balance.", None

    return True, "", amount


def collect_transactions(input_file=INPUT_FILE):
    """Get transaction lines from the user and save them to a text file."""
    print("Enter transactions one at a time.")
    print("Choose an option from the menu, then enter the amount.")
    print("For a transfer you do not want to make, enter 0 as its amount.")
    transactions = []

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Finish and process transactions")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "4":
            break

        transaction_types = {
            "1": "Deposit",
            "2": "Withdraw",
            "3": "Transfer",
        }
        transaction_type = transaction_types.get(choice)
        if transaction_type is None:
            print("Invalid choice. Please choose a number from 1 to 4.")
            continue

        amount = input(f"Enter {transaction_type} amount: ").strip()
        if transaction_type == "Transfer" and amount == "0":
            print("No transfer entered.")
            continue

        transactions.append(f"{transaction_type},{amount}")

    try:
        with open(input_file, "w", encoding="utf-8") as file:
            for transaction in transactions:
                file.write(transaction + "\n")
        print(f"Transactions saved to '{input_file}'.\n")
        return True
    except OSError as error:
        print(f"Error writing '{input_file}': {error}")
        return False


def process_transactions(input_file=INPUT_FILE, valid_output_file=VALID_OUTPUT_FILE):
    """Read, validate, report, and save valid bank transactions."""
    balance = OPENING_BALANCE
    valid_count = 0
    invalid_count = 0
    valid_lines = []

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            transactions = file.readlines()
    except FileNotFoundError:
        print(f"Error: '{input_file}' was not found.")
        return
    except OSError as error:
        print(f"Error reading '{input_file}': {error}")
        return

    for line_number, raw_line in enumerate(transactions, start=1):
        line = raw_line.strip()
        if not line:
            invalid_count += 1
            print(f"Line {line_number}: Invalid - empty line.")
            continue

        parts = line.split(",")
        if len(parts) != 2:
            invalid_count += 1
            print(f"Line {line_number}: Invalid - format must be Type,Amount.")
            continue

        transaction_type, amount_text = parts
        is_valid, reason, amount = validate_transaction(
            transaction_type, amount_text, balance
        )

        if not is_valid:
            invalid_count += 1
            print(f"Line {line_number}: Invalid - {reason}")
            continue

        transaction_type = transaction_type.strip()
        if transaction_type == "Deposit":
            balance += amount
        else:
            balance -= amount

        valid_count += 1
        valid_lines.append(f"{transaction_type},{amount}\n")
        print(f"Line {line_number}: Valid | Balance: {balance}")

    try:
        with open(valid_output_file, "w", encoding="utf-8") as file:
            file.writelines(valid_lines)
    except OSError as error:
        print(f"Error writing '{valid_output_file}': {error}")

    print(f"Valid: {valid_count} | Invalid: {invalid_count} | Final balance: {balance}")


if __name__ == "__main__":
    if collect_transactions():
        process_transactions()
