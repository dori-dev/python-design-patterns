"""products store system made with mvc design pattern!
"""
from abc import ABC, abstractmethod


class Model(ABC):
    """Model Abstract Class
    """
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def get(self, product):
        """Returns an object with a .items() call method
        that iterates over key,value pairs of its information
        """

    @property
    @abstractmethod
    def item_type(self):
        """type of item
        """


class ProductModel(Model):
    """Product Model Class
    """
    class Price(float):
        """A polymorphic way to pass a float with a particular
        __str__ functionality."""

        def __str__(self):
            return f"{self:.2f}"

    products = {
        "milk": {"price": Price(1.50), "quantity": 10},
        "eggs": {"price": Price(0.20), "quantity": 100},
        "cheese": {"price": Price(2.00), "quantity": 10},
    }

    item_type = "product"

    def __iter__(self):
        for product in self.products:
            yield product

    def get(self, product):
        """get product info

        Args:
            product (str): name of product

        Returns:
            dict: product information
        """
        null_product = {"price": 0.0, "quantity": 0}
        return self.products.get(product, null_product)


class View(ABC):
    """View Abstract Class
    """
    @abstractmethod
    def show_item_list(self, item_type: str, item_list: list):
        """show list of items
        """

    @abstractmethod
    def show_item_information(self, item_type, item_name, item_info):
        """Will look for item information by iterating over key,value pairs
        yielded by item_info.items()"""


class ConsoleView(View):
    """Console View Class
    """

    def show_item_list(self, item_type, item_list):
        """show item list

        Args:
            item_type (str): type of items
            item_list (list): list of items
        """
        print(item_type.upper() + " LIST:")
        for item in item_list:
            print(item)
        print("")

    def show_item_information(self, item_type: str,
                              item_name: str,
                              item_info: dict):
        print(item_type.upper() + " INFORMATION:")
        print_out = f"Name: {item_name}"
        for key, value in item_info.items():
            print_out += f", {str(key).title()}: {str(value)}"
        print_out += "\n"
        print(print_out)


class Controller:
    """Controller Class
    """

    def __init__(self, model, view):
        self.model: Model = model
        self.view: View = view

    def show_items(self):
        """show items of `item_type`
        """
        items: list = list(self.model)
        item_type: str = self.model.item_type
        self.view.show_item_list(item_type, items)

    def show_item_information(self, item_name):
        """Show information about a `item_type` item.

        Args:
            item_name (str): the name of `item_type` item to show info
        """
        item_info = self.model.get(item_name)
        item_type = self.model.item_type
        self.view.show_item_information(item_type, item_name, item_info)


if __name__ == "__main__":
    the_model = ProductModel()
    the_view = ConsoleView()
    controller = Controller(the_model, the_view)
    controller.show_items()
    controller.show_item_information("cheese")
    controller.show_item_information("eggs")
    controller.show_item_information("milk")
    controller.show_item_information("arepas")
