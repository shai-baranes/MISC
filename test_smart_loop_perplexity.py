import pytest
from smart_loop_pytest_testable import get_int

# Test valid inputs
@pytest.mark.parametrize("input_value, expected", [
    ("5", 5),
    ("-3", -3),
    ("0", 0)
])
def test_valid_inputs(input_value, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    assert get_int() == expected

# Test invalid -> valid sequences
@pytest.mark.parametrize("inputs, expected", [
    (["abc", "10"], 10),
    (["foo", "bar", "7"], 7)
])
def test_invalid_then_valid(inputs, expected, monkeypatch, capsys):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))
    
    result = get_int()
    captured = capsys.readouterr()
    
    assert result == expected
    assert "x is not an integer" in captured.out

# Edge case test
def test_empty_then_valid(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "\n")  # Simulate Enter key
    input_iter = iter(["\n", "8"])  # First empty, then valid
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))
    
    assert get_int() == 8
    captured = capsys.readouterr()
    assert "x is not an integer" in captured.out
