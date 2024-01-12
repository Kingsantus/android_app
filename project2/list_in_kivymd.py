from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        scroll_view = ScrollView()
        list_view = MDList()
        scroll_view.add_widget(list_view)
        for i in range(20):
            items = ThreeLineListItem(text='Item ' + str(i), secondary_text='Hello World', tertiary_text='my text')
            list_view.add_widget(items)

        screen.add_widget(scroll_view)
        return screen
    
DemoApp().run()