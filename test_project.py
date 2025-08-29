import project
import pytest

def test_load_csv(): # test that project successfully converts csv to list
    test_list = project.load_from_csv("csv/test_vocab.csv")

    assert test_list == [{'Japanese': '油 (abura)', 'English': 'oil'}, {'Japanese': '愛 (ai)', 'English': 'love, affection, care'}, {'Japanese': '愛情 (aijou)', 'English': 'love, affection'}, {'Japanese': '相変わらず (aikawarazu)', 'English': 'as ever, as usual, the same'}, {'Japanese': '生憎 (ainiku)', 'English': 'unfortunately; sorry, but…'}]


def test_load_txt(): # test that project successfully converts txt to list
    columns = ["Japanese", "English"]
    test_list = project.load_from_txt("txt/test_vocab.txt", columns, ':')

    assert test_list == [{'Japanese': '油 (abura)', 'English': 'oil'}, {'Japanese': '愛 (ai)', 'English': 'love, affection, care'}, {'Japanese': '愛情 (aijou)', 'English': 'love, affection'}, {'Japanese': '相変わらず (aikawarazu)', 'English': 'as ever, as usual, the same'}, {'Japanese': '生憎 (ainiku)', 'English': 'unfortunately; sorry, but…'}]


def test_invalid_file(): # test that project quits if file is too short
    with pytest.raises(SystemExit):
        test_list = project.load_from_csv("csv/test_vocab_short.csv")