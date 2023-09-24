from collections import namedtuple
from enum import Enum

SubjectInfo = namedtuple("SubjectInfo", ["value", "score"])


class Subject(Enum):
    ENGLISH = SubjectInfo(1, 100)
    MATH = SubjectInfo(2, 100)
    SCIENCE = SubjectInfo(3, 100)
    JAPANESE = SubjectInfo(4, 100)
    GEOHIST = SubjectInfo(5, 100)
