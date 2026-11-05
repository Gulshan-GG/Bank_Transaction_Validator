
# Bank Transaction Validation System

## 1. Project Overview

The Bank Transaction Validation System is a Python-based project that reads bank transactions from a text file, validates each transaction, updates the account balance, and saves all valid transactions into a separate output file.

The project helps identify invalid transactions and maintain an accurate account balance.

## 2. Features

- Reads transactions from a text file.
- Supports Deposit and Withdraw transactions.
- Checks whether the amount is numeric.
- Rejects zero and negative amounts.
- Applies a maximum transaction limit of 100000.
- Checks insufficient account balance.
- Counts valid and invalid transactions.
- Updates the account balance automatically.
- Saves valid transactions into an output file.
- Displays a final transaction summary.

## 3. Technologies Used

- Python 3
- VS Code
- Text Files (.txt)

## 4. Project Structure

```text
Bank_Transaction_Project/
│
├── main.py
├── transactions.txt
├── valid_transactions.txt
└── README.md
```

## 5. Input File Format

Create a file named `transactions.txt`.

Write transactions in the following format:

```text
deposit,5000
withdraw,2000
deposit,3000
withdraw,1500
deposit,abc
withdraw,20000
```

**Note:** Each transaction must contain a transaction type and amount separated by a comma.

## 6. How to Run the Project

1. Install Python 3 on your computer.
2. Open the project folder in VS Code.
3. Create the required Python and text files.
4. Add transaction details to `transactions.txt`.
5. Open the terminal in VS Code.
6. Run the following command:

```bash
python main.py
```

## 7. Output

The program displays:

- Transaction status (Valid or Invalid).
- Reason for invalid transactions.
- Updated account balance.
- Total valid transactions.
- Total invalid transactions.
- Final account balance.

## 8. Output File

The program automatically creates:

`valid_transactions.txt`

This file stores only successfully validated transactions.

## 9. Validation Rules

| Condition | Result |
|---|---|
| Valid deposit | Accepted |
| Valid withdrawal | Accepted |
| Non-numeric amount | Rejected |
| Zero amount | Rejected |
| Negative amount | Rejected |
| Amount above 100000 | Rejected |
| Insufficient balance | Rejected |
| Unknown transaction type | Rejected |

## 10. Conclusion

This project demonstrates the practical implementation of Python programming concepts such as functions, conditional statements, loops, exception handling, file handling, lists, and string manipulation.

It provides a simple way to validate bank transactions and manage account balances.
