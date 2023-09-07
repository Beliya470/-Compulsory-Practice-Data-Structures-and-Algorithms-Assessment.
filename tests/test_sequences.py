# test_sequences.py

from sequences import remove_duplicates

def test_remove_duplicates():
    input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
    result = remove_duplicates(input_sequence)
    assert result == [2, 3, 4, 5, 6, 7]
