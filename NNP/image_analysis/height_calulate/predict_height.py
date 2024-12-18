import pickle
import pickle
import inspect


from pathlib import Path

def get_current_directory():
    # Получаем путь к текущему файлу
    current_file = inspect.getfile(inspect.currentframe())

    # Получаем директорию, используя pathlib
    current_dir = Path(current_file).resolve().parent

    return current_dir

def predict_height(human_points: dict):
    """
    Рассчитывает рост на основе точек тела.

    :param human_points: Словарь с ключевыми точками тела, полученными из get_points.
    :param model_path: Путь к сохранённой модели.
    :return: Предсказанный рост.
    """

    def calculate_distance(point1, point2):
        """Calculate the Euclidean distance between two points."""
        return int(((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5)

    # Проверяем, что в данных присутствуют необходимые точки
    required_points = ['RShoulder', 'LShoulder', 'Nose', 'RAnkle']
    for point in required_points:
        if point not in human_points or human_points[point] is None:
            raise ValueError(f"Missing or invalid point: {point}")

    # Извлекаем признаки
    features = [
        calculate_distance(human_points['RShoulder'], human_points['LShoulder']),
        calculate_distance(human_points['Nose'], human_points['RAnkle']),
    ]

    cur_dir = get_current_directory()
    fp = str(cur_dir / "model")
    # Загружаем модель
    with open(fp, 'rb') as model_file:
        model = pickle.load(model_file)

    # Предсказываем рост
    height = model.predict([features])[0]
    return height
