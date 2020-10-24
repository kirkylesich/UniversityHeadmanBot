from dataclasses import dataclass
from typing import List


@dataclass
class TimetableObject:
    time: str
    name: str
    class_order: int


@dataclass
class StudyDay:
    objects: List[TimetableObject] 
    
    @property
    def objects_count(self) -> int:
        return len(self.objects)


@dataclass
class Timetable:
    week: int
    timatable_days: List[StudyDay]
