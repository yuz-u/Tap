from typing import List, Tuple, Dict

from conditions.condition import Condition


class ExamResultProcessor:
    def __init__(self, conditions_examinees: List[Tuple[List[Condition], Tuple[str, Dict[str, int]]]]):
        self.conditions_examinees = conditions_examinees

    def count_passed_students(self) -> int:
        passed_students = 0
        for condition_examinee in self.conditions_examinees:
            dictionary = condition_examinee[1][1]
            is_passed = all(condition.is_passed(dictionary) for condition in condition_examinee[0])
            if is_passed:
                passed_students += 1

        return passed_students
