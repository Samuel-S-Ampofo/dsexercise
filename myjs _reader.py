
import json

with open("../documents/movies.json") as json_file:
    json_data = json.load(json_file)
    print(json_data)