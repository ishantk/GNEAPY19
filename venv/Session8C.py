# import datetime
import datetime as dt

today = dt.datetime.today()
print("Today:",today)

tomorrow = dt.datetime(2019, 6, 25, 12, 12, 12, 200)
print("Tomorrow:",tomorrow)

howmany = tomorrow - today
print("How Many Days of Difference:",howmany)