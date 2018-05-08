#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def product(*z):
    if(z.__len__() == 0):
        raise RuntimeError('error')
        
    products = 1

    for num in z:
        products *= num

    return products

# 测试
if __name__ == '__main__':
    print('product(5) =', product(5))
    print('product(5, 6) =', product(5, 6))
    print('product(5, 6, 7) =', product(5, 6, 7))
    print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
    if product(5) != 5:
        print('测试失败!')
    elif product(5, 6) != 30:
        print('测试失败!')
    elif product(5, 6, 7) != 210:
        print('测试失败!')
    elif product(5, 6, 7, 9) != 1890:
        print('测试失败!')
    else:
        try:
            product()
            print('测试失败!')
        except RuntimeError:
            print('测试成功!')
