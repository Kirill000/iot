from transliterate import translit

text = str(input())
text = text.lower()
text_lst = list(text)
ed_txt = ""
for el in text_lst:
    if el == " ":
        ed_txt+="-"
    else:
        ed_txt+=el
print(translit(ed_txt, language_code='ru', reversed=True))