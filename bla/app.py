#!python3 -m pip install virtualenv
#!python3 -m pip install venv

#!python3 -m venv venv
#!source venv/bin/activate
#!./venv/scripts/Activate.bat

#!python3 -m pip install kivy

#!python3 -m pip freeze > requirements.txt

#!deactivate

#!python3 -m pip install -r requirements.txt

#zdrojaky: github.com/pavelberanek91/kombinovane-programovani-gui

from kivy.app import App as KivyApp
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from random import random

class MobilniAplikace(KivyApp):
    
    def build(self):

        self._posledni_tlacitko = None
        self._operatory = ["/","*","-","+"]

        vnejsi_rozlozeni = BoxLayout(
            orientation = "vertical", #horizontal
            spacing = 0
        )

        self.displej = TextInput(
            readonly = True,
            multiline = False,
            halign = "right",
            font_size = 55
        )
        vnejsi_rozlozeni.add_widget(self.displej)

        #3. pridat nova tlacitka (zavorky, sinus, cosinus)
        tlacitka = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        for radek_tlacitek in tlacitka:
            vnitrni_rozlozeni = BoxLayout() #orientation = Horizontal
            for popisek_tlacitka in radek_tlacitek:
                nahodna_barva = [random() for _ in range(3)]
                nahodna_barva.append(1)
                tlacitko = Button(
                    text = popisek_tlacitka,
                    pos_hint = {
                        "center_x": 0.5,
                        "center_y": 0.5,
                    },
                    background_color = nahodna_barva
                )
                tlacitko.bind(
                    on_press = self._stisk_tlacitka
                )
                vnitrni_rozlozeni.add_widget(tlacitko)
            vnejsi_rozlozeni.add_widget(vnitrni_rozlozeni)

        tlacitko_rovnitko = Button(
            text= "=",
            pos_hint = {
                "center_x": 0.5,
                "center_y": 0.5,
            }
        )
        tlacitko_rovnitko.bind(on_press = self._vypocitej)
        vnejsi_rozlozeni.add_widget(tlacitko_rovnitko)

        return vnejsi_rozlozeni

    def _stisk_tlacitka(self, instance):

        #1. zhezcit - rozsekat na vic funkci nebo tak neco
        popisek_tlacitka = instance.text

        if self._posledni_tlacitko in self._operatory and popisek_tlacitka in self._operatory:
            symboly_displeje = list(self.displej.text)
            symboly_displeje[-1] = popisek_tlacitka
            self.displej.text = "".join(symboly_displeje)
        #2. defaultni text na displeji aby byl 0
        elif popisek_tlacitka == "C":
            self.displej.text = ""
        else:
            self.displej.text += popisek_tlacitka
        self._posledni_tlacitko = popisek_tlacitka

        nahodna_barva = [random() for _ in range(3)]
        nahodna_barva.append(1)
        instance.background_color = nahodna_barva

    def _vypocitej(self, instance):
        vyraz = self.displej.text
        if vyraz:
            vysledek = eval(vyraz)
            self.displej.text = str(vysledek)

if __name__ == "__main__":
    mobilni_appka = MobilniAplikace()
    mobilni_appka.run()