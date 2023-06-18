from datetime import date, timedelta
import requests


class Student:
    """ A student class as base for method testing"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False
        self.extended = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True

    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    @property
    def start_date(self):
        return self._start_date

    def apply_extension(self, plusdays):
        self.end_date = self.end_date + timedelta(days=plusdays)
        d1 = date(self.end_date)
        d2 = date(self._start_date)
        if (d1 - d2) > 365:
            self.extended = True

    def course_schedule(self):
        response = requests.get(f"http://company.com/course-schedule/{self._first_name}/{self._last_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"
