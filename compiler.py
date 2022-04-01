"""Implement compiler using template-method pattern"""

from abc import ABC, abstractmethod


class Compiler(ABC):
    """Abstract Compiler Class
    """

    @abstractmethod
    def collect_source(self):
        """collect source code
        """

    @abstractmethod
    def compile_to_binary(self):
        """compile codes to binary
        """

    @abstractmethod
    def run(self):
        """run source code
        """

    def compile_and_run(self):
        """compile and run codes,
        with call all methods!
        """
        self.collect_source()
        self.compile_to_binary()
        self.run()


class AndroidCompiler(Compiler):
    """android source code compiler
    """

    def collect_source(self):
        print("collecting source code...")

    def compile_to_binary(self):
        print("compiling source code to binary code...")

    def run(self):
        print("compiler is running...")


if __name__ == "__main__":
    android_store_app = AndroidCompiler()
    android_store_app.compile_and_run()
