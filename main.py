from typing import List

import application

first_conversation: List[str] = [
    "Who are you?",
    "Hi",
    "What's your name?",
    "Where are we now?",
    "Thank you very much",
    "Is there any job for me here?",
    "I need some weapons, where i can found those?",
    "Hello",
    "I have searched the caves, there are some cult activities there",
    "Where can I go now?",
    "Appreciate it",
]
second_conversation: List[str] = [
    "Hello",
    "I encountered some bandit camp nearby",
    "I forgot asking. What is your name?",
    "What you actualy do here?",
    "Thanks",
    "I have cleared bandit camp, I heard about some Black Spider there.",
    "Triboar should be nearby. How to get there?",
    "Fine, I will go there"

]

application.main([4, 4], 0.5)
