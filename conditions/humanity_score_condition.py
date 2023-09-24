from typing import Dict

from conditions.condition import Condition
from subject_enum import Subject


class HumanityScoreCondition(Condition):
    def __init__(self, passing_score: int):
        self.passing_score = passing_score

    def is_passed(self, student: Dict[str, int]) -> bool:
        humanity_score = student[Subject.JAPANESE.name] + student[Subject.GEOHIST.name]
        return humanity_score >= self.passing_score
