from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Account(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/account.kv")
        super().__init__(**kw)
