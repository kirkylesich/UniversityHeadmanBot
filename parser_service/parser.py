import json
from enum import Enum, auto
from dataclasses import dataclass
from requests import request
from utils import Timetable

class TimeTableExcelParser:
    
    def parse_to_json(self):
        pass 
    

class SheduleType(Enum):
    on_week = auto()
    on_semester = auto()
    on_date = auto()
    on_exam = auto()

@dataclass
class UsatuTimetableRequest:
    faculty: str
    study_class: int
    group: int
    shedule_type: SheduleType
    week: int
    date: str
    sem: int


class TimetableParser:

    def parse(self, request: UsatuTimetableRequest) -> Timetable:
        pass  

    def _get_csrf_token(self, page: str) -> str:
        pass

     
