class Avangers:
    
    def __init__(self,name):
        self.health_pool = [0,100,200,300,400,500]
        self.ulti_pool = [0,10,20,30,40,50]
        self.defense_pool = [0,1,2,3,4,5]
        self.__name = name
        self.__exp = 0
        self.__level = 0

    def show_info(self):
        print("{} \n\tlevel: {}\n\thealth: {} \n\tulti: {} \n\tdefense: {}".format(
              self.__name,
              self.__level,
              self.__health,
              self.__ulti,
              self.__defense,
            )
        )

    @property
    def health_pool(self):
        pass

    @property
    def ulti_pool(self):
        pass

    @property
    def defense_pool(self):
        pass

    @property
    def levelUp(self):
        pass

    @property
    def gainExp(self):
        pass

    @health_pool.setter
    def health_pool(self,input):
        self.__health_pool = input

    @ulti_pool.setter
    def ulti_pool(self,input):
        self.__ulti_pool = input

    @defense_pool.setter
    def defense_pool(self,input):
        self.__defense_pool = input

    @gainExp.setter
    def gainExp(self,input):
        self.__exp += input
        if(self.__exp >= 100):
            self.levelUp = self.__exp//100
            self.__exp %= 100

    @levelUp.setter
    def levelUp(self,input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__ulti = self.__ulti_pool[self.__level]
        self.__defense = self.__defense_pool[self.__level]
        

class AvangersRank(Avangers):

    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,50,100,150,200,250]
        self.ulti_pool = [0,20,40,60,80,100]
        self.defense_pool = [0,0.5,1,1.5,2,2.5]
        self.levelUp = 1

class AvangersBrawl(Avangers):

    def __init__(self,name):
        super().__init__(name)
        self.heal_th_pool = [0,200,300,400,500,600]
        self.ulti_pool = [0,20,40,60,80,100]
        self.defense_pool = [0,2,4,6,8,10]
        self.levelUp = 1

Ironman = AvangersRank('Ironman')
Hulk = AvangersBrawl('Hulk')
Ironman.show_info()
Hulk.show_info()

Ironman.gainExp = 230
Hulk.gainExp = 260
Ironman.show_info()
Hulk.show_info()
