# test_dictionaries.py

from dictionaries import word_frequency

def test_word_frequency():
    sentence = "This is a test sentence. This sentence is a test."
    result = word_frequency(sentence)
    assert result == {
        "this": 2,
        "is": 2,
        "a": 2,
        "test": 2,
        "sentence": 2,
    }
