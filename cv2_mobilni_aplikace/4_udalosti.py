from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from random import random

class MobilniAplikace(App):
    
    def build(self):
        
        rozlozeni = BoxLayout(
            padding=[50, 30, 50, 30],
            orientation='vertical',
            spacing = 20
        )

        for idx_tlacitka in range(5):
            barva = [random() for i in range(3)]
            barva.append(1)
            tlacitko = Button(
                text=f"Tlacitko {idx_tlacitka}",
                background_color = barva
            )
            tlacitko.bind(on_press=self.stisk_tlacitka)
            rozlozeni.add_widget(tlacitko)
        
        return rozlozeni

    def stisk_tlacitka(self, instance):
        print('Stiskl jsi tlacitko!')

if __name__ == "__main__":
    app = MobilniAplikace()
    app.run()