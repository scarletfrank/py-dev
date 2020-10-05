class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah')
            self.hungry = False
        else:
            print('No, thanks!')

class SongBird(Bird):
    def __init__(self) -> None:
        super().__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

class Fibs:
    def __init__(self) -> None:
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self

