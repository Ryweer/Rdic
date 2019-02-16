import sys

def config_parse(args,keywords,is_Name_func):
    isSet_socialContact = False
    #get keywors parse
    if args.keystring:
        keywords = args.keystring
    else:
        print('Please set -s parse.')
        sys.exit()
    #make sure if the keywords is a name 
    if args.isName == True:
        is_Name_func = True
    if args.socalContact:
        isSet_socialContact = True
        social_contact = args.socalContact
    #get birth date
    if args.birth_str:
        birth_string_list = args.birth_str.split('-')
        if len(birth_string_list) == 3:
            #判断年份是否符合规定
            if len(birth_string_list[0]) == 4 and 1 <= int(birth_string_list[0][0:1]) <= 2 and 1<= int(birth_string_list[1]) <= 12 and 1<= int(birth_string_list[2]) <= 31:
                return (keywords,is_Name_func,birth_string_list)
            else:
                print('The birth_str is not in right format!')
                sys.exit()
        elif len(birth_string_list) == 2:
            #print('here')
            #没设置年份的情况
            if 1<= int(birth_string_list[0]) <= 12 and 1<= int(birth_string_list[1]) <= 31:
                #print('here')
                return (keywords,is_Name_func,birth_string_list)
            else:
                print('The birth_str is not in right format!')
                sys.exit()
        else:
            print('The birth_str is not in right format!')
            sys.exit()
    else:
        return (keywords,is_Name_func)

