import random
from configparser import SafeConfigParser

from conversationgraph import ConversationGraph
from model import Corpus
from neuralnetwork import NeuralNetwork
from preprocessing import Preprocessor

config = SafeConfigParser()
config.read("config.ini")

conversation_graph = ConversationGraph(config.get("main", "path_to_cg_json"))
lemmatizer = Preprocessor(conversation_graph.corpuses)
neural_network = NeuralNetwork(4, conversation_graph)

neural_network.train(
    lemmatizer.prepare_nn_entries(),
    lemmatizer.lemmatize_all_patterns())

print(config.get("strings", "welcome_message"))

while True:
    expression = input(config.get("strings", "player_tag") + ": ")
    input_lemmatize = lemmatizer.lemmatize_expression(expression)
    matching_tag: str = neural_network.predict(input_lemmatize)

    tag: Corpus = conversation_graph.get_corpus_to_respond(matching_tag)

    conversation_graph.close_corresponding_tags(tag)

    tag.isAchieved = True

    print(config.get("strings", "npc_tag") + ": " + random.choice(tag.responses))
