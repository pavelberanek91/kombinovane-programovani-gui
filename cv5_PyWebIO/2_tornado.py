#python3 -m pip install pywebio

from pywebio import start_server, config
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_html

#python3 -m pip install tornado

import tornado.ioloop
import tornado.web
from pywebio.platform.tornado import webio_handler

@config(theme="sketchy")
def bmi():
    height = input("Your Height(cm): ", type=FLOAT)
    weight = input("Your Weight(kg): ", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(14.9, 'Severely underweight'), (18.4, 'Underweight'),
                  (22.9, 'Normal'), (27.5, 'Overweight'),
                  (40.0, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_text('Your BMI: %.1f, category: %s' % (BMI, status))
            break

def cute_plots():

    #cute: https://github.com/cutecharts/cutecharts.py 
    #bohatejsi: https://pywebio-charts.pywebio.online/?app=pyecharts

    #python3 -m pip install cutecharts
    from cutecharts.charts import Line

    chart = Line("Line chart")
    chart.set_options(
        labels=["Pondeli", "Utery", "Streda", "Ctvrtek", "Patek", "Sobota", "Nedele"], 
        x_label="den", 
        y_label="nalada",
    )
    chart.add_series("Petr", [57, 134, 137, 129, 145, 60, 49])
    chart.add_series("Jana", [114, 55, 27, 101, 125, 27, 105])
    chart.render()
    put_html(chart.render_notebook())

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/bmi", webio_handler(bmi)),
        (r"/cuteplots", webio_handler(cute_plots)),
    ])
    application.listen(port=8000, address='localhost')
    tornado.ioloop.IOLoop.current().start()