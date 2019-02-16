import os
import string
import sys
import argparse
import time

from lib.parse import cmdParser
from lib.configParse import config_parse
from lib.func import create_dic
from lib.func import getBaseDic
from lib.func import word_color_print


if __name__ == '__main__':
    args = cmdParser()
    keywords = ""
    is_Name = False
    birth_string_list = config_parse(args,keywords,is_Name)
    keywords = birth_string_list[0]
    if not keywords:
        exit()
    is_Name = birth_string_list[1]
    if len(birth_string_list) == 3:
        birth_string_list = birth_string_list[2]
    else:
        birth_string_list = []
    #程序启动，加载基础字典。
    final_dic_list = []
    Path_baseDic = os.getcwd()+'/'+'baseDic.txt'
    word_color_print('Start get base dic....')
    baseDic_list = getBaseDic(Path_baseDic)
    create_dic(keywords,baseDic_list,is_Name,birth_string_list)
    #获取关键词成功，开始生成字典，执行字段拼接    
