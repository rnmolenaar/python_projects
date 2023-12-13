class Character:
  def __init__(self, name, gender):
    name = self.name
    gender = self.gender

class Hero(Character):
  def __init__(self, name, gender, level, hp)
    super().__init=__(name, gender)
    level = self.level
    hp = self.hp
   
class NPC(Character):
    def __init__(self, name, gender):
        super().__init__(name, gender)
        
    def npc_says(self):
        return f"{self.name} says: 'The carrots are cheaper this year. The harvest was good'"


  
  
  
