from typing import List, Tuple, Dict

from subject_enum import Subject


class ExamineeBuilder:
    def build(self, input_data: List[List[str]]) -> List[Tuple[str, Dict[str, int]]]:
        students = []
        subjects = [subject.name for subject in Subject]
        for line in input_data:
            scores = {subject: int(score) for subject, score in zip(subjects, line[1:])}
            student = (line[0], scores)
            students.append(student)

        return students
