def make_average0():
    series = [] #这是没有被初始化的，所以不会被当作局部变量。当作自由变量。

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager

def make_average1():
    count = 0 #初始化了就被当作局部变量，作用域在局部。
    total = 0

    def averager(new_value):
        nonlocal count, total #不是本地局部变量也不是全部变量，那就是闭包变量了咯。
        count += 1
        total += new_value
        return total / count

    return averager

avg = make_average1()
print(avg(10))
print(avg(20))
print(avg(30))
print(avg(40))