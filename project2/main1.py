from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from screen_nav import screen_helper
from kivy.core.window import Window

Window.size = (300, 500)


class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
    
DemoApp().run()