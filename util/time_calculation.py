import datetime

dt_now = datetime.datetime.now()
print(dt_now)

time_str = '12:30:30'
time_dt = datetime.datetime.strptime(time_str, '%H:%M:%S')
print(time_dt)

print(type(time_dt))

print("###############")

## time calc sample
td_30_m = datetime.timedelta(minutes=30)

time_str = '23:30:30'
time_dt = datetime.datetime.strptime(time_str, '%H:%M:%S')

time_dt_new = time_dt + td_30_m

print(time_dt_new)
print(time_dt_new.strftime('%H:%M:%S'))

print(time_dt < time_dt_new)
print(time_str < time_dt_new.strftime('%H:%M:%S'))

time_dt_new = time_dt_new - td_30_m

print(time_dt_new)
print(time_dt_new.strftime('%H:%M:%S'))

print(time_dt == time_dt_new)

print('12:30:30' < '23:30:30')
print('12:30:30' < '24:30:30')
print('12:30:30' < '24:00:30')