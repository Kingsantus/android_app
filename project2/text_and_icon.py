from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon

class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text='Hello Emeka', halign='center', theme_text_color='Custom', text_color='#7f6700', font_style='Caption')
        icon_label = MDIcon(icon='library-video', halign='center')
        return icon_label
    
DemoApp().run()