from typing import List
from model import Corpus
import json


class InputStreamReader:

    def __init__(self, path: str):
        self.corpuses: List[Corpus] = []
        self.path = path

    def parse_json(self):
        with open(self.path) as json_file:
            data = json.load(json_file)
            for tag in data:
                self.corpuses.append(
                    Corpus(
                        tag["tag"],
                        tag["keywords"],
                        tag["tagsToAchieveBefore"],
                        tag["nextTags"],
                        tag["tagsToCloseWhenDone"],
                        tag["isClosed"],
                        tag["isAchieved"],
                        tag["redirectTo"],
                        tag["patterns"],
                        tag["responses"]
                    )
                )
