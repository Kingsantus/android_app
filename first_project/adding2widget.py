from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
Window.size = (360, 600)

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40) #orientation used to change the direction of the button
        btn = Button(text="Click Here")
        btn1 = Button(text="Click me Here")
        btn2 = Button(text=" me Here")
        layout.add_widget(btn)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        return layout

MainApp().run()