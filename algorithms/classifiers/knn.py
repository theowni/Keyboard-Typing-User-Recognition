import operator
from datetime import timedelta


class kNNClassifier:
    def __init__(self, distanceCls):
        self.distanceCls = distanceCls

    def get_k_neighbours(self, test_instance, training_set, k):
        distances = list()
        for x in range(len(training_set)):
            train_instance = training_set[x]
            dist = self.distanceCls.measure(
                self.distanceCls,
                test_instance.input0_time,
                train_instance.input0_time
            )
            if test_instance.ip != train_instance.ip:
                dist += 1000
            if test_instance.browser != train_instance.browser:
                dist += 600
            if test_instance.time - train_instance.time > timedelta(hours=1):
                dist += 200

            distances.append((training_set[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = list()
        for x in range(k):
            neighbors.append(distances[x][0])
        return neighbors

    def frequent_sort(self, neighbours):
        id_to_num = dict()

        for neighbour in neighbours:
            class_id = neighbour.user_id
            if class_id in id_to_num:
                id_to_num[class_id] += 1
            else:
                id_to_num[class_id] = 0

        sorted_id_to_num = sorted(
            id_to_num.items(),
            key=operator.itemgetter(1),
            reverse=True

        )
        return sorted_id_to_num

    def classify(self, test_instance, training_set, k):
        neighbours = self.get_k_neighbours(
            test_instance,
            training_set,
            k
        )

        ret_class_id = self.frequent_sort(neighbours)[0][0]

        return ret_class_id
