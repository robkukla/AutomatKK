from win32api import GetSystemMetrics
import pywinauto


def pozycja(self):
    list_pos_x = int(GetSystemMetrics(0) / 2)
    list_pos_y = int(GetSystemMetrics(1) * 1 / 3)
    pywinauto.mouse.right_click(coords=(list_pos_x, list_pos_y))


def pozycja2(self):
    list_pos_x = int(GetSystemMetrics(0) / 2)
    list_pos_y = int(GetSystemMetrics(1) * 1 / 2)
    pywinauto.mouse.right_click(coords=(list_pos_x, list_pos_y))