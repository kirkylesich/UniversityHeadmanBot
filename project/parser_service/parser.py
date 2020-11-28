import json
from enum import Enum, auto
from dataclasses import dataclass
import requests
from utils import Timetable
from typing import Dict
from bs4 import BeautifulSoup


class TimeTableExcelParser:
    def parse_to_json(self):
        pass


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


