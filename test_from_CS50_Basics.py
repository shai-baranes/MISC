import pytest
from from_CS50_Basics import get_int, get_int2




@pytest.mark.parametrize("input_value, expected", [
    # (" ", "out of the loop, value = "),
    (" ", "out of the loop, value =  "),
    ("4", 4),
    ("-4", -4),
    ("koko", 'out of the loop, value = koko'),
    ("test", 'out of the loop, value = test'),
])
def test_get_int(input_value, expected):
    assert get_int(value=input_value) == expected




# -----monkeypatch helps us testing as if getting real inpout fronm user wihout having to alter the tested function as one above


@pytest.mark.parametrize("input_value, expected", [
    ("5", 5),
    ("-3", -3),
    ("0", 0),
    # ("test", 'out of the loop, value = test'),
])
def test_get_int2_valid_inputs(input_value, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    assert get_int2() == expected




@pytest.mark.parametrize("input_value, expected", [
    (["abc", "10"], 10),
    (["foo", "bar", "7"], 7)
])
def test_get_int2_multiple_attemps(input_value, expected, monkeypatch, capsys):
    input_iter = iter(input_value)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))
    
    result = get_int2()
    captured = capsys.readouterr()
    
    assert result == expected
    assert "x is not an integer" in captured.out
