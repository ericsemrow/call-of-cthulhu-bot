from src.models.char.from_raw import FromRaw
import math

class AttackModel(FromRaw):

  name = ""
  damage = ""
  rnge = ""
  num_attacks = 0

  def __init__(self, source: dict = {}):
    self.name = source["name"]
    self.damage = source["damage"]
    self.rnge = source["range"]
    self.num_attacks = source["num_attacks"]
    self.db = source["db"]
    
  def to_dict(self):
    return {
      "name": self.name,
      "damage": self.damage,
      "range": self.rnge,
      "num_attacks": self.num_attacks,
      "db": self.db
    }

    return skills_list
  
  @staticmethod
  def from_dict(source: dict):
    return SkillModel(source)


  def __str__(self):
    return f"""{self.name} _{self.damage}_ / {self.rnge} / {self.num_attacks}""" 
    