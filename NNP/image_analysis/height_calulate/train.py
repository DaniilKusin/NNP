from human_pose_estimation_opencv.get_human_data import get_points
from sklearn.model_selection import train_test_split
from dataset_worker import DatasetWorker
from height_nn import HeightNN


def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return int(((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5)


def extract_features_heights(human_data: list[dict]):
    features = []
    heights = []
    for el in human_data:
        heights.append(el['height'])
        f = []
        f.append(calculate_distance(el['RShoulder'], el['LShoulder']))
        f.append(calculate_distance(el['Nose'], el['RAnkle']))
        features.append(f.copy())
    return features, heights


def main():
    dw = DatasetWorker()
    d = dw.read_csv_to_dict(['height', 'RShoulder', 'LShoulder', 'Nose', 'RAnkle'])
    print(len(d))
    features, heights = extract_features_heights(d)
    #heights, body_p = dw.read_csv_to_lists(['RShoulder', 'LShoulder', 'Nose', 'LAnkle'])
    height_nn = HeightNN()

    X = features
    y = heights
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #height_nn.load()
    height_nn.model.fit(X_train, y_train)

    y_pred = height_nn.model.predict(X_test)
    height_nn.evaluate(y_test, y_pred)
    height_nn.save()


if __name__ == '__main__':
    main()
