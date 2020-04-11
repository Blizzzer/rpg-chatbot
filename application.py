from preprocessing import process_input


class Application(object):

    @staticmethod
    def start_application():
        print("Welcome in our rpg chat bot npc !!!")
        while True:
            expression = input("Player: ")
            process_input(expression)


Application.start_application()