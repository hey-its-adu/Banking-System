# Banking System

A simple Banking System web application built using Python and Flask.

## Features

- View account balance
- Deposit money
- Withdraw money
- Validate account numbers
- Validate deposit and withdrawal amounts
- Prevent withdrawals with insufficient balance
- View account-specific transaction history

## Technologies Used

- Python
- Flask
- HTML
- CSS

## Project Structure

```text
Banking-System/
│
├── app.py
│
├── templates/
│   ├── index.html
│   └── history.html
│
└── static/
    └── style.css
```

## Sample Accounts

| Account Number | Initial Balance |
|---|---:|
| 101 | ₹5,000 |
| 102 | ₹3,000 |
| 103 | ₹7,500 |

## Future Improvements

- SQLite database integration
- Permanent transaction storage
- User authentication
- Improved user interface

## Note

Currently, account balances and transaction history are stored in Python memory. They reset when the application restarts.
