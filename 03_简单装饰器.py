import time
import logging


def authorization(func):
    def wrapper(*args):
        print("新增的验证功能，需要等待2秒。。。。。。。")
        time.sleep(2)
        return func(*args)
    return wrapper


def warnning(func):
    def wrapper(a, b):
        logging.warning("这是一个警告！")
        time.sleep(2)
        return func(a, b)
    return wrapper


def largeBefore(func):
    def wrapper(a, b):
        logging.warning("此时需要把两数扩大十倍求和")
        a = a * 10
        b = b * 10
        return func(a, b)
    return wrapper


@authorization
def login():
    print("小海腾登陆成功！")


@authorization
@largeBefore
def cal_sum(a, b):
    return a + b


if __name__ == '__main__':
    re = cal_sum(3, 8)
    print(re)
    login()

