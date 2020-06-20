#!/usr/bin/python3
# -*- coding:utf-8 -*-

def triangles1(n):
    a=[1]
    print('1'.center(90))
    while len(a)<=n:
        ar = [0] + a + [0]
        a = [ar[x-1] + ar[x] for x in range(1,len(ar))]
        print('   '.join(map(str,a)).center(90))

triangles1(8)


def triangles2(n):
    a=[1]
    print('1'.center(90))
    while len(a)<=n:
        a = [sum(x) for x in zip([0] + a, a + [0])]
        print('   '.join(map(str,a)).center(90))

triangles2(9)