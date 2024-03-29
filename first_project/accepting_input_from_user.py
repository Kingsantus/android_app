from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (360, 600)

class MainApp(App):
    def build(self):
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=40, spacing=10, padding=20)
        self.weight = TextInput(text='Enter weight here\n')  #self.weight to able to take use input
        self.height = TextInput(text='Enter height here\n')
        submit = Button(text='Submit', on_press=self.submit)
        layout.add_widget(self.weight)
        layout.add_widget(self.height)
        layout.add_widget(submit)
        return layout
    
    def submit(self, obj):
        print("weight: " + self.weight.text)
        print("height: " + self.height.text)

MainApp().run()