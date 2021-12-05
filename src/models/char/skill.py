from src.models.char.from_raw import FromRaw
import math

class SkillModel(FromRaw):

  used = ""
  name = ""
  val = 0

  def __init__(self, source: dict = {}):
    self.used = source["used"]
    self.name = source["name"]
    self.val = int(source["val"] or 0)
    
  def to_dict(self):
    return {
      "used": self.used,
      "name": self.name,
      "val": int(self.val or 0)
    }

    return skills_list
  
  @staticmethod
  def from_dict(source: dict):
    return SkillModel(source)

  def success(self):
    return self.val or 0
  
  def hard(self):
    return math.ceil(self.success()/2)
  
  def extreme(self):
    return math.ceil(self.success()/5)

  def success_level(self, roll):
    if roll <= self.extreme():
      return "Extreme"
    elif roll <= self.hard():
      return "Hard"
    elif roll <= self.success():
      return "Normal"
    else:
      return False

  def __str__(self):
    return f"""{self.name} _{self.success()}/{self.hard()}/{self.extreme()}_""" 
    