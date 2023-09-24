from examinee_builder import ExamineeBuilder
from conditions.exam_condition_builder import ExamConditionBuilder
from examinee_input_reader import ExamineeInputReader
from conditions.total_score_condition import TotalScoreCondition
from conditions.science_score_condition import ScienceScoreCondition
from conditions.humanity_score_condition import HumanityScoreCondition
from exam_result_processor import ExamResultProcessor


def main():
    # Reads the input
    examinee_input_reader = ExamineeInputReader()
    input_data = examinee_input_reader.read_input()

    # Builds a list of examinees(classification, scores) based on the input
    examinee_builder = ExamineeBuilder()
    examinees = examinee_builder.build(input_data)

    # Builds a list of tuples(conditions, examinees)
    exam_condition_builder = ExamConditionBuilder()
    conditions_examinees = []
    for examinee in examinees:
        conditions = exam_condition_builder.add_condition(TotalScoreCondition(350))
        if 's' in examinee[0]:
            conditions = exam_condition_builder.add_condition(ScienceScoreCondition(160))
        if 'l' in examinee[0]:
            conditions = exam_condition_builder.add_condition(HumanityScoreCondition(160))
        conditions_examinees.append((conditions.copy(), examinee))
        conditions.clear()
    # Processes the list of tuples to calculate the number of successful examinees
    exam_result_processor = ExamResultProcessor(conditions_examinees)
    passed_students = exam_result_processor.count_passed_students()

    print(passed_students, end="\n")


if __name__ == "__main__":
    main()
