from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.toolbar import MDBottomAppBar

Window.size = (300, 600)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Android App'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["clock", lambda x: app.navigation_draw()]]
        MDLabel:
            text: 'Learning Android App with Python'
            halign: 'center'

        MDBottomAppBar:
            left_action_items: [["coffee", lambda x: app.navigation_draw()]]
            mode: 'free-end'
            type: 'bottom'
            icon: 'language-python'
            
"""

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        screen = Builder.load_string(screen_helper)
        return screen
    
    def navigation_draw(self):
        print("Navigation")
    
DemoApp().run()