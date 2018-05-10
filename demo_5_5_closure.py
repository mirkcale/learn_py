#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def createCounter ():
    a = [0,]
    def fnc () :
        a[0] +=1
        return a[0]
    return fnc

#def createCounter():
#    i=0 
#    def counter():
#        nonlocal i 
#        i=i+1 
#        return i 
#    return counter

#test
if __name__ == '__main__':
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')
