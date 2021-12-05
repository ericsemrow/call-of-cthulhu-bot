from src.models.char.from_raw import FromRaw
from src.models.char.skill import SkillModel
import difflib, re

class SkillsModel(FromRaw):

  skills = []

  def __init__(self, source = []):
    self.skills = []
    for val in source:
      self.skills.append(SkillModel(val))
    

  def get_skill_by_name(self, skill_name, strip_name=True):
    for val in self.skills:
      if val.name == skill_name:
        if strip_name:
          val.name = re.sub("[\(\[].*?[\)\]]","", val.name)
          
        return val


  def get_closest_skill_name(self, skill_name):
    matches = self.match_substr(skill_name,self.get_skill_names())
    
    return matches

  def match_substr(self, needle, haystack):
    return [i for i in haystack if needle.lower() in i.lower()]

  def get_skill_names(self):
    names = []
    for val in self.skills:
      names.append(val.name)
    
    return names


  def to_dict(self):
    skills_list = []
    for val in self.skills:
      skills_list.append(val.to_dict())

    return skills_list
  
  @staticmethod
  def from_dict(source: list):
    return SkillsModel(source)

  @staticmethod
  def from_raw(source: dict):
    """
    used_01,name_01,val_01,used_02,name_02,val_02,used_03,name_03,val_03,used_04,name_04,val_04,used_05,name_05,val_05,used_06,name_06,val_06,used_07,name_07,val_07,used_08,name_08,val_08,used_09,name_09,val_09,used_10,name_10,val_10,used_11,name_11,val_11,used_12,name_12,val_12,used_13,name_13,val_13,used_14,name_14,val_14,used_15,name_15,val_15,used_16,name_16,val_16,used_17,name_17,val_17,used_18,name_18,val_18,used_19,name_19,val_19,used_20,name_20,val_20,used_21,name_21,val_21,used_22,name_22,val_22,used_23,name_23,val_23,used_24,name_24,val_24,used_25,name_25,val_25,used_26,name_26,val_26,used_27,name_27,val_27,used_28,name_28,val_28,used_29,name_29,val_29,used_30,name_30,val_30,used_31,name_31,val_31,used_32,name_32,val_32,used_33,name_33,val_33,used_34,name_34,val_34,used_35,name_35,val_35,used_36,name_36,val_36,used_37,name_37,val_37,used_38,name_38,val_38,used_39,name_39,val_39,used_40,name_40,val_40,used_41,name_41,val_41,used_42,name_42,val_42,used_43,name_43,val_43,used_44,name_44,val_44,used_45,name_45,val_45,used_46,name_46,val_46,used_47,name_47,val_47,used_48,name_48,val_48,used_49,name_49,val_49,used_50,name_50,val_50,used_51,name_51,val_51,used_52,name_52,val_52,used_53,name_53,val_53,used_54,name_54,val_54,used_55,name_55,val_55,used_56,name_56,val_56,used_57,name_57,val_57,used_58,name_58,val_58,used_59,name_59,val_59,used_60,name_60,val_60,used_61,name_61,val_61,used_62,name_62,val_62,used_63,name_63,val_63,used_64,name_64,val_64,used_65,name_65,val_65,used_66,name_66,val_66,used_67,name_67,val_67,used_68,name_68,val_68,used_69,name_69,val_69,used_70,name_70,val_70,used_71,name_71,val_71,used_72,name_72,val_72

    """
    
    skills = []
    counter = 0
    for i in range(72):
      try:
        if source[f'name_{str(i).zfill(2)}']:
          skill = {
            "used": source[f'used_{str(i).zfill(2)}'],
            "name": source[f'name_{str(i).zfill(2)}'],
            "val": source[f'val_{str(i).zfill(2)}']
          }
          skills.append(skill)
      except KeyError:
        pass

      counter += 1
    
    return SkillsModel(skills)

  
  def __str__(self):
    skill_string =  "**Skills:**"
    for val in self.skills:
      skill_string += f"""
      {str(val)}"""
    
    return skill_string
    