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


if __name__ == '__main__':
    s = Student()
    s.name = "xiaohaiteng"
    s.score = 99

    print(s.school)
    print(s.name)
    print(s.score)

