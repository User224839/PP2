class time:
    def init(t1,hour,minute,second):
        t1.hour=hour
        t1.minute=minute
        t1.second=second
    def str(t1):
        return f"{t1.hour} : {t1.minute} : {t1.second}"
time1=[1,2,3]
print(time(time1))