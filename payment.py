"""payment management system using proxy pattern
"""
from abc import ABC, abstractmethod


class Pay(ABC):
    """Payment Abstract Class"""
    @abstractmethod
    def do_pay(self):
        """do pay
        """


class Bank(Pay):
    """Bank Management
    """

    def __init__(self):
        self.card = None
        self.account = None

    def __get_card(self):
        """get card number
        """
        return self.card

    def __check_inventory(self):
        print("Bank: Checking that account of [", self.__get_card(
        ), "] have enough money or not..")
        return False

    def set_card(self, card):
        """set card number
        """
        self.card = card

    def do_pay(self):
        """do payment

        Returns:
            bool: True for paid False for not enough money
        """
        if self.__check_inventory():
            print("Bank: Successfully paid.")
            return True
        print("Bank: Your money is not enough.")
        return False


class Card(Pay):
    """Card Class
    """

    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        """do payment with this card

        Returns:
            bool: True for paid False for not enough money
        """
        card = input("Enter your card number: ")
        self.bank.set_card(card)
        return self.bank.do_pay()


class You:
    """Manage User
    """

    def __init__(self):
        print("You: I want to buy a product.")
        self.card = Card()
        self.is_bought = None

    def pay(self):
        """pay with card
        is_bought = True if paid and False if not enough money
        """
        self.is_bought = self.card.do_pay()

    def __del__(self):
        if self.is_bought:
            print("You: I bought the product.")
        else:
            print("You: My money is not enough to buy.")


if __name__ == "__main__":
    you = You()
    you.pay()
