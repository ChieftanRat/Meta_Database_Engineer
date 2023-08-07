import pytest
import spellcheck

alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"

@pytest.fixture
def input_value():
    input = alpha
    return input

def test_length(input_value):
    words = input_value.split()
    assert len(words) < 10, "The string has more than 10 words"
    assert len(input_value) < 50

def test_struc(input_value):
    assert input_value[0].isupper(), "The string doesn't start with a capital letter"
    assert input_value.endswith(".")
