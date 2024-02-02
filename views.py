from flask import Blueprint
import calendar

#setup
views = Blueprint("views")
calendar.setfirstweekday(6) #set sunday as the first day of thw week

@views.route("/")
def home():
    return "This is the home page :)"

@views.route("/caledner<year><>month>")
def getCalender(year:int, month:int):  #year:int -> the interger value of the year (exp: 2024). month:int -> the intiger representing the monthn (exp: febuary = 2).
    cal = calendar.monthcalendar(year, month)
    