from typing import Dict
from conversationgraph import ConversationGraph, Corpus

print("Hello World")

graph = ConversationGraph("conversations-test.json")
print(graph.corpuses[0].tag)

input_string: str = ""

# TODO: obtain input string
# input_string = inputStringObtainer()

tagProbabilities: Dict[str, float]

# TODO: obtain tags probabilities based on input string
# tagProbabilities = neuralNetworkAnalysis(input_string)

tag: Corpus

# TODO: obtain corpus based on tags probabilities map and searcher result
# tag = graph.searchTagToReturn(tagProbabilities)

textToPrint: str = ""

# TODO: choose text to print - random from corpus
# textToPrint = randomizer(tag.responses)

print(textToPrint)




