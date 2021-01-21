# @Date    : 2021-01-15
# @Author  : 小海腾


# Python continue 语句跳出本次循环，而break跳出整个循环。
# continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。


# 我们想只打印0-10之间的奇数，可以用continue语句跳过某些循环：
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
