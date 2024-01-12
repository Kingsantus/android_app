from kivy.app import App
from kivy.uix.image import Image, AsyncImage  #Image for image in local dir AsyncImage for downloadable image

class MainApp(App):
    def buld(self):
        #img = Image(source='cute.png')
        img = AsyncImage(source='https://w7.pngwing.com/pngs/636/531/png-transparent-frog-flower-cartoon-amphibian-animal-cute-kawaii-thumbnail.png')
        return img

MainApp().run()