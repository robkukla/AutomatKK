from ZUS import Zus
from time import sleep
from pywinauto.application import Application
from uniwersalne_funkcje import *


class PueZus(Zus):
    def __init__(self):
        self.testName = "Nowa subskryupcja"

    def nowa_subskrypcja(self):
        logging.info("%s - Test: %s", "2", self.testName)
