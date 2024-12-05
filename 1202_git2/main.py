class LittleBell:
    def sound(self):
        print('ding')


class BigBell:
    def __init__(self):
        self.d = 2

    def sound(self):
        if self.d % 2 == 0:
            print('ding')
            self.d += 1
        else:
            print('dong')
            self.d += 1


class BellTower:
    def __init__(self, *args):
        self.colocola = []
        for i in args:
            self.colocola.append(i)

    def sound(self):
        for i in self.colocola:
            i.sound()
        print('...')

    def append(self, arg):
        self.colocola.append(arg)



bell_tower = BellTower(BigBell(), LittleBell())
bell_tower.sound()
bell_tower.sound()
bell_tower.append(BigBell())
bell_tower.sound()
bell_tower.sound()