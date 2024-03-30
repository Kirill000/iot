import csv

def load_csv_file(filepath):
    # Загрузка csv
    if filepath != "":
        data = []
        x_coords = []
        z_coords = []
        r_values = []

        with open(filepath, encoding='utf-8') as r_file:
            # Создаем объект reader, указываем символ-разделитель ","
            file_reader = csv.reader(r_file, delimiter=",")
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            # Считывание данных из CSV файла
            for row in file_reader:
                if count == 0:
                    # Проверка количества и содержания столбцов
                    if len(row) != 3:
                        # ErrorWindow(self, config.errorTextImport)
                        break
                else:
                    l = [] 
                    for num in row:
                        l.append(num)
                    data.append(l)
                    for a in range(len(l)):
                        if a % 3 == 0:
                            x_coords.append(float(l[a]))
                        elif a % 3 == 1:
                            z_coords.append(float(l[a]))
                        else:
                            r_values.append(float(l[a]))
                count += 1
            return x_coords, z_coords, r_values
# print(load_csv_file("1\data\points.csv"))