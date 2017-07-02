from datetime import datetime


class UserData:
    def __init__(self, tuple_object):
        self.time = datetime.strptime(tuple_object[0], "%Y-%m-%d %H:%M:%S")
        self.user_id = int(tuple_object[1])
        self.input0_time = self.parse_input(tuple_object[2])
        self.ip = tuple_object[3]
        self.browser = tuple_object[4]

    def parse_input(self, input0):
        splitted = input0.split(' ')
        inputs = list()
        last_time = 0

        for i in range(1, len(splitted)):
            key = splitted[i]
            if 'd_16' in key:
                continue
            if 'u_16' in key:
                continue
            if key is '':
                break
            data = key.split('_')
            diff = int(data[2]) - last_time
            last_time = int(data[2])
            inputs.append(diff)

        return inputs

    def __str__(self):
        return str(self.user_id)
