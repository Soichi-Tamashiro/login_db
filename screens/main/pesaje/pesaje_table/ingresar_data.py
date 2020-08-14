# -*- coding: utf-8 -*-
import sqlite3
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.gridlayout import GridLayout

from kivy.lang import Builder

Builder.load_file('pesaje_table/ingresar_data.kv')

# from kivy.config import Config
# Config.set("graphics", "minimum_width", "800")
# Config.set("graphics", "minimum_height", "600")


class IngresarData(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ingresar_data(App):
    def build(self):
        return IngresarData()


if __name__ == '__main__':
    ingresar_data().run()