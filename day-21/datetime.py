'''
from datetime import date,time,datetime,timedelta
d=date(2004,8,4)
print(d)



'''
'''
from datetime import date,time,datetime,timedelta
d=date.today()
print(d)
print(d.day)
print(d.month)
print(d.year)
print(d.weekday())
print(d.isoweekday())
'''
'''
from datetime import date,time,datetime,timedelta
d=time(23,8,4)
print(d)

'''
'''
from datetime import date,time,datetime,timedelta
d=datetime.now()
print(d)
print(d.day)
print(d.month)
print(d.year)
print(d.weekday)
print(d.isoweekday())
print(d.hour)
print(d.minute)
print(d.second)
'''
'''
from datetime import date,time,datetime,timedelta
d=datetime.now()
print(d.strftime('%d/%m/%y'))
print(d.strftime('%d/%m/%Y %H:%M:%S'))
print(d.strftime('%d/%m/%Y %I:%H:%M:%S %p'))
print(d.strftime('%d/%b/%Y %I:%H:%M:%S %p'))
print(d.strftime('%d/%B/%Y %I:%H:%M:%S %p'))
print(d.strftime('%a,%d/%B/%Y %I:%H:%M:%S %p'))
print(d.strftime('%A,%d/%B/%Y %I:%H:%M:%S %p'))
'''
'''
from datetime import date,time,datetime,timedelta
d=datetime.now()
d7=d+timedelta(days=60)
print(d7)
m15=d+timedelta(minutes=15)
print(m15)
s15=d+timedelta(seconds=15)
print(s15)

'''
