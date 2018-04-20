#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from random import randint
from math import ceil, sqrt
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.graphics.transformation import Matrix
import Bag

_maxcoins = 20

class CustomDropDown(DropDown):
    pass
class NewBag(Popup):
    pass

class DiceBagApp(App):

    def build(self):
        root = self.root
        self.title = "Dicebag"
        self.shownCoins = []
        self.myBag = Bag.Bag(difficulty="normal")
        btDraw = self.root.ids.btDraw
        btChange = self.root.ids.btChange
        btShow = self.root.ids.btContent
        dropdown = CustomDropDown()
        popup = NewBag()
        btPopup = dropdown.ids.btPopup

        btDraw.bind(on_press=self.drawCoin)
        btChange.bind(on_release=dropdown.open)
        btShow.bind(on_press=self.showBag)
        btPopup.bind(on_release=popup.open)
        dropdown.bind(on_select=lambda instance, x: self.changeBag(instance, x))


    def on_pause(self):
        return True

    def drawCoin(self, instance):
        if self.myBag.bagSize() is None or self.myBag.bagSize()==0:
            return "Bag is empty"
        self.clearCoins()
        coin = self.myBag.drawCoin()
        coin.getScatterImage().pos = (0,0)
        x, y = self.getRndXY()
        mat = Matrix().translate(x, y, 0)
        coin.getScatterImage().apply_transform(mat)

        self.root.add_widget(coin.getScatterImage())
        self.shownCoins.append(coin)
        return "Coin drawn."

    def showBag(self, instance):
        self.clearCoins()
        width, height= self.root.size
        for coin in self.myBag.getBag():
            coin.getScatterImage().pos = (0,0)
            x, y = self.getRndXY()
            mat = Matrix().translate(x, y, 0)
            coin.getScatterImage().apply_transform(mat)
            self.root.add_widget(coin.getScatterImage())
            self.shownCoins.append(coin)

    def changeBag(self, instance, value):

        if value == "1":
            value = "+1"
            self.myBag.addCoin(coin=value)
        if value == "Clear":
            self.clearBag()

        else:
            #print(value)
            self.myBag.addCoin(coin=value)

    def clearCoins(self):
        for coin in self.shownCoins:
            #print(coin.getValueAsStr())
            coin.getScatterImage().pos = (0,0)
            self.root.remove_widget(coin.getScatterImage())

    def clearBag(self):
        self.clearCoins()
        clist = []
        for coin in self.myBag.getBag():
            #print(coin.getValueAsStr())
            #self.myBag.removeCoin(coin=coin)
            clist.append(coin.getValueAsStr())
        for item in clist:
            self.myBag.removeCoin(coin=item)

        #print(self.myBag.getBag())
        self.shownCoins = []

    def getRndXY(self):
        bnd = 100
        width, height = self.root.size
        x = randint(bnd, width-bnd)
        y = randint(bnd, height-bnd)
        return x, y

    def makeNewBag(self, instance):
        self.myBag = Bag.Bag(difficulty=instance)

if __name__ == '__main__':
    DiceBagApp().run()
