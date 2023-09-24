from conditions.condition import Condition


class ExamConditionBuilder:
    def __init__(self):
        self.conditions = []

    def add_condition(self, condition: Condition):
        self.conditions.append(condition)
        return self.conditions
