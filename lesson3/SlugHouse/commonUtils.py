class CommonUtils:
    def __init__(self, slug_data):
        self.slug_list = slug_data[0]
        self.filename = slug_data[1]
        self.write_in_file()

    def write_in_file(self):
        file = open(self.filename, 'a')
        for slug in self.slug_list:
            file.write(slug+"\n")
        file.close()
        print("Имена сохранены")