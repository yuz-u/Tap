from typing import Dict

from conditions.condition import Condition
from subject_enum import Subject


class ScienceScoreCondition(Condition):
    def __init__(self, passing_score: int):
        self.passing_score = passing_score

    def is_passed(self, student: Dict[str, int]) -> bool:
        science_score = student[Subject.MATH.name] + student[Subject.SCIENCE.name]
        return science_score >= self.passing_score
