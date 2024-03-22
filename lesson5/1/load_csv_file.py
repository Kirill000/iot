import csv

class CSVLoader:
    @staticmethod
    def load_points_from_csv(filename):
        points = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                x, z, r = map(float, row)
                points.append((x, z, r))
        return points