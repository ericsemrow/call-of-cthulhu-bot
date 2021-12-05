from src.models.char.skills import SkillsModel
from src.models.char.attacks import AttacksModel
from src.models.char.from_raw import FromRaw

class Character(FromRaw):

  @property
  def attacks(self):
    return self._attacks

  @property
  def skills(self):
    return self._skills



  def __init__(self, id=None,owner="",name="",pronouns="",occupation="",birthplace="",residence="",sex="",age="",st="",con="",dex="",powr="",app="",i="",siz="",edu="",luck="",move="",build="",san="",hp_curr="",hp_max="",mp_curr="",mp_max="",db="",attacks=[],skills=[]):

    if attacks is None:
      attacks = AttacksModel()
    if skills is None:
      skills = SkillsModel()

    self.id = id
    self.owner = owner
    self.name = name
    self.pronouns = pronouns
    self.occupation = occupation
    self.birthplace = birthplace
    self.residence = residence
    self.sex = sex
    self.age = age
    self.str = st
    self.con = con
    self.dex = dex
    self.pow = powr
    self.app = app
    self.int = i
    self.siz = siz
    self.edu = edu
    self.luck = luck
    self.move = move
    self.build = build
    self.san = san
    self.hp_curr = hp_curr
    self.hp_max = hp_max
    self.mp_curr = mp_curr
    self.mp_max = mp_max

    self.db = db
    # These might need additional objects

    self._skills = skills
    self._attacks = attacks

   

  @skills.setter
  def skills(self, val):
    if isinstance(val, SkillsModel):
      self._skills = val
    elif isinstance(val, list):
      self._skills = SkillsModel.from_dict(val)
    elif isinstance(val, dict):
      self._skills = SkillsModel.from_raw(val)


  @attacks.setter
  def attacks(self, val):
    if isinstance(val, AttacksModel):
      self._attacks = val
    elif isinstance(val, list):
      self._attacks = AttacksModel.from_dict(val)
    elif isinstance(val, dict):
      self._attacks = AttacksModel.from_raw(val)




  def from_dict(self, source: dict):
    self.set_basic_vars(source)
    self.id = source["id"]
    self.owner = source["owner"]
    
    self.skills = source["skills"]
    self.attacks = source["attacks"]
    
    return self
    

  def to_dict(self):
    return {
      "id": self.id,
      "owner": self.owner,
      "name": self.name,
      "pronouns": self.pronouns,
      "occupation": self.occupation,
      "birthplace": self.birthplace,
      "residence": self.residence,
      "sex": self.sex,
      "age": self.age,
      "str": self.str,
      "con": self.con,
      "dex": self.dex,
      "pow": self.pow,
      "app": self.app,
      "int": self.int,
      "siz": self.siz,
      "edu": self.edu,
      "luck": self.luck,
      "move": self.move,
      "build": self.build,
      "san": self.san,

      
      "hp_curr": self.hp_curr,
      "hp_max": self.hp_max,
      "mp_curr": self.mp_curr,
      "mp_max": self.mp_max,

      "db": self.db,

      "attacks": self._attacks.to_dict(),

      "skills": self._skills.to_dict()
    }
  
  def from_raw(self, raw: dict):
    """
      {name,pronouns,occupation,birthplace,residence,sex,age,str,con,dex,pow,app,int,siz,edu,luck,move,build,san,hp_curr,hp_max,mp_curr,mp_max,used_01,name_01,val_01,used_02,name_02,val_02,used_03,name_03,val_03,used_04,name_04,val_04,used_05,name_05,val_05,used_06,name_06,val_06,used_07,name_07,val_07,used_08,name_08,val_08,used_09,name_09,val_09,used_10,name_10,val_10,used_11,name_11,val_11,used_12,name_12,val_12,used_13,name_13,val_13,used_14,name_14,val_14,used_15,name_15,val_15,used_16,name_16,val_16,used_17,name_17,val_17,used_18,name_18,val_18,used_19,name_19,val_19,used_20,name_20,val_20,used_21,name_21,val_21,used_22,name_22,val_22,used_23,name_23,val_23,used_24,name_24,val_24,used_25,name_25,val_25,used_26,name_26,val_26,used_27,name_27,val_27,used_28,name_28,val_28,used_29,name_29,val_29,used_30,name_30,val_30,used_31,name_31,val_31,used_32,name_32,val_32,used_33,name_33,val_33,used_34,name_34,val_34,used_35,name_35,val_35,used_36,name_36,val_36,used_37,name_37,val_37,used_38,name_38,val_38,used_39,name_39,val_39,used_40,name_40,val_40,used_41,name_41,val_41,used_42,name_42,val_42,used_43,name_43,val_43,used_44,name_44,val_44,used_45,name_45,val_45,used_46,name_46,val_46,used_47,name_47,val_47,used_48,name_48,val_48,used_49,name_49,val_49,used_50,name_50,val_50,used_51,name_51,val_51,used_52,name_52,val_52,used_53,name_53,val_53,used_54,name_54,val_54,used_55,name_55,val_55,used_56,name_56,val_56,used_57,name_57,val_57,used_58,name_58,val_58,used_59,name_59,val_59,used_60,name_60,val_60,used_61,name_61,val_61,used_62,name_62,val_62,used_63,name_63,val_63,used_64,name_64,val_64,used_65,name_65,val_65,used_66,name_66,val_66,used_67,name_67,val_67,used_68,name_68,val_68,used_69,name_69,val_69,used_70,name_70,val_70,used_71,name_71,val_71,used_72,name_72,val_72,db,atk_name_01,atk_damage_01,atk_range_01,atk_num_attacks_01,atk_name_02,atk_damage_02,atk_range_02,atk_num_attacks_02,atk_name_03,atk_damage_03,atk_range_03,atk_num_attacks_03,atk_name_04,atk_damage_04,atk_range_04,atk_num_attacks_04,atk_name_05,atk_damage_05,atk_range_05,atk_num_attacks_05,atk_name_06,atk_damage_06,atk_range_06,atk_num_attacks_06,atk_name_07,atk_damage_07,atk_range_07,atk_num_attacks_07,atk_name_08,atk_damage_08,atk_range_08,atk_num_attacks_08,atk_name_09,atk_damage_09,atk_range_09,atk_num_attacks_09,atk_name_10,atk_damage_10,atk_range_10,atk_num_attacks_10,atk_name_11,atk_damage_11,atk_range_11,atk_num_attacks_11,atk_name_12,atk_damage_12,atk_range_12,atk_num_attacks_12,atk_name_13,atk_damage_13,atk_range_13,atk_num_attacks_13,atk_name_14,atk_damage_14,atk_range_14,atk_num_attacks_14,atk_name_15,atk_damage_15,atk_range_15,atk_num_attacks_15,atk_name_16,atk_damage_16,atk_range_16,atk_num_attacks_16}
    """
    
    self.set_basic_vars(raw)
    
    self.skills = raw
    self.attacks = raw
    
    return self

  def set_basic_vars(self, source):

    self.id = source["id"]
    self.name = source["name"]
    self.pronouns = source["pronouns"]
    self.occupation = source["occupation"]
    self.birthplace = source["birthplace"]
    self.residence = source["residence"]
    self.sex = source["sex"]
    self.age = source["age"]
    self.str = int(source["str"])
    self.con = int(source["con"])
    self.dex = int(source["dex"])
    self.pow = int(source["pow"])
    self.app = int(source["app"])
    self.int = int(source["int"])
    self.siz = int(source["siz"])
    self.edu = int(source["edu"])
    self.luck = int(source["luck"])
    self.move = int(source["move"])
    self.build = int(source["build"])
    self.san = int(source["san"])

    
    self.hp_curr = int(source["hp_curr"])
    self.hp_max = int(source["hp_max"])
    self.mp_curr = int(source["mp_curr"])
    self.mp_max = int(source["mp_max"])

    self.db = source["db"]

  def __str__(self):

    return f"""
    **Name:** {self.name}
    **Pronouns:** {self.pronouns}
    **Occupation:** {self.occupation}
    **Birthplace:** {self.birthplace}
    **Residence:** {self.residence}
    **Sex:** {self.sex} **Age:** {self.age}
    
    **Characteristics**
    ```STR: {self.str} SIZ: {self.siz}
CON: {self.con} POW: {self.pow}
DEX: {self.dex} APP: {self.app}
INT: {self.int} EDU: {self.edu}```

    Hit Points: {self.hp_curr}/{self.hp_max}
    Magic Points: {self.mp_curr}/{self.mp_max}
    Luck: {self.luck}
    Sanity: {self.san}

    """

  def __repr__(self):
    return self.to_dict()