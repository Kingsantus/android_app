"""Button (Button)"""
from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        button = Button(text="Print this", size_hint=(0.15, 0.05), font_size='20sp', pos_hint={'center_x':0.5, 'center_y':0.3}, on_press=self.printpress,on_release=self.printrelease) #size_hint to resize the button the param (x,y) x for horixontal width y for vertical height x (0.5 is 50%)
        return button
    
    def printpress(self, obj): #the parameter obj is very important
        print("Button has been pressed")

    def printrelease(self, obj):
        print("Button has been released")

MainApp().run()