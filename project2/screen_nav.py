screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'profile'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'upload'
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        on_press: root.manager.current = 'upload'

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome Kingsantus'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'back'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'
<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Uploaded completely'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'back'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

"""