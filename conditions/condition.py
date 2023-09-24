from typing import Dict


class Condition:
    def is_passed(self, student: Dict[str, int]) -> bool:
        raise NotImplementedError("Subclasses must implement is_passed method")
