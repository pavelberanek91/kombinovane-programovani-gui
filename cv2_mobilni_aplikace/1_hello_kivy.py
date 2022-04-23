#!python3 -m pip install kivy

from kivy.app import App
from kivy.uix.label import Label

class MobilniAplikace(App):
    def build(self):
        text = Label(
            text='Hello Kivy',
            size_hint=(.5, .5),
            pos_hint={
                'center_x': .5, 
                'center_y': .5}
            )

        return text

if __name__ == '__main__':
    app = MobilniAplikace()
    app.run()