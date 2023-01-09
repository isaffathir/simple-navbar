from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.screenmanager import ScreenManager
from .account import Account
from .music import Music
from .search import Search

class Account_scr(Account):
    name = "account"

class Search_scr(Search):
    name = "search"

class Music_scr(Music):
    name = "music"

class MyNavbar(CommonElevationBehavior,MDFloatLayout):
    pass

class MyScreen(ScreenManager):
    pass

class Home(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/home.kv")
        super().__init__(**kw)
        #temp data
        self.btn1 = 0
        self.btn2 = 0
        self.btn3 = 0

    def search_btn(self):
        if self.btn1 == 0:
            self.ids.myscr.add_widget(Search_scr())
            self.btn1 += 1
        else:
            pass

    def music_btn(self):
        if self.btn2 == 0:
            self.ids.myscr.add_widget(Music_scr())
            self.btn2 += 1
        else:
            pass

    def account_btn(self):
        if self.btn3 == 0:
            self.ids.myscr.add_widget(Account_scr())
            self.btn3 += 1
        else:
            pass

    def navbar_click(self,instance):
        if instance in self.ids.values():
            current_id = list(self.ids.keys())[list(self.ids.values()).index(instance)]
            for i in range(4):
                if f"btn{i+1}" == current_id:
                    self.ids[f"btn{i+1}"].text_color = 1,0,0,1
                else:
                    self.ids[f"btn{i+1}"].text_color = 0,0,0,1
