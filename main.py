from match import Jiangsu
from icalendar import Calendar, Event
import pytz
import datetime

cal = Calendar()
for match in Jiangsu.match:
    e = Event()
    e.add('summary', match.i)
    e.add('dtstart', match.start)
    e.add('dtend', match.end)
    # e.add('etimezone')
    e.add('location', match.info)
    cal.add_component(e)

f = open('JiangSu Sunning.ics', 'wb')
f.write(cal.to_ical())
f.close()
print(pytz.all_timezones)

