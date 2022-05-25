import unittest
import main


class ReadingExerciseValues(unittest.TestCase):
    def test_numeric_values_successfully_parsed_returned(self):
        input_values = ["200", "57", "1740", "1290"]

        report_entries = main.get_report_entries(input_values)

        self.assertIsNotNone(report_entries)

        self.assertEqual(4, len(report_entries))

        expected_values = [200, 57, 1740, 1290]

        self.assertListEqual(expected_values, report_entries)

    def test_non_numeric_values_raises_error(self):
        input_values = ["200", "57", "not_an_int", "1290"]

        with self.assertRaises(ValueError):
            main.get_report_entries(input_values)


class ProcessingExerciseValues(unittest.TestCase):
    def test_does_not_match_against_same_value(self):
        # Theoretically the inner loop could add 1010 to itself,
        # so we want to make sure that doesn't happen
        input_values = [452, 686, 1010, 980]

        entity_score = main.process_report_entries(input_values)

        self.assertIsNone(entity_score)

    def test_with_no_matching_values_returns_none(self):
        input_values = [842, 568, 324, 1812, 1944, 2100, 3000, 1712]

        entity_score = main.process_report_entries(input_values)

        self.assertIsNone(entity_score)

    def test_with_matching_values_returns_expected(self):
        test_case_values = {
            1020100: [452, 686, 1010, 980, 1010],
            889056: [1372, 648, 926, 205, 52],
            242176: [600, 112, 480, 300, 128, 1892]
        }

        # todo Is there a better way to do this?
        for expected, test_case_input in test_case_values.items():
            with self.subTest(test_case_input):

                entity_score = main.process_report_entries(test_case_input)

                self.assertIsNotNone(entity_score)

                self.assertEqual(expected, entity_score)


if __name__ == '__main__':
    unittest.main()
