#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 14:41
# @Author  : 小海腾
import time
import logging


def authorization(level):
    def author(func):
        def wrapper(*args):
            if level == 1:
                logging.warning("新增的简单验证功能，需要等待2秒。。。。。。。")
                time.sleep(2)
            elif level == 2:
                logging.warning("新增的高级验证功能，需要等待5秒。。。。。。。")
                time.sleep(5)
            return func(*args)
        return wrapper
    return author


@authorization(level=1)
def cal_sum(a, b):
    c = 10 * a + b
    return c


if __name__ == '__main__':
    re = cal_sum(3, 4)
    print(re)
