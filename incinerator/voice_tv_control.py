class VoiceCommand:
    def __init__(self, collection: list):
        self._collection = collection
        self._cursor = 0

    def first_channel(self):
        self._cursor = 0
        return self.current_channel()

    def last_channel(self):
        self._cursor = len(self._collection) - 1
        return self.current_channel()

    def turn_channel(self, n):
        if self.is_exist(n) == "Yes":
            self._cursor = n - 1
            return self.current_channel()

    def next_channel(self):
        if self._cursor + 1 > len(self._collection) - 1:
            self._cursor = 0
        else:
            self._cursor += 1
        return self.current_channel()

    def previous_channel(self):
        if self._cursor == 0:
            self._cursor = len(self._collection) - 1
        else:
            self._cursor -= 1
        return self.current_channel()

    def current_channel(self):
        current = self._collection[self._cursor]
        return current

    def is_exist(self, channel):
        if type(channel) == int:
            if len(self._collection) >= channel:
                return "Yes"
            else:
                return "No"

        if type(channel) == str:
            if channel in self._collection:
                return "Yes"
            else:
                return "No"


if __name__ == '__main__':
    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")
