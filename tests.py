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


if __name__ == '__main__':
    unittest.main()
