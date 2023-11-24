from bank.user import Account
from bank.bank import Bank


def main():
    bank = Bank()
    mani_acc = Account("mani@gmail", 140)
    sahar_acc = Account("sahar@gmail", 490)
    sahar_acc.withdraw(12.40)
    sahar_acc.deposit_amount(12.44)
    bank.add_account_to_bank(mani_acc)
    bank.add_account_to_bank(sahar_acc)
    print(bank)


if __name__ == "__main__":
    main()
