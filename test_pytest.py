import pytest
import main


def test_numeric_string_values_converted_integer_values():
    input_values = ["200", "57", "1740", "1290"]
    expected_values = [200, 57, 1740, 1290]

    report_entries = main._get_report_entries(input_values)

    assert report_entries == expected_values


def test_non_numeric_string_values_raises_error():
    input_values = ["200", "57", "not_an_int", "1290"]

    with pytest.raises(ValueError):
        main._get_report_entries(input_values)


def test_does_not_match_against_same_value():
    # Theoretically the inner loop could add 1010 to itself,
    # so we want to make sure that doesn't happen
    input_values = [452, 686, 1010, 980]

    entity_score = main._process_report_entries(input_values)

    assert entity_score is None


def test_with_no_matching_values_returns_none():
    input_values = [842, 568, 324, 1812, 1944, 2100, 3000, 1712]

    entity_score = main._process_report_entries(input_values)

    assert entity_score is None


@pytest.mark.parametrize("expected,input_values", [
    (1020100, [452, 686, 1010, 980, 1010]),
    (889056, [1372, 648, 926, 205, 52]),
    (242176, [600, 112, 480, 300, 128, 1892])])
def test_with_matching_values_returns_expected(expected, input_values):
    entity_score = main._process_report_entries(input_values)

    assert expected == entity_score
