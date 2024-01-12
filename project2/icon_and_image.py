from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, ThreeLineListItem, ThreeLineIconListItem, ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        scroll_view = ScrollView()
        list_view = MDList()
        scroll_view.add_widget(list_view)
        for i in range(20):
            #icon = IconLeftWidget(icon="android")
            image = ImageLeftWidget(source='src/image/fb.png')
            items = ThreeLineIconListItem(text='Item ' + str(i), secondary_text='Hello World', tertiary_text='my text')
            #items.add_widget(icon)
            items.add_widget(image)
            list_view.add_widget(items)

        screen.add_widget(scroll_view)
        return screen
    
DemoApp().run()