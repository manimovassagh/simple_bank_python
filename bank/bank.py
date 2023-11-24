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
