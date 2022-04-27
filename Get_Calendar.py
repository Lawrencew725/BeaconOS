import time, calendar
import Messages_Declear as Messages_Declear
def get_calender():
    month_cal = int(time.strftime("%m", time.localtime()))
    year_cal = int(time.strftime("%Y", time.localtime()))
    cal = calendar.month(year_cal, month_cal)
    print(cal)