import pytest
from match_case import is_weekend






@pytest.mark.parametrize("day, result", [
	("Sunday", False),
	("sunday", False),
	("SUNDAY", False),
	("Monday", False),
	("monday", False),
	("Tuesday", False),
	("tuesday", False),
	("Wednesday", False),
	("wednesday", False),
	("Thursday", False),
	("thursday", False),
	("Friday", True),
	("friday", True),
	("Saturday", True),
	("saturday", True),
	("koko", False),
])
def test_is_day_match_weekend(day, result):
	assert is_weekend(day) == result




