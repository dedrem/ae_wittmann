from dataclasses import dataclass
import pandas 
from datetime import datetime, time, timedelta


# csv
dataframe: pandas.DataFrame = pandas.read_csv('csv_data/flughafenkuerzel.csv', sep=';')
print(dataframe.values.tolist())

dataframe.columns = ['city', 'postal code', 'abrv.']
print(dataframe)


#dates
d1: datetime = datetime(year=2020, month=9, day=6)
print(d1.strftime("%d.%m.%Y"))

str1: str = "2020.09.17"
d2: datetime = datetime.strptime(str1, "%Y.%m.%d")
print(d2, isinstance(d2, datetime))


# shoptimes
@dataclass
class OpeningTimespan:
    time_open: time
    time_close: time
    def check_time(self, time_to_check: time) -> bool:
        if time_to_check >= self.time_open and time_to_check <= self.time_close:
            return True
        else: 
            return False

timespan1: OpeningTimespan = OpeningTimespan(time_open=time(hour=8), time_close=time(hour=12))
timespan2: OpeningTimespan = OpeningTimespan(time_open=time(hour=13), time_close=time(hour=18))
timespans: list[OpeningTimespan] = [timespan1, timespan2]

current_time: time = datetime.now().time()
print(current_time.strftime("%H:%M:%S"))

if True in [True for span in timespans if span.check_time(current_time)]:
    print("shop is open")
else:
    print("shop is closed")
    

# stempo
time_start: datetime = datetime(year=2020, month=9, day=7, hour=7, minute=55)
time_end: datetime = datetime(year=2020, month=9, day=7, hour=16, minute=47)
time_pause: timedelta = timedelta(hours=1)

working_time: timedelta = (time_end - time_start) - time_pause

print(f"Eingestempelt: {time_start} - Ausgestempelt: {time_end} - Arbeitszeit: {working_time}")

