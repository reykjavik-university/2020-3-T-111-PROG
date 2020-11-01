from collections import defaultdict


class Sample:
    def __init__(self, value: float, classification: str) -> None:
        self.value = value
        self.classification = classification

    def __str__(self) -> str:
        return f"{self.value}: {self.classification}"


class ClosestMeanClassifier:
    """ A classifier that predicts the classification which has the closest mean (i.e. average) """

    def __init__(self, samples: list) -> None:
        self.mean_by_classification = self._calculate_means(samples)

    @staticmethod
    def _calculate_means(samples: list) -> dict:
        means = defaultdict(float)
        counts = defaultdict(int)
        for sample in samples:
            previous_mean = means[sample.classification]
            n = counts[sample.classification]
            updated_mean = (sample.value + n * previous_mean) / (n + 1)
            means[sample.classification] = updated_mean
            counts[sample.classification] += 1
        return means

    def classify(self, value: float) -> str:
        """ Predict the classification for the supplied value """
        closest_so_far = float("inf")
        prediction = None
        for classification, mean in self.mean_by_classification.items():
            distance = abs(value - mean)
            if distance < closest_so_far:
                closest_so_far = distance
                prediction = classification
        return prediction
