from typing import List

from subject_enum import Subject


class ExamineeInputReader:
    def read_input(self) -> List[List[str]]:
        # if a message should be displayed
        # n = int(input("Enter the number of examinees: "))
        n = int(input())
        input_data = []
        subjects = [subject.value for subject in Subject]

        for _ in range(n):
            # if a message should be displayed
            # line = input("Enter the scores for an examinee (e.g., Name 80 90 70 85 95): ").split()
            line = input().split()

            if len(line) != len(subjects) + 1:
                raise ValueError("Invalid input. Please provide scores for all subjects.")

            for subject, score in zip(subjects, map(int, line[1:])):
                if score > subject.score:
                    raise ValueError(f"Score for {subject} exceeds the limit of {subject.score}.")

            input_data.append(line)
        return input_data
