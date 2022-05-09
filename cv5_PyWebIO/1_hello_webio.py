from pywebio import *

#https://pywebio-demos.pywebio.online/

@config(theme="dark")
def main():  # PyWebIO application function
    name = input.input("what's your name")
    output.put_text("hello", name)

start_server(main, port=8000, debug=True)