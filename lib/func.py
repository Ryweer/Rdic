import sys,time,os
def word_color_print(text):
    #格式：\033[显示方式;前景色;背景色m eg；print('\033[1;31;40m')
    print('\033[1;32;40m'+text+'\033[0m')

def getBaseDic(path):
    if os.path.isfile(path) == False:
        print('The base dic is not exit!')
    elif os.path.getsize(path) == 0:
        print('Something wrong with the base dic!')
    else:
        with open(path) as file:
            baseDic_list = file.read().split('\n')
        word_color_print('Load base dic success!')
        #print(baseDic_list)
        return baseDic_list
    tmp_list = ''
    final_dic_list = []
    upper_text = ''
    if is_Name:
        #print('here')
        for char in keywords:
            if char.isupper():
                upper_text += char
    if len(birth_string_list) == 2:
        m_text = birth_string_list[0]
        d_text = birth_string_list[1]
    elif len(birth_string_list) == 3:
        y_text = birth_string_list[0]
        m_text = birth_string_list[1]
        d_text = birth_string_list[2]
    #第一次组合
    text = 'Now starting the first create.'
    sys.stdout.write(text)
    for baseDic in baseDic_list:
        final_dic_list.append(keywords+baseDic)
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.01)
    word_color_print('First creating is completed!')

def create_dic(keywords,baseDic_list,is_Name,birth_string_list):
    flag_birthday = False
    tmp_list = ''
    final_dic_list = []
    upper_text = ''#姓名首字母
    if is_Name:
        #print('here')
        for char in keywords:
            if char.isupper():
                upper_text += char
                #print(upper_text)
    if len(birth_string_list) == 2 or len(birth_string_list) == 3:
        flag_birthday = True
    text = 'Now starting the first create.'
    word_color_print(text)
    basic_create(keywords,baseDic_list,final_dic_list)
    if upper_text != '':
        is_name_create(upper_text,baseDic_list,final_dic_list)
    #birthday create:
        if flag_birthday:
            birth_create(keywords,upper_text,baseDic_list,birth_string_list,final_dic_list)
    word_color_print('First creating is completed!')
    word_color_print('Starting the second create')
    print(final_dic_list)
    
def is_name_create(upper_text,baseDic_list,final_dic_list):
    #upper_text create
    word_color_print('Detected Name strings, start a new create')
    for baseDic in baseDic_list:
        final_dic_list.append(upper_text+baseDic) #all upper_text
        final_dic_list.append(upper_text.lower()+baseDic) #all lower_text
        final_dic_list.append(upper_text[0:1]+upper_text[1:].lower()+baseDic) #first_upper text
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.01)
    #lower_text create
    #print(upper_text[0:1])
    word_color_print('\ncompleted!')

def basic_create(keywords,baseDic_list,final_dic_list):
    for baseDic in baseDic_list:
        final_dic_list.append(keywords+baseDic)
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.01)
    sys.stdout.write('\n')

def birth_create(keywords,upper_text,baseDic_list,birth_string_list,final_dic_list):
    word_color_print('Detected birthday string, starting name-birth create.')
    y_text = ''
    birth_string = []
    if len(birth_string_list) == 2:
        m_text = birth_string_list[0]
        d_text = birth_string_list[1]
    elif len(birth_string_list) == 3:
        flag_birthday = True
        y_text = birth_string_list[0]
        m_text = birth_string_list[1]
        d_text = birth_string_list[2]
    if y_text != '':
        birth_string.append(y_text+m_text+d_text)
        birth_string.append(y_text[-2:]+m_text+d_text)
    birth_string.append(m_text+d_text)
    #start create
    for birth in birth_string:
        final_dic_list.append(upper_text+birth)
        final_dic_list.append(upper_text.lower()+birth)
        final_dic_list.append(keywords+birth)
        final_dic_list.append(keywords.lower()+birth)
    print(birth_string)
