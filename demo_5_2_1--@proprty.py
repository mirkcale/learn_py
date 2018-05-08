#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Screen:
    @property
    def width (self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def heigth (self):
        return self._height

    @heigth.setter
    def heigth(self, value):
        self._height = value

    @property
    def resolution(self):
        return 786432
# test
if __name__ == '__main__':
    s = Screen()
    s.width = 102
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')