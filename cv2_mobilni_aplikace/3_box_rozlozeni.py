from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from random import random

class MobilniAplikace(App):
    def build(self):
        
        rozlozeni = BoxLayout(
            padding=[50, 30, 50, 30],   #padding = [50, 30] #padding = 50
            orientation='vertical',     #vertical, horizontal
            spacing = 20
        )

        for idx_tlacitka in range(5):
            barva = [random() for i in range(3)]
            barva.append(1)
            tlacitko = Button(
                text=f"Tlacitko {idx_tlacitka}",
                background_color = barva
            )
            rozlozeni.add_widget(tlacitko)
        
        return rozlozeni

if __name__ == "__main__":
    app = MobilniAplikace()
    app.run()