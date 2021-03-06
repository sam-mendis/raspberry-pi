# object orientated programming example
class parameters:

    def __init__(self, name, input, value):
        self.name = name
        self.input = input
        self.value = value

    def input_v(self):
        return self.input

    def reading(self, value):
        self.value = value

    def change(self, input):
        self.input = input


Time = parameters("Time", 1, 0)
Temp = parameters("Temp", 25, 100)

Temp.reading(10)
Time.change(30)
t = Temp.value
print(Time.input)
print(t)
