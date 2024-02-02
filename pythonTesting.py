from flask import Blueprint
import calendar

calendar.setfirstweekday(6) #0 = monday, 6 = sunday
print(type(calendar.monthcalendar()))