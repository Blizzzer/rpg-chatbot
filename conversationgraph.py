import json
from typing import List


class ConversationGraph:
    def __init__(self, path: str):
        with open(path) as json_file:
            data = json.load(json_file)
            self.corpuses: List[Corpus] = []
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
                        tag["patterns"],
                        tag["responses"]
                    )
                )


class Corpus:
    def __init__(self,
                 tag: str,
                 keywords: List[str],
                 tagsToAchieveBefore: List[str],
                 nextTags: List[str],
                 tagsToCloseWhenDone: List[str],
                 isClosed: bool,
                 isAchieved: bool,
                 patterns: List[str],
                 responses: List[str]):
        self.tag = tag
        self.keywords = keywords
        self.tagsToAchieveBefore = tagsToAchieveBefore
        self.nextTags = nextTags
        self.tagsToCloseWhenDone = tagsToCloseWhenDone
        self.isClosed = isClosed
        self.isAchieved = isAchieved
        self.patterns = patterns
        self.responses = responses
