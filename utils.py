import json
from json.decoder import JSONDecodeError
from typing import Dict


class Car:
    def __init__(self, car: Dict):
        self.car = car

    def __str__(self):
        msg = f'''\n
brand: {self.car['brand']}
model: {self.car['model']}
year: {self.car['year']}
        '''
        return msg

    def append_data_to_json(self):
        try:
            # read data from json file
            with open('car.json', 'r') as f:
                objects: list = json.load(f)
                objects.append(self.car)
                f.close()
        except (JSONDecodeError, FileNotFoundError):
            with open('car.json', 'w') as f1:
                json.dump([], f1)
                objects = [self.car]
                f1.close()

        # write data to json file
        with open('car.json', 'w') as f:
            json.dump(objects, f, indent=4)
