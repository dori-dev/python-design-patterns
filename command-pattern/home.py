"""home trade system
using command design patterns"""
from abc import ABC, abstractmethod
from typing import List


class Order(ABC):
    """The basic of home ordering classes
    """
    @abstractmethod
    def execute(self):
        """Execute command or commands
        """
        pass


class HouseTrade:
    """Buying and selling a home
    """

    def buy(self):
        """The buyer buys the house
        """
        print("You are buying this house.")

    def sell(self):
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


class SellHouse(Order):
    """sell a house
    """

    def __init__(self, house: HouseTrade):
        self.house = house

    def execute(self):
        """execute sell command
        """
        self.house.sell()


class Agent:
    """order management
    """

    def __init__(self):
        self.__order_queue: List[Order] = []

    def request_order(self, order: Order):
        self.__order_queue.append(order)

    def place_orders(self):
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
