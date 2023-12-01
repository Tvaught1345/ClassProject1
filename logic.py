from PyQt6.QtWidgets import *
from bank import *

class Logic(QMainWindow, Ui_Accounts):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.__check_balance = 10000
        self.__save_balance = 10000
        self.__account_balance = 0
        self.amount = 0
        self.name = 'none'

        self.cbalance.setText(f'${self.__check_balance:.2f}')
        self.sbalance.setText(f'${self.__save_balance:.2f}')
        self.checking_button.clicked.connect(lambda : self.checking_tab())
        self.savings_button.clicked.connect(lambda : self.savings_tab())
        self.deposit_button.clicked.connect(lambda: self.deposit_tab(self.amount))
        self.withdrawal_button.clicked.connect(lambda: self.withdrawal_tab(self.amount))


    def checking_tab(self) -> None:
        """
        Method to get checking account balance and change variable values.
        """
        self.balance.setText(f'${self.get_check():.2f}')
        self.__account_balance = self.__check_balance
        self.name = 'Checking'

    def savings_tab(self) -> None:
        """
        Method to get savings account balance and change variable values.
        """
        self.balance.setText(f'${self.get_save():.2f}')
        self.__account_balance = self.__save_balance
        self.name = 'Savings'

    def deposit_tab(self, amount) -> None:
        """
        Method to deposit a given amount in to selected account.
        """
        self.amount = float(self.doubleSpinBox.value())
        if self.amount > 0:
            self.__account_balance += self.amount
            self.final_message.setText(f'You have successfully deposited\n${self.amount:.02f} into your\n{self.name} account.\nNew Balance: ${self.__account_balance:.2f}')
            if self.name == "Checking":
                self.__check_balance = self.__account_balance
                self.cbalance.setText(f'${self.__check_balance:.2f}')
            elif self.name == "Savings":
                self.__save_balance = self.__account_balance
                self.sbalance.setText(f'${self.__save_balance:.2f}')
        else:
            self.final_message.setText(f'Error: Please enter amount greater than zero')


    def withdrawal_tab(self,amount) -> None:
        """
        Method to withdrawal a given amount from a selected account.
        """
        self.amount = float(self.doubleSpinBox.value())
        if self.amount > 0 and self.amount < self.__account_balance:
            self.__account_balance -= self.amount
            self.final_message.setText(
                f'You have successfully withdrawn\n${self.amount:.02f} from your\n{self.name} account.\nNew Balance: ${self.__account_balance:.2f}')
            if self.name == "Checking":
                self.__check_balance = self.__account_balance
                self.cbalance.setText(f'${self.__check_balance:.2f}')
            elif self.name == "Savings":
                self.__save_balance = self.__account_balance
                self.sbalance.setText(f'${self.__save_balance:.2f}')
        else:
            self.final_message.setText(f'Error: Please enter amount greater than zero\nand less than current account balance')


    def get_check(self):
        """
        Method to get checking account balance.
        :return: Checking account balance.
        """
        return self.__check_balance

    def get_save(self):
        """
        Method to get savings account balance.
        :return: Savings account balance.
        """
        return self.__save_balance