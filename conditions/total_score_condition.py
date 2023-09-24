from typing import Dict

from conditions.condition import Condition


class TotalScoreCondition(Condition):
    def __init__(self, passing_score: int):
        self.passing_score = passing_score

    def is_passed(self, student: Dict[str, int]) -> bool:
        total_score = sum(student.values())
        return total_score >= self.passing_score
