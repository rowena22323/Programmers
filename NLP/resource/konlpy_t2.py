from konlpy.tag import Okt, Komoran, Hannanum, Kkma

def get_tokenizer(tokenizer_name):
    if tokenizer_name == "komoran":
        tokenizer = Komoran()
    elif tokenizer_name == "okt":
        tokenizer = Okt()
    elif tokenizer_name == "hannanum":
        tokenizer = Mecab()
    elif tokenizer_name == "kkma":
        tokenizer = Kkma()
    return tokenizer