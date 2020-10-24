import json
from enum import Enum, auto
from dataclasses import dataclass
import requests
from utils import Timetable
from typing import Dict
from bs4 import BeautifulSoup

import pandas as pd
from utils import TimetableObject
from utils import StudyDay
from utils import Timetable

class TimeTableExcelParser:
    def parse_to_json(self):
        pass

    def convert_to_dataclass(self, path):
        table = pd.ExcelFile(path)
        df1 = table.parse(table.sheet_names)
        inp = df1.get('Raspisanie').values.tolist()

        num = get_number_week(inp[0][0])

        time_start, time_finish = get_time(inp)

        weeks = get_weeks(inp)

        week_info = get_week_info(inp, time_start, time_finish, weeks)

        Upper = Timetable(week=num, timatable_days=week_info)
        return Upper

    def get_week_info(self, inp, time_start, time_finish, weeks):
        week_info = []
        for i in range(0, 6):
            day_info = []
            for el in range(0, 7):
                element = TimetableObject(time_start=time_start[el], time_finish=time_finish[el], name=weeks[i][el],
                                          class_order=el)
                day_info.append(element)
            k = StudyDay(day_info)
            week_info.append(k)
        return week_info

    def get_weeks(self, inp):
        weeks = []
        for day in range(1, 7):
            name = []
            class_order = []
            for line in range(3, 10):
                if inp[line][day] != 'nan':
                    stringf = clear_stringf(str(inp[line][day]))
                    name.append(stringf[1:])
            weeks.append(name)
        return weeks

    def get_time(self, inp):
        time_start = []
        time_finish = []
        for i in range(0, 1):
            for st in range(3, 10):
                ll = inp[st][i][7:]
                index = int(str.find(ll, ' ', ))
                time_start.append(ll[1:index])
                time_finish.append(ll[index + 3:])
        return time_start, time_finish

    def get_number_week(self, f_st):
        w = f_st[14:16]
        if w[1] == ' ':
            num = int(w[0])
        else:
            num = int(w[0]) * 10 + int(w[1])
        return num

    def clear_stringf(self, s):
        for i in range(0, len(s)):
            if s[i] == '\n':
                s = s[0:i] + ' ' + s[i + 1:];
        return s


class SheduleType(Enum):
    on_week = "За неделю"
    on_semester = "За семестр"
    on_date = "На дату"
    on_exam = "Экзамены"


@dataclass
class UsatuTimetableRequest:
    csrfmiddlewaretoken: str
    faculty: str
    study_class: int
    group: int
    shedule_type: SheduleType
    week: int
    date: str
    sem: int

    def to_dict(self) -> Dict:
        return {
            "csrfmiddlewaretoken": self.csrfmiddlewaretoken,
            "faculty": self.faculty,
            "klass": self.study_class,
            "group": self.group,
            "ScheduleType": self.shedule_type,
            "week": self.week,
            "date": self.date,
            "sem": self.sem,
            "viewEXCEL.x": 6,
            "viewEXCEL.y": 10,
        }


class TimetableParser:
    def parse(self, request: UsatuTimetableRequest) -> Timetable:
        pass

    def make_request(self):
        pass

    def create_timetable_request(
        self,
        faculty: str,
        group: int,
        date: str,
        week: int,
        sem: int,
        shedule_type: SheduleType,
        study_class: int = 1,
    ) -> UsatuTimetableRequest:

        url = "https://lk.ugatu.su/raspisanie/"
        csrf_token = self._get_csrf_token(requests.get(url).text)

        timetable_request = UsatuTimetableRequest(
            csrfmiddlewaretoken=csrf_token,
            faculty=faculty,
            study_class=study_class,
            group=group,
            date=date,
            week=week,
            sem=sem,
            shedule_type=shedule_type
        )
        return timetable_request

    def _get_csrf_token(self, page: str) -> str:
        _page = BeautifulSoup(page, "html.parser")
        input_tag = str(
            _page.find("input", attrs={"name": "csrfmiddlewaretoken", "type": "hidden"})
        ).split("\n")[0]
        token = input_tag.split("value=")[1].replace('"', "").replace(">", "")
        return token


