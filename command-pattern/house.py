"""house trade system
using command design patterns"""
from abc import ABC, abstractmethod
from typing import List


class Order(ABC):
    """The basic of home ordering classes
    """
    @abstractmethod
    def execute(self):
        """execute command or commands
        """

    @abstractmethod
    def describe(self):
        """order description
        """


class HouseTrade:
    """Buying and selling a home
    """

    @staticmethod
    def buy():
        """The buyer buys the house
        """
        print("You are buying this house.")

    @staticmethod
    def sell():
        """The seller is selling the house
        """
        print("You are selling this house")


class BuyHouse(Order):
    """buy a house
    """

    def __init__(self, house: HouseTrade):
        self.house = house

    def execute(self):
        """execute buy command
        """
        self.house.buy()

    def describe(self):
        print("cheap and amazing house")


class SellHouse(Order):
    """sell a house
    """

    def __init__(self, house: HouseTrade):
        self.house = house

    def execute(self):
        """execute sell command
        """
        self.house.sell()

    def describe(self):
        print("big and beautiful house")


class Agent:
    """order management
    """

    def __init__(self):
        self.__order_queue: List[Order] = []

    def request_order(self, order: Order):
        """request a order

        Args:
            order (Order): the order
        """
        self.__order_queue.append(order)

    def place_orders(self):
        """place all orders
        """
        for order in self.__order_queue:
            order.execute()


if __name__ == "__main__":
    house1 = HouseTrade()
    house2 = HouseTrade()
    house3 = HouseTrade()
    buy_house = BuyHouse(house1)
    sell_house = SellHouse(house2)
    house3_order = BuyHouse(house3)

    # take order
    agent = Agent()
    agent.request_order(buy_house)
    agent.request_order(sell_house)
    agent.request_order(house3_order)

    # place orders
    agent.place_orders()
    print()
