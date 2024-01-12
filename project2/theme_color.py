from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'  # for the background
        self.theme_cls.primary_palette = 'Green' #for the displayed matterial
        self.theme_cls.primary_hue = 'A700'  #for the displayed matterial
        screen = Screen()
        icon_btn = MDFloatingActionButton(icon='android', pos_hint={'center_x':0.5, 'center_y':0.5})
        screen.add_widget(icon_btn)
        return screen
    
DemoApp().run()