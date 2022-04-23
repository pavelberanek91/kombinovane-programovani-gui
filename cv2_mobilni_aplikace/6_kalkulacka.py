from ast import operator
import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from numpy import spacing

class Kalkulacka(App):


    def build(self):
        
        self.operatory = ["/", "*", "+", "-"]
        self.posledni_tlacitko = None

        hlavni_rozlozeni = BoxLayout(
            orientation="vertical",
            spacing=0
        )

        self.displej = TextInput(
            multiline=False, 
            readonly=True, 
            halign="right", 
            font_size=55
        )
        hlavni_rozlozeni.add_widget(self.displej)

        tlacitka = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for radek_tlacitek in tlacitka:
            horizontalni_rozlozeni = BoxLayout()
            for popisek_tlacitka in radek_tlacitek:
                tlacitko = Button(
                    text=popisek_tlacitka,
                    pos_hint={
                        "center_x": 0.5, 
                        "center_y": 0.5},
                )
                tlacitko.bind(on_press=self.stisk_tlacitka)
                horizontalni_rozlozeni.add_widget(tlacitko)
            hlavni_rozlozeni.add_widget(horizontalni_rozlozeni)

        tlacitko_rovnitko = Button(
            text="=", 
            pos_hint={
                "center_x": 0.5, 
                "center_y": 0.5
            }
        )
        tlacitko_rovnitko.bind(on_press=self.vypocitej)
        hlavni_rozlozeni.add_widget(tlacitko_rovnitko)

        return hlavni_rozlozeni 


    def stisk_tlacitka(self, instance):
        zadani_vypoctu = self.displej.text
        popisek_tlacitka = instance.text

        #mazani reseni
        if popisek_tlacitka == "C":
            self.displej.text = ""
        else:
            #ochrana proti dvoum za sebou dvoucim operacim
            if self.posledni_tlacitko in self.operatory and popisek_tlacitka in self.operatory:
                symboly_vypoctu = list(zadani_vypoctu)
                symboly_vypoctu[-1] = popisek_tlacitka
                self.displej.text = "".join(symboly_vypoctu)
                return
            #ochrana proti prvnimu znaku jako operator misto cisla
            elif zadani_vypoctu == "" and popisek_tlacitka in self.operatory:
                return
            else:
                #aktualizace reseni
                novy_text = zadani_vypoctu + popisek_tlacitka
                self.displej.text = novy_text

        self.posledni_tlacitko = popisek_tlacitka


    def vypocitej(self, instance):
        text = self.displej.text
        if text and list(text)[-1] not in self.operatory:
            reseni = str(eval(self.displej.text))
            self.displej.text = reseni


if __name__ == "__main__":
    app = Kalkulacka()
    app.run()