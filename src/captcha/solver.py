import numpy as np
from scipy import stats

from captcha.utils import svg_to_vec, split_image, IMAGE_SPLIT_RANGES


class KNN:
    def __init__(self, k=10):
        self.X_train = None
        self.y_train = None
        self.k = k

    def fit(self, X, y):
        self.X_train = np.array(X, dtype=np.int)
        self.y_train = np.array(y, dtype=np.int)

    def predict(self, x):
        assert x.shape == (self.X_train.shape[1],)
        dist = np.sum((self.X_train - x) ** 2, axis=1)
        min_dist_indices = np.argsort(dist)[:self.k]
        return stats.mode(self.y_train[min_dist_indices]).mode[0]


class CaptchaSolver:
    def __init__(self):
        self.data_loaded = False
        self.knns = []

    def load_data(self, data_path):
        data = np.load(data_path)
        for i in range(len(IMAGE_SPLIT_RANGES)):
            knn_i = KNN()
            knn_i.fit(data['X'][i], data['y'][i])
            self.knns.append(knn_i)
        self.data_loaded = True

    def solve_captcha(self, captcha_vector):
        if not self.data_loaded:
            raise Exception("Data Not Loaded")

        result = ""
        captcha_splits = split_image(captcha_vector)
        for i, captcha_split in enumerate(captcha_splits):
            result += str(self.knns[i].predict(captcha_split))
        return result


__captcha_solver = CaptchaSolver()


def load_captcha_data(data_path):
    __captcha_solver.load_data(data_path)


def solve_captcha(captcha_svg):
    captcha_vec = svg_to_vec(captcha_svg)
    captcha_result = __captcha_solver.solve_captcha(captcha_vec)
    return captcha_result
