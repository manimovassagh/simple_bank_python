from user import user


class Bank:

    def __init__(self):
        self.__accounts = []

    def add_account_to_bank(self, account):
        self.__accounts.append(account)

    def __str__(self):
        account_list_str = "\n".join(str(account) for account in self.__accounts)
        return f"Bank Accounts:\n{account_list_str}"

    def get_accounts(self):
        return self.__accounts

    def transaction_job(self, account: user.Account, receiver_account: user.Account, amount_transfer):
        if amount_transfer > account.amount:
            print("you can not transfer more than your remain amount")
        else:
            account.amount = account.amount - amount_transfer
            for account in self.get_accounts():
                if account.email == receiver_account.email:
                    account.amount = account.amount + amount_transfer
                    print(
                        f"The account {account.email} received {amount_transfer} and now has {account.amount} {account.currency}")
