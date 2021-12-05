from __future__ import print_function
import os.path, re, json
from googleapiclient.discovery import build 
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials


class GoogleSheets(object):
  SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
  sheet = None
  range = {"R4":"name","R6":"pronouns","R8":"occupation","AL4":"birthplace","AL6":"residence","AI8":"sex","AR8":"age","Q14":"str","Q17":"con","AA14":"dex","AA17":"pow","AK14":"app","AK17":"int","AU14":"siz","AU17":"edu","P22":"luck","Z22":"move","AJ22":"build","AP28":"san","K28":"hp_curr","P29":"hp_max","AA28":"mp_curr","AF28":"mp_max",
  #
  # The following are skill slots
  #
  "K35":"used_01","L35":"name_01","S35":"val_01",
  "K36":"used_02","L36":"name_02","S36":"val_02",
  "K37":"used_03","L37":"name_03","S37":"val_03",
  "K38":"used_04","L38":"name_04","S38":"val_04",
  "K39":"used_05","L39":"name_05","S39":"val_05",
  "K40":"used_06","L40":"name_06","S40":"val_06",
  "K41":"used_07","L41":"name_07","S41":"val_07",
  "K42":"used_08","L42":"name_08","S42":"val_08",
  "K43":"used_09","L43":"name_09","S43":"val_09",
  "K44":"used_10","L44":"name_10","S44":"val_10",
  "K45":"used_11","L45":"name_11","S45":"val_11",
  "K46":"used_12","L46":"name_12","S46":"val_12",
  "K47":"used_13","L47":"name_13","S47":"val_13",
  "K48":"used_14","L48":"name_14","S48":"val_14",
  "K49":"used_15","L49":"name_15","S49":"val_15",
  "K50":"used_16","L50":"name_16","S50":"val_16",
  "K51":"used_17","L51":"name_17","S51":"val_17",
  "K52":"used_18","L52":"name_18","S52":"val_18",
  "K53":"used_19","L53":"name_19","S53":"val_19",
  "K54":"used_20","L54":"name_20","S54":"val_20",
  "K55":"used_21","L55":"name_21","S55":"val_21",
  "K56":"used_22","L56":"name_22","S56":"val_22",
  "K57":"used_23","L57":"name_23","S57":"val_23",
  "K58":"used_24","L58":"name_24","S58":"val_24",

  "Y35":"used_25","Z35":"name_25","AG35":"val_25",
  "Y36":"used_26","Z36":"name_26","AG36":"val_26",
  "Y37":"used_27","Z37":"name_27","AG37":"val_27",
  "Y38":"used_28","Z38":"name_28","AG38":"val_28",
  "Y39":"used_29","Z39":"name_29","AG39":"val_29",
  "Y40":"used_30","Z40":"name_30","AG40":"val_30",
  "Y41":"used_31","Z41":"name_31","AG41":"val_31",
  "Y42":"used_32","Z42":"name_32","AG42":"val_32",
  "Y43":"used_33","Z43":"name_33","AG43":"val_33",
  "Y44":"used_34","Z44":"name_34","AG44":"val_34",
  "Y45":"used_35","Z45":"name_35","AG45":"val_35",
  "Y46":"used_36","Z46":"name_36","AG46":"val_36",
  "Y47":"used_37","Z47":"name_37","AG47":"val_37",
  "Y48":"used_38","Z48":"name_38","AG48":"val_38",
  "Y49":"used_39","Z49":"name_39","AG49":"val_39",
  "Y50":"used_40","Z50":"name_40","AG50":"val_40",
  "Y51":"used_41","Z51":"name_41","AG51":"val_41",
  "Y52":"used_42","Z52":"name_42","AG52":"val_42",
  "Y53":"used_43","Z53":"name_43","AG53":"val_43",
  "Y54":"used_44","Z54":"name_44","AG54":"val_44",
  "Y55":"used_45","Z55":"name_45","AG55":"val_45",
  "Y56":"used_46","Z56":"name_46","AG56":"val_46",
  "Y57":"used_47","Z57":"name_47","AG57":"val_47",
  "Y58":"used_48","Z58":"name_48","AG58":"val_48",

  "AM35":"used_49","AN35":"name_49","AU35":"val_49",
  "AM36":"used_50","AN36":"name_50","AU36":"val_50",
  "AM37":"used_51","AN37":"name_51","AU37":"val_51",
  "AM38":"used_52","AN38":"name_52","AU38":"val_52",
  "AM39":"used_53","AN39":"name_53","AU39":"val_53",
  "AM40":"used_54","AN40":"name_54","AU40":"val_54",
  "AM41":"used_55","AN41":"name_55","AU41":"val_55",
  "AM42":"used_56","AN42":"name_56","AU42":"val_56",
  "AM43":"used_57","AN43":"name_57","AU43":"val_57",
  "AM44":"used_58","AN44":"name_58","AU44":"val_58",
  "AM45":"used_59","AN45":"name_59","AU45":"val_59",
  "AM46":"used_60","AN46":"name_60","AU46":"val_60",
  "AM47":"used_61","AN47":"name_61","AU47":"val_61",
  "AM48":"used_62","AN48":"name_62","AU48":"val_62",
  "AM49":"used_63","AN49":"name_63","AU49":"val_63",
  "AM50":"used_64","AN50":"name_64","AU50":"val_64",
  "AM51":"used_65","AN51":"name_65","AU51":"val_65",
  "AM52":"used_66","AN52":"name_66","AU52":"val_66",
  "AM53":"used_67","AN53":"name_67","AU53":"val_67",
  "AM54":"used_68","AN54":"name_68","AU54":"val_68",
  "AM55":"used_69","AN55":"name_69","AU55":"val_69",
  "AM56":"used_70","AN56":"name_70","AU56":"val_70",
  "AM57":"used_71","AN57":"name_71","AU57":"val_71",
  "AM58":"used_72","AN58":"name_72","AU58":"val_72",
  #
  # Finally attack related stuff
  #
  "V70": "db",
  "L63": "atk_name_01","R63":"atk_damage_01","W63":"atk_range_01","Y63":"atk_num_attacks_01",
  "L64": "atk_name_02","R64":"atk_damage_02","W64":"atk_range_02","Y64":"atk_num_attacks_02",
  "L65": "atk_name_03","R65":"atk_damage_03","W65":"atk_range_03","Y65":"atk_num_attacks_03",
  "L66": "atk_name_04","R66":"atk_damage_04","W66":"atk_range_04","Y66":"atk_num_attacks_04",
  "L67": "atk_name_05","R67":"atk_damage_05","W67":"atk_range_05","Y67":"atk_num_attacks_05",
  "L68": "atk_name_06","R68":"atk_damage_06","W68":"atk_range_06","Y68":"atk_num_attacks_06",
  "L69": "atk_name_07","R69":"atk_damage_07","W69":"atk_range_07","Y69":"atk_num_attacks_07",

  "AD63": "atk_name_08","AJ63":"atk_damage_08","AP63":"atk_range_08","AR63":"atk_num_attacks_08",
  "AD64": "atk_name_09","AJ64":"atk_damage_09","AP64":"atk_range_09","AR64":"atk_num_attacks_09",
  "AD65": "atk_name_10","AJ65":"atk_damage_10","AP65":"atk_range_10","AR65":"atk_num_attacks_10",
  "AD66": "atk_name_11","AJ66":"atk_damage_11","AP66":"atk_range_11","AR66":"atk_num_attacks_11",
  "AD67": "atk_name_12","AJ67":"atk_damage_12","AP67":"atk_range_12","AR67":"atk_num_attacks_12",
  "AD68": "atk_name_13","AJ68":"atk_damage_13","AP68":"atk_range_13","AR68":"atk_num_attacks_13",
  "AD69": "atk_name_14","AJ69":"atk_damage_14","AP69":"atk_range_14","AR69":"atk_num_attacks_14",
  "AD70": "atk_name_15","AJ70":"atk_damage_15","AP70":"atk_range_15","AR70":"atk_num_attacks_15",
  "AD71": "atk_name_16","AJ71":"atk_damage_16","AP71":"atk_range_16","AR71":"atk_num_attacks_16",
  
  }

  def __init__(self):
    service_account = os.environ.get("GOOGLE_SERVICE_ACCOUNT")
    if service_account is not None:
      creds = Credentials.from_service_account_info( json.loads(service_account), scopes=self.SCOPES)

    service = build('sheets', 'v4', credentials=creds)
    self.sheet = service.spreadsheets()

  def get_sheet_id(self, url):
    regex = re.compile(r'/spreadsheets/d/([a-zA-Z0-9-_]+)')
    parts = regex.search(url)
    assert parts, "This isn't a valid sheet"

    return parts.group(1)
  
  def get_sheet_by_id(self, id):
    result = self.sheet.values().batchGet(spreadsheetId=id, ranges=list(self.range.keys())).execute()
    values = result.get('valueRanges', [])
    #values = result.get('values', [])

    char_dict = {}
    for value in values:
      new_key = value["range"].split("!",1)[1]
      potential_value = None
      try:
        potential_value = value["values"][0][0]
      except KeyError:
        pass
      
      char_dict[self.range[new_key]] = potential_value
    
    char_dict["id"] = id
    return char_dict