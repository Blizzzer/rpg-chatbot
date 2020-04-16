import random

from conversationgraph import ConversationGraph
from model import Corpus
from neuralnetwork import NeuralNetwork
from preprocessing import Preprocessor

conversation_graph = ConversationGraph()
lemmatizer = Preprocessor(conversation_graph.corpuses)
neural_network = NeuralNetwork(8, conversation_graph)

neural_network.train(
    lemmatizer.prepare_nn_entries(),
    lemmatizer.lemmatize_all_patterns())

print("Welcome in our rpg chat bot npc !!!")

while True:
    expression = input("Player: ")
    input_lemmatize = lemmatizer.lemmatize_expression(expression)
    matching_tag: str = neural_network.predict(input_lemmatize)
    tag: Corpus = conversation_graph.get_corpus_to_respond(matching_tag)
    conversation_graph.close_corresponding_tags(tag)

    tag.isAchieved = True

    textToPrint: str = random.choice(tag.responses)

    print(textToPrint)
