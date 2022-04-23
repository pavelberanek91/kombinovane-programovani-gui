from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

class MobilniAplikace(App):
    def build(self):
        img = Image(source='ujep.png',
                    size_hint=(1, .5),
                    pos_hint={
                        'center_x':.5, 
                        'center_y':.5
                    })
        return img


if __name__ == '__main__':
    app = MobilniAplikace()
    app.run()