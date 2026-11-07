import flask

app = flask.Flask(__name__)

accounts = {
    101: 5000,
    102: 3000,
    103: 7500
}

transaction_history = []


@app.route("/")
def home():
    return flask.render_template("index.html")


@app.route("/about")
def about():
    return "This is the Banking System application."


@app.route("/bank/<name>")
def name(name):
    return f"Welcome, {name}!"


@app.route("/balance", methods=["GET"])
def balance():
    try:
        account_id = int(flask.request.args.get("acc_id"))

        if account_id in accounts:
            return f"Your account number is {account_id}<br>Balance: {accounts[account_id]}"
        else:
            return f"account {account_id} does not exist"

    except (ValueError, TypeError):
        return "Please enter a valid account ID"


@app.route("/deposit", methods=["POST"])
def deposit():
    try:
        account_id = int(flask.request.form.get("acc_id"))

        try:
            amount = int(flask.request.form.get("amount"))

            if account_id in accounts:
                if amount > 0:
                    accounts[account_id] += amount

                    transaction_history.append({
                        "account_id": account_id,
                        "type": "deposit",
                        "amount": amount,
                        "balance": accounts[account_id]
                    })

                    return f"Account Number: {account_id}<br>Deposited Amount: {amount}<br>Updated Balance: {accounts[account_id]}<br>Deposited Successfully!"

                else:
                    return "enter valid amount"

            else:
                return f"account {account_id} does not exist"

        except (ValueError, TypeError):
            return "Please enter a valid amount"

    except (ValueError, TypeError):
        return "Please enter a valid account ID"


@app.route("/withdraw", methods=["POST"])
def withdraw():
    try:
        account_id = int(flask.request.form.get("acc_id"))

        try:
            to_get = int(flask.request.form.get("withdraw_amount"))

            if account_id in accounts:
                if to_get > 0:
                    if accounts[account_id] >= to_get:
                         accounts[account_id] -= to_get
 
                         transaction_history.append({
                            "account_id": account_id,
                            "type": "withdraw",
                            "amount": to_get,
                            "balance": accounts[account_id]
                        })

                         return f"Account Number: {account_id}<br>Withdrawn amount: {to_get}<br>Remaining balance: {accounts[account_id]}<br>Withdrawal successful."
                    else:
                       return"Insufficient balance"    
                else:
                   return "enter valid amount"
   
            else:
                   return f"account {account_id} does not exist"

        except (ValueError, TypeError):
            return "Please Enter valid amount"

    except (TypeError, ValueError):
        return "Please enter a valid account ID"


@app.route("/history", methods=["GET"])
def history():
    
    transactions=[]

    try:
        account_id = int(flask.request.args.get("acc_id"))

        if account_id in accounts:
         
            for i in transaction_history:
                if i["account_id"] == account_id:
                  transactions.append(i)
            if transactions:
               return flask.render_template("history.html", transactions=transactions,account_id=account_id)
               
            else:
                return "No transaction history found."

        else:
            return f"Account {account_id} does not exist"

    except (ValueError, TypeError):
        return "Please enter a valid account ID"


if __name__ == "__main__":
    app.run(debug=True)