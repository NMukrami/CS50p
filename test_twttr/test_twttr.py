from twttr import shorten

def test_shorten():
    #uppercase
    assert shorten("TWITTER") == "TWTTR"
    #lowercase
    assert shorten("twitter") == "twttr"
    #number
    assert shorten("7") == "7"
    #punctuation
    assert shorten("!") == "!"