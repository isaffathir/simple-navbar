from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Search(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/search.kv")
        super().__init__(**kw)
