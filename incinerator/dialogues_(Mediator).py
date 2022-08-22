VOWELS = "AEIOUaeiou"


class Participant:
    def __init__(self, name):
        self.name = name
        self.chat = None

    def send(self, message):
        self.chat.dialogue.append({'name': self.name,
                                   'message': message})


class Human(Participant):
    pass


class Robot(Participant):
    pass


class Chat:
    def __init__(self):
        self.dialogue = []
        self.participant_1 = None
        self.participant_2 = None

    @staticmethod
    def translate_to_robot(message):
        robot_message = ''
        for i in message:
            if i in VOWELS:
                robot_message += '0'
            else:
                robot_message += '1'
        return robot_message

    def show_human_dialogue(self):
        human_dialog = '\n'.join(f"{record['name']} said: {record['message']}" for record in self.dialogue)
        return human_dialog

    def show_robot_dialogue(self):
        robot_dialog = '\n'.join(f"{record['name']} said: {self.translate_to_robot(record['message'])}" for record in self.dialogue)
        return robot_dialog

    def connect_human(self, participant: Participant):
        participant.chat = self

    def connect_robot(self, participant: Participant):
        participant.chat = self


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")