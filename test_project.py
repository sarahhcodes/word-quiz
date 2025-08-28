import project
import pytest

def test_load_list(): # test that project successfully converts csv to list
    test_list = project.load_list("test_vocab.csv")

    assert test_list == [{'油 (abura)': '愛 (ai)', 'oil': 'love, affection, care'}, {'油 (abura)': '愛情 (aijou)', 'oil': 'love, affection'}, {'油 (abura)': '相変わらず (aikawarazu)', 'oil': 'as ever, as usual, the same'}, {'油 (abura)': '生憎 (ainiku)', 'oil': 'unfortunately; sorry, but…'}, {'油 (abura)': '愛する (aisuru)', 'oil': 'to love'}]


def test_invalid_file(): # test that project quits if file is too short
    with pytest.raises(SystemExit):
        test_list = project.load_list("test_vocab_short.csv")


def test_invalid_game():
    ...
    
def test_invalid_play(): 
    with pytest.raises(ValueError):
        project.play_again()