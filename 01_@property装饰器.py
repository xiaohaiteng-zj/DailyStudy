# @Date    : 2021-01-15
# @Author  : 小海腾
# 学习链接：https://www.liaoxuefeng.com/wiki/1016959663602400/1017502538658208


# Python内置的@property装饰器就是负责把一个方法变成属性调用的
# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
# 于是，我们就拥有一个可控的属性操作
class Student(object):
    school = "华东师范大学"
    name = ''
    _score = 100
    _total_short_stock_by_truck = False

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("分数必须是整数")
        if value < 0 or value > 100:
            raise ValueError("分数必须在0-100之间")
        self._score = value

    @property
    def total_short_stock_by_truck_(self):
        """SKU-各仓的汽运总缺货量"""
        if not self._total_short_stock_by_truck:
            self._total_short_stock_by_truck = 10000

        return self._total_short_stock_by_truck

    @total_short_stock_by_truck_.setter
    def total_short_stock_by_truck_(self, value):
        self._total_short_stock_by_truck -= value


if __name__ == '__main__':
    s = Student()
    s.name = "xiaohaiteng"
    s.score = 99

    print(s.school)
    print(s.name)
    print(s.score)
    print(s.total_short_stock_by_truck_)
    s._total_short_stock_by_truck_ = 300
    print(s.total_short_stock_by_truck_)

