import random
import time

from faker import Faker
from .my_string_utils import generate_salt
from .my_string_utils import get_string_md5

fake = Faker()
def mock_data(i):

    padded_number_list = str(i).rjust(5, "0")
    group_id = "0"
    pid = "0"
    username = "19{}{}{}".format(padded_number_list[0], random.randint(1000, 9999), padded_number_list[1:])
    nickname = "19{}{}{}".format(padded_number_list[0], "****", padded_number_list[1:])
    salt = generate_salt(6)
    password = get_string_md5(username + salt)
    email = fake.email()
    mobile = username
    avatar = "/assets/img/avatar.png"
    level = "1"
    gender = "0"
    birthday = ""
    bio = ""
    code = generate_salt(7)
    money = "0.00"
    score = "0"
    successions = "1"
    maxsuccessions = "1"
    prevtime = int(time.time())
    logintime = int(time.time())
    loginip = fake.ipv4()
    loginfailure = "0"
    joinip = fake.ipv4()
    jointime = int(time.time())
    createtime = int(time.time())
    updatetime = int(time.time())
    token = ""
    status = "normal"
    verification = ""
    total = ""
    openid = ""
    session_key = ""

    value_str = ("({},{},\"{}\",\"{}\",\"{}\","
                 "\"{}\",\"{}\",\"{}\",\"{}\",{},"
                 "{},null,\"{}\",\"{}\",{},"
                 "{},{},{},{},{},"
                 "\"{}\",{},\"{}\",{},{},"
                 "{},null,\"{}\",null,null,"
                 "\"{}\",\"{}\")"
                 .format(group_id, pid, username, nickname, password,
                         salt, email, mobile, avatar, level,
                         gender, bio, code, money,
                         score, successions, maxsuccessions, prevtime, logintime,
                         loginip, loginfailure, joinip, jointime, createtime,
                         updatetime, status,
                         openid, session_key))
    return value_str
