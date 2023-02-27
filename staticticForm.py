import customtkinter as ctk
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from MySQLAdapt import SQL

class StaticticForm(ctk.CTk):
     def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.geometry("700x500")
        self.title("Статистика")

        # Получение данных из таблицы zakaz
        data = SQL.get_zakaz_data()

        dates = [row[0] for row in data]
        numberOfGoods = [row[1] for row in data]
        plt.plot(dates, numberOfGoods,  marker = 'o')
        plt.ylabel('Количество товаров')
        plt.xlabel('Дата')

        # Отображение графика
        plt.show()
