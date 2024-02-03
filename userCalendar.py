import calendar

class uCalender:
    def __init__(self) -> None:
        pass
    def generateMonth(self, year:int, month:int):
        return calendar.monthcalendar(year, month)