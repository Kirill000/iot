from transliterate import translit

class SlugConverter:
    def __init__(self):
        self.__file_name = str(input("Введите название файла для сохранения:"))
        self.__slug_list = []
        self.run()

    def run(self):
        print("Вводите ИО людей. Для завершения введите пустую строку")
        while 1:
            name = str(input())
            if name == "":
                break
            text = name.lower()
            text_lst = list(text)
            ed_txt = ""
            for el in text_lst:
                if el == " ":
                    ed_txt += "-"
                else:
                    ed_txt += el
            self.__slug_list.append(translit(ed_txt, language_code='ru', reversed=True))

    def data(self):
        return (self.__slug_list, self.__file_name)