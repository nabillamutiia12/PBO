class Avangers:
    def __init__(self,name,health,attPower,armor):
        self.name = name
        self.health = health
        self.attPower = attPower
        self.armor = armor

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attPower)

    def diserang(self, lawan, attPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attPower_lawan/self.armor
        print('serangan terasa : ' + str(attack_diterima))
        self.health -= attack_diterima
        print('Darah ' + self.name + ' tersisa ' + str(self.health))

Ironman = Avangers('Ironman',100,10,10)
Spiderman = Avangers('Spiderman',100,20,20)
Ironman.serang(Spiderman)
print( )
Spiderman.serang(Ironman)
print( )
Spiderman.serang(Ironman)
Spiderman.serang(Ironman)
Ironman.serang(Spiderman)
Ironman.serang(Spiderman)
Ironman.serang(Spiderman)
