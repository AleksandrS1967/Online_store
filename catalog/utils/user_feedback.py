import os
import json


def feedback(file, data):
    with open(file, "a") as f:
        if os.stat(file).st_size == 0:
            json.dump([data], f)
        else:
            with open(file) as f_:
                list_ = json.load(f_)
                list_.append(data)
            with open(file, "w") as f_1:
                json.dump(list_, f_1)
