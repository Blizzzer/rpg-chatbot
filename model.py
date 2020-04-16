from typing import List


class Corpus:
    def __init__(self,
                 tag: str,
                 keywords: List[str],
                 tagsToAchieveBefore: List[str],
                 tagsToCloseWhenDone: List[str],
                 isClosed: bool,
                 isAchieved: bool,
                 redirectTo: str,
                 patterns: List[str],
                 responses: List[str]):
        self.tag = tag
        self.keywords = keywords
        self.tagsToAchieveBefore = tagsToAchieveBefore
        self.tagsToCloseWhenDone = tagsToCloseWhenDone
        self.isClosed = isClosed
        self.isAchieved = isAchieved
        self.redirectTo = redirectTo
        self.patterns = patterns
        self.responses = responses


class NeuralNetworkTrainingDTO:
    def __init__(self,
                 tag: str,
                 patterns: List[List[str]]):
        self.tag = tag
        self.lemmas = patterns


class ConversationGraphDTO:
    def __init__(self,
                 tag: str,
                 probability):
        self.tag = tag
        self.probability = probability
