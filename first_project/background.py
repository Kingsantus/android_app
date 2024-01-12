"""Background(windows) and text(label)"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window #used to change the background of the window

Window.clearcolor = (1,1,1,1) # changing the background to white color

class MainApp(App):
    def build(self):
        label = Label(text='I am Kingsantus', font_size='20sp', bold=True, italic=True, color=(0,0,0,1)) #sp is pixels in kivy
        return label

MainApp().run()
