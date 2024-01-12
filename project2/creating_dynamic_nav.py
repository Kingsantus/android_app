from kivymd.app import MDApp
from kivy.lang import Builder

from kivy.core.window import Window

Window.size = (300, 500)

screen_helper = """
Screen:
    ScreenManager:
        Screen:
            BoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: 'Android App'
                    left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                Widget:
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            spacing: '8dp'
            padding: '8dp'
            Image:
                source: 'src/image/fb.png'
            MDLabel:
                text: 'Attreya'
                font_style: 'Subtitle1'
                size_height_y: None
                height: self.texture_size[1]
            MDLabel:
                text: '   Attreya'
                font_style: 'Caption'
                size_height_y: None
                height: self.texture_size[1]
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: 'Profile'
                        IconLeftWidget:
                            icon: 'android'
                    OneLineIconListItem:
                        text: 'Upload'
                        IconLeftWidget:
                            icon: 'file-upload'
                    OneLineIconListItem:
                        text: 'Logout'
                        IconLeftWidget:
                            icon: 'logout'
"""

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
    
    
DemoApp().run()