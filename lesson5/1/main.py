from load_csv_file import CSVLoader
from GraphWindow import GraphWindow
from DiagramWindow import DiagramWindow

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # Создание основного окна с кнопками
    
    def visualize_points(self):
        points = CSVLoader.load_points_from_csv('data/points.csv')
        graph_window = GraphWindow(points)
        # Отображение окна для визуализации точек
    
    def build_epure(self):
        interpolated_points = []
        for i in range(20):
            # Интерполяция значений параметра R методом триангуляции Делоне
            # и добавление новых точек
            diagram_window = DiagramWindow(interpolated_points)
        # Отображение окна для построения эпюры
        
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

