from banking import bank as b
from user import user




def main():
    bank = b.Bank()
    mani_acc = user.Account("mani@gmail", 140)
    sahar_acc = user.Account("sahar@gmail", 490)
    sahar_acc.withdraw(12.40)
    sahar_acc.deposit_amount(12.44)
    bank.add_account_to_bank(mani_acc)
    bank.add_account_to_bank(sahar_acc)
    bank.transaction_job(sahar_acc, mani_acc, 12.44)
    bank.transaction_job(sahar_acc, mani_acc, 50)
    bank.transaction_job(sahar_acc, mani_acc, 100)
    bank.transaction_job(sahar_acc, mani_acc, 100)
    bank.transaction_job(sahar_acc, mani_acc, 100)
    bank.transaction_job(sahar_acc, mani_acc, 100)
    print(bank)


def prin_me_alone(self, check) -> int:
    return 2


if __name__ == "__main__":

    main()
