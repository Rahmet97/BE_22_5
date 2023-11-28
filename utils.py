import json
from json.decoder import JSONDecodeError
from typing import Dict
from tabulate import tabulate


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
            with open('movie.json', 'r') as f:
                objects: list = json.load(f)
                objects.append(self.car)
                f.close()
        except (JSONDecodeError, FileNotFoundError):
            with open('movie.json', 'w') as f1:
                json.dump([], f1)
                objects = [self.car]
                f1.close()

        # write data to json file
        with open('movie.json', 'w') as f:
            json.dump(objects, f, indent=4)


def print_tab(movies: list):
    movies_table = []
    for movie in movies:
        movies_table.append([
            movie["id"],
            movie["name"],
            movie["year"],
            ", ".join(movie["genre"]),
            movie["duration"],
            movie["language"],
            movie["country"],
            movie["description"]
        ])

    # Display the tabulated data
    headers = ["ID", "Name", "Year", "Genre", "Duration", "Language", "Country", "Description"]
    print(tabulate(movies_table, headers=headers, tablefmt="grid"))
