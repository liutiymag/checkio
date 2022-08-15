class MicrowaveBase:
    current_time = '00:00'
    max_time = 90 * 60
    min_time = 0

    def display_format(self, broken_position=None):
        displayed_time = ''
        for n, i in enumerate(self.current_time):
            if n == broken_position:
                displayed_time += '_'
            else:
                displayed_time += i
        return displayed_time


class Microwave1(MicrowaveBase):

    def display_time(self):
        dt = self.display_format(broken_position=0)
        return dt


class Microwave2(MicrowaveBase):
    def display_time(self):
        dt = self.display_format(broken_position=len(self.current_time) - 1)
        return dt


class Microwave3(MicrowaveBase):
    def display_time(self):
        dt = self.display_format()
        return dt


class RemoteControl:
    def __init__(self, microwave):
        self.microwave = microwave

    def set_time(self, time_str):
        self.microwave.current_time = time_str

    def add_time(self, t):
        final_seconds = 0
        current_seconds = self.time_str_to_seconds(self.microwave.current_time)
        if 's' in t:
            final_seconds = current_seconds + int(t.split('s')[0])
        if 'm' in t:
            final_seconds = current_seconds + int(t.split('m')[0]) * 60

        if final_seconds > self.microwave.max_time:
            final_seconds = self.microwave.max_time

        final_time = self.seconds_to_time_str(final_seconds)
        self.microwave.current_time = final_time

    def del_time(self, t):
        final_seconds = 0
        current_seconds = self.time_str_to_seconds(self.microwave.current_time)
        if 's' in t:
            final_seconds = current_seconds - int(t.split('s')[0])
        if 'm' in t:
            final_seconds = current_seconds - int(t.split('m')[0]) * 60

        if final_seconds < self.microwave.min_time:
            final_seconds = self.microwave.min_time

        final_time = self.seconds_to_time_str(final_seconds)
        self.microwave.current_time = final_time

    def show_time(self):
        return self.microwave.display_time()

    @staticmethod
    def time_str_to_seconds(time_str):
        minutes = int(time_str.split(':')[0])
        seconds = int(time_str.split(':')[1])
        total_seconds = minutes * 60 + seconds
        return total_seconds

    @staticmethod
    def seconds_to_time_str(seconds):
        minutes = str(int(seconds / 60))
        if len(minutes) == 1:
            minutes = '0' + minutes

        seconds = str(seconds % 60)
        if len(seconds) == 1:
            seconds = '0' + seconds

        time_str = f'{minutes}:{seconds}'
        return time_str


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")
