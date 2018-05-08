#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def trim (s):
    if len(s) == 0:
        return s
    if s[:1] == ' ':
        s = s[1:]
    elif s[-1:] == ' ':
        s = s[:-1]
    if s[:1] == ' ' or s[-1:] == ' ':
        return trim(s)
    else:
        return s

# good example
    # while s[:1] == ' ':
    #     s = s[1:]
    # while s[-1:] == ' ':
    #     s = s[:-1]
    # return s

# 测试:
if __name__ == '__main__':
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')