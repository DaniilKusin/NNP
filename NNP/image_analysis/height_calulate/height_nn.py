from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, BaggingRegressor
from sklearn.svm import SVR
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import pickle
import inspect


from pathlib import Path

def get_current_directory():
    # Получаем путь к текущему файлу
    current_file = inspect.getfile(inspect.currentframe())

    # Получаем директорию, используя pathlib
    current_dir = Path(current_file).resolve().parent

    return current_dir

class HeightNN:
    def __init__(self, model=None):
        """Инициализация класса с выбором модели."""
        self.model = model if model else RandomForestRegressor(random_state=42)

    def evaluate(self, y_test, y_pred):
        """Оценка модели с использованием метрик."""
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        pmae = mean_absolute_percentage_error(y_test, y_pred)
        print(f"Mean Squared Error: {mse}")
        print(f"Mean Absolute Error: {mae}")
        print(f"Mean Absolute Percentage Error: {pmae}")

    def save(self):
        cur_dir = get_current_directory()
        fp = str(cur_dir / "model")
        with open(fp, 'wb') as picklefile:
            pickle.dump(self.model, picklefile, protocol=5)

    def load(self):
        cur_dir = get_current_directory()
        fp = str(cur_dir / "model")
        with open(fp, 'rb') as picklefile:
            self.model = pickle.load(picklefile)
