import sys
import os

# add developer folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../developer")))

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from char_utils import most_frequent_repeating_char

def test_with_repeats():
    repeats, most_frequent = most_frequent_repeating_char("Arun Kumaru")
    assert repeats == {'a': 2, 'r': 2, 'u': 3}
    assert most_frequent == ('u', 3)

def test_no_repeats():
    repeats, most_frequent = most_frequent_repeating_char("abc")
    assert repeats == {}
    assert most_frequent is None

def test_case_insensitive():
    repeats, most_frequent = most_frequent_repeating_char("AaBbCc")
    assert repeats == {'a': 2, 'b': 2, 'c': 2}
    assert most_frequent[1] == 2

def test_empty():
    repeats, most_frequent = most_frequent_repeating_char("")
    assert repeats == {}
    assert most_frequent is None
