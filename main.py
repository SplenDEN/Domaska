class Car:
    def init(self, color, type , year):
        self.color = color
        self.type = type
        self.year = year

    def turn_on(self):
        print('Заведён')

    def turn_off(self):
        print('Заглушен')

    def col(self):
        print(self.color)

    def typ(self):
        print(self.type)

    def yea(self):
        print(self.year)

telo = Car('black', 'ford', 1996)
telo.turn_on()
telo.turn_off()
telo.col()
telo.typ()
telo.yea()