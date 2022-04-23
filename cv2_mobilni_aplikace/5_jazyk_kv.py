from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from random import random

#https://kivy.org/doc/stable/guide/lang.html
class MobilniAplikace(App):
    def build(self):
        return Button()

    def stisk_tlacitka(self):
        print('Stiskl jsi tlacitko!')

if __name__ == "__main__":
    app = MobilniAplikace()
    app.run()