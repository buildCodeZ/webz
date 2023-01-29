#coding=utf-8
import sys
import os

# 下面三行代码可以删除
from . import __path__
webpath = os.path.dirname(os.path.dirname(os.path.dirname(__path__[0])))
sys.path.append(webpath)
# 上面三行代码可以删除


import webz
class Test(webz.Base):
    def deal(self):
        self.output.set("url", self.input.url)
        self.output.set("action", self.input.type)
        self.output.update(self.input.get())

pass


from webz import configz

def run(fps):
    configz.run(fps)

pass
