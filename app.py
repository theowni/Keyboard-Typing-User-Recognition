import os
import random
import sqlite3
from db_lib.database_manager import DatabaseManager
from db_lib.entities.user_data import UserData
from algorithms.classifiers.knn import kNNClassifier
from algorithms.distances.manhattan_distance import ManhattanDistance


K_NUM = 5
PATH = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    db_path = os.path.join(PATH, 'database.db')
    database = DatabaseManager(db_path)
    insert_data_script = os.path.join(PATH, 'data/insert_data.sql')

    try:
        database.run_sql_from_file(insert_data_script)
    except sqlite3.IntegrityError:
        pass

    users_raw = database.execute(
        'SELECT * from user_typing_data WHERE user_id < 30'
    )
    users_list = list()

    for item_raw in users_raw:
        user = UserData(item_raw)
        users_list.append(user)

    random.shuffle(users_list)
    percent = 0.73
    train_len = int(len(users_list)*percent)
    test_len = len(users_list) - train_len
    train_set = users_list[train_len:]
    test_set = users_list[:-test_len]

    successes = 0
    knn_classifier = kNNClassifier(ManhattanDistance)
    for test_inst in test_set:
        result_id = knn_classifier.classify(
            test_inst,
            train_set,
            K_NUM
        )
        if test_inst.user_id == result_id:
            successes += 1

    accuracy = successes/len(test_set)
    print('Accuracy: %f' % accuracy)

    database.close()
