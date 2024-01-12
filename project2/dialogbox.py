from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import username_helper

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette= 'Green'
        btn = MDRectangleFlatButton(text='Submit', pos_hint={'center_x':0.5, 'center_y':0.4}, size_hint_x=None,width=300, on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(btn)
        return screen
    
    def show_data(self,obj):
        if self.username.text is "":
            check_string = 'Please enter a username'
        else:
            check_string = self.username.text + ' does not exist'
        close_btn = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_btn = MDFlatButton(text='More')
        self.dialog = MDDialog(title='Username Check',text=check_string, size_hint=(0.7, 1), buttons=[close_btn, more_btn])
        self.dialog.open()
        #print(self.username.text) to print on the console

    def close_dialog(self, obj):
        self.dialog.dismiss()
    
DemoApp().run()