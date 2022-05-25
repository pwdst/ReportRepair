from typing import List, Optional


def _get_exercise_lines() -> List[str]:
    # https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    with open("exercise_part_one_input.txt", 'r') as f:
        read_data = f.read()

    file_lines = read_data.split("\n")

    return file_lines


def _get_report_entries(input_lines: List[str]) -> List[int]:
    entries: List[int] = []

    for input_line in input_lines:
        try:
            int_value = int(input_line)

            entries.append(int_value)
        except ValueError:
            print(f"The input value {input_line} is not a valid integer")
            raise

    return entries


def _process_report_entries(entries: List[int]) -> Optional[int]:
    outer = 0

    # Iterate through all but the last entry in the list
    for left_entry in entries[:-1]:
        if left_entry > 2020:
            outer += 1
            continue

        # Compare the item with all other items to the right in the list
        for right_entry in entries[outer + 1:]:
            if right_entry > 2020:
                continue

            combined_entries = left_entry + right_entry

            if combined_entries == 2020:
                combined_entry_score = left_entry * right_entry

                return combined_entry_score

        outer += 1

    return None


if __name__ == '__main__':
    exercise_lines = _get_exercise_lines()

    report_entries = _get_report_entries(exercise_lines)

    entry_score = _process_report_entries(report_entries)

    if entry_score is None:
        print("No matching pairs found")
    else:
        print(f"Entry score: {entry_score}")
