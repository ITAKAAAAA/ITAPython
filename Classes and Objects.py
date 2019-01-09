class Enemy:
    life = 3
    # Inizializzaione per le classi
    def __init__(self):
        self.life = 4
    def attack(self):
        print("Ouch!")
        self.life -= 1

    def checklife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")

#Creating an Object
enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checklife()
enemy2.checklife()