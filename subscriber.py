"""subscriber management system using observer pattern
"""
from abc import ABC, abstractmethod
from typing import List


class Publisher:
    """book publisher class
    """

    def __init__(self):
        self.__subscribers: List[Subscriber] = []
        self.__latest_books = None

    def register(self, subscriber: object):
        """registered subscriber(add it in subscribers list)

        Args:
            subscriber (object): the subscriber object
        """
        self.__subscribers.append(subscriber)

    def un_register(self) -> object:
        """un register last subscriber

        Returns:
            Subscriber: the subscriber object
        """
        return self.__subscribers.pop()

    def get_subscribers(self) -> list:
        """get all subscribers

        Returns:
            list: list of subscriber names
        """
        return list(
            map(lambda subscriber: subscriber.get_name(), self.__subscribers)
        )

    def add_book(self, book: str):
        """change latest book

        Args:
            books (str): new book
        """
        self.__latest_books = book

    def get_books(self) -> str:
        """get latest book

        Returns:
            str: new book alert
        """
        return f'newly published "{self.__latest_books}"'

    def notify_all_subscribers(self):
        """send notify to all subscribers
        with call update() method
        """
        for subscriber in self.__subscribers:
            subscriber.update()


class Subscriber(ABC):
    """subscriber abstract class
    """
    @abstractmethod
    def update(self):
        """update subscribers
        """

    @abstractmethod
    def get_name(self) -> str:
        """get name(type) of subscribers
        """


class SMSSubscriber(Subscriber):
    """sms subscribers management
    """

    def __init__(self, publisher: Publisher):
        self.publisher = publisher
        # register itself
        self.publisher.register(self)

    def update(self):
        print(f'"{self.get_name()}" {self.publisher.get_books()}')

    def get_name(self) -> str:
        return "sms subscribers"


class EmailSubscriber(Subscriber):
    """email subscribers management
    """

    def __init__(self, publisher: Publisher):
        self.publisher = publisher
        # register itself
        self.publisher.register(self)

    def update(self):
        print(f'<{self.get_name()}> {self.publisher.get_books()}')

    def get_name(self) -> str:
        return "email subscribers"


class OtherSubscriber(Subscriber):
    """other subscribers management
    """

    def __init__(self, publisher: Publisher):
        self.publisher = publisher
        # register itself
        self.publisher.register(self)

    def update(self):
        print(f':{self.get_name()}: {self.publisher.get_books()}')

    def get_name(self) -> str:
        return "other subscribers"


if __name__ == "__main__":
    # create subject
    the_publisher = Publisher()
    # register all observers
    for each_subscriber in [SMSSubscriber, EmailSubscriber, OtherSubscriber]:
        each_subscriber(the_publisher)
    # add book
    the_publisher.add_book("Django for Professionals")
    # notify this event(add book) with `update`
    the_publisher.notify_all_subscribers()
    # other methods
    print("all subscriber:", the_publisher.get_subscribers())
    print("un register:", the_publisher.un_register().get_name())
    print("subscribers:", the_publisher.get_subscribers())
