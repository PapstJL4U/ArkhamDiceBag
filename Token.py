import re
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from os.path import join, dirname


class Token(Scatter):

    def __init__(self, art="-1", pos_hint={'top': 200, 'right': 200}):

        self.pos_hint = pos_hint
        self.art = str(art)
        self.dir = dirname(__file__)
        self.path = "images"
        self.image = None
        self.value = None
        self.arkhamInt = re.compile("(\+\-)*[0-9]+")

        if self.art == '+1':
            self.image = 'plusone.png'
            self.value = '+1'

        elif self.art == '0':
            self.image = 'zero.png'
            self.value = '0'

        elif self.art == '-1':
            self.image = 'minusone.png'
            self.value = '-1'

        elif self.art == '-2':
            self.image = 'minustwo.png'
            self.value = '-2'

        elif self.art == '-3':
            self.image = 'minusthree.png'
            self.value = '-3'

        elif self.art == '-4':
            self.image = 'minusfour.png'
            self.value = '-4'

        elif self.art == '-5':
            self.image = 'minusfive.png'
            self.value = '-5'

        elif self.art == '-6':
            self.image = 'minussix.png'
            self.value = '-6'

        elif self.art == '-7':
            self.image = 'minusseven.png'
            self.value = '-7'

        elif self.art == '-8':
            self.image = 'minuseight.png'
            self.value = '-8'

        elif self.art == 'akolyth':
            self.image = 'akolyth.png'
            self.value = 'Akolyth'

        elif self.art == 'skull':
            self.image = 'skull.png'
            self.value = 'Skull'

        elif self.art == 'elder':
            self.image = 'eldersign.png'
            self.value = 'Elder'

        elif self.art == 'gravestone':
            self.image = 'gravestone.png'
            self.value = 'Gravestone'

        elif self.art == 'tentacle':
            self.image = 'tentacle.png'
            self.value = 'Tentacle'

        elif self.art == 'monster':
            self.image = 'monster.png'
            self.value = 'Monster'

        self.scatter = Scatter(scale_min=0.5, scale_max=3.0)  # """, pos_hint=self.pos_hint"""
        self.scatter.size_hint = (None, None)
        self.scatter.auto_bring_to_front = True
        # print(self.dir, self.path, self.image)
        path = join(self.dir, self.path, self.image)
        img = Image(source=path)
        self.scatter.height = img.height
        self.scatter.width = img.width

        self.scatter.add_widget(img)

    def getValueAsStr(self):
        return self.value

    def getValueAsInt(self):
        if re.search(self.arkhamInt, self.value):
            return int(self.value)
        else:
            return -10

    def getImagePath(self):
        return join(self.dir, self.path, self.image)

    def getScatterImage(self):
        return self.scatter
