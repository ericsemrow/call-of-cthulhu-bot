from src.models.char.from_raw import FromRaw
from src.models.char.attack import AttackModel

class AttacksModel(FromRaw):

  attacks = []

  def __init__(self, source = []):
    self.attacks = []
    for val in source:
      self.attacks.append(AttackModel(val))
    
  def to_dict(self):
    attacks_list = []
    for val in self.attacks:
      attacks_list.append(val.to_dict())

    return attacks_list
  
  @staticmethod
  def from_dict(source: list):
    return AttacksModel(source)

  @staticmethod
  def from_raw(source: dict):
    """
    db,atk_name_01,atk_damage_01,atk_range_01,atk_num_attacks_01,atk_name_02,atk_damage_02,atk_range_02,atk_num_attacks_02,atk_name_03,atk_damage_03,atk_range_03,atk_num_attacks_03,atk_name_04,atk_damage_04,atk_range_04,atk_num_attacks_04,atk_name_05,atk_damage_05,atk_range_05,atk_num_attacks_05,atk_name_06,atk_damage_06,atk_range_06,atk_num_attacks_06,atk_name_07,atk_damage_07,atk_range_07,atk_num_attacks_07,atk_name_08,atk_damage_08,atk_range_08,atk_num_attacks_08,atk_name_09,atk_damage_09,atk_range_09,atk_num_attacks_09,atk_name_10,atk_damage_10,atk_range_10,atk_num_attacks_10,atk_name_11,atk_damage_11,atk_range_11,atk_num_attacks_11,atk_name_12,atk_damage_12,atk_range_12,atk_num_attacks_12,atk_name_13,atk_damage_13,atk_range_13,atk_num_attacks_13,atk_name_14,atk_damage_14,atk_range_14,atk_num_attacks_14,atk_name_15,atk_damage_15,atk_range_15,atk_num_attacks_15,atk_name_16,atk_damage_16,atk_range_16,atk_num_attacks_16

    """
    
    attacks = []
    counter = 0
    for i in range(16):
      try:
        if source[f'atk_name_{str(i).zfill(2)}']:
          attack = {
            "name": source[f'atk_name_{str(i).zfill(2)}'],
            "damage": source[f'atk_damage_{str(i).zfill(2)}'],
            "range": source[f'atk_range_{str(i).zfill(2)}'],
            "num_attacks": source[f'atk_num_attacks_{str(i).zfill(2)}'],
            "db": source["db"]
          }
          attacks.append(attack)
      except KeyError:
        pass

      counter += 1
    
    return AttacksModel(attacks)

  
  def __str__(self):
    attack_string =  "**Attacks:**"
    for val in self.attacks:
      attack_string += f"""
      {str(val)}"""
    
    return attack_string
    