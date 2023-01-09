from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Music(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/music.kv")
        super().__init__(**kw)
