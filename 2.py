class Footbalist:
    def __init__(self, name, number, height, weight, clean_sheets=0, tackles=0):
        self.name = name
        self.number = number
        self.height = height
        self.weight = weight
        self.clean_sheets = clean_sheets  
        self.tackles = tackles  

    def player_first_name(self):
        return 'The player first name: ' + self.name

    def player_number(self):
        return f'The player {self.name} number is {self.number}'

    def player_stats(self):
        return f'{self.name} has {self.clean_sheets} clean sheets and {self.tackles} tackles.'


class Goalkeeper(Footbalist):
    def __init__(self, name, number, height, weight, clean_sheets):
        super().__init__(name, number, height, weight, clean_sheets=clean_sheets)

    def goalkeeper_stats(self):
        return f'{self.name} has {self.clean_sheets} clean sheets.'


class Defenders(Footbalist):
    def __init__(self, name, number, height, weight, tackles):
        super().__init__(name, number, height, weight, tackles=tackles)

    def defender_stats(self):
        return f'{self.name} has made {self.tackles} tackles this season.'



player_1 = Footbalist('Danial Soufi', 7, 175, 60, clean_sheets=5, tackles=12)  
player_2 = Goalkeeper('Arvin Zaheri', 17, 175, 90, clean_sheets=15)  
player_3 = Defenders('Media Sharifi', 20, 180, 91, tackles=35)  

print(player_1.player_first_name())
print(player_1.player_number())
print(player_1.player_stats())  

print(player_2.goalkeeper_stats())  
print(player_3.defender_stats()) 
