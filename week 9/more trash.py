class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0):
         self.hours = hrs
         self.minutes = mins
         self.seconds = secs

def add_time(t1, t2):
    h = t1.hours + t2.hours
    m = t1.minutes + t2.minutes
    s = t1.seconds + t2.seconds
    sum_t = MyTime(h, m, s)
    return sum_t

current_time = MyTime(9, 14, 30)
bread_time = MyTime(3, 35, 0)
done_time = add_time(current_time, bread_time)
print(done_time)


def multadd(x, y, z):
    return x * y + z