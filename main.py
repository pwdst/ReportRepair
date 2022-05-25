from typing import List


def get_exercise_lines() -> List[str]:
    # https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    with open("exercise_part_one_input.txt", 'r') as f:
        read_data = f.read()

    file_lines = read_data.split("\n")

    return file_lines


def get_report_entries(input_lines: List[str]) -> List[int]:
    report_entries: List[int] = []

    for input_line in input_lines:
        try:
            int_value = int(input_line)

            report_entries.append(int_value)
        except ValueError:
            print(f"The input value {input_line} is not a valid integer")
            raise

    return report_entries


if __name__ == '__main__':
    exercise_lines = get_exercise_lines()
