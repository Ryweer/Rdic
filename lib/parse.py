import argparse
import sys

def cmdParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s',metavar='keystring',dest='keystring',type=str,default=None,help='The key string')
    parser.add_argument('-in',metavar='isName',dest='isName',type=bool,default=False,help='The keystring is a name or not')
    parser.add_argument('-bs',metavar='birth_str',dest='birth_str',type=str,default=None,help='If have birth-data,put it on here.(eg.2017-01-02,or 01-02)')
    parser.add_argument('-sc',metavar='socialContact',dest='socalContact',type=int,default=None,help='If you know the socal contact of target such as phone or qq number,you can figure out here')
    parser.add_argument('-e',metavar='email',dest='email',type=str,default=None,help='Set email here.(eg.test@163.com)')
    parser.add_argument('-r',metavar='referenceNum',dest='referenceNum',type=int,default=None,help='The reference data such as work ID, student ID and so on.')
    parser.add_argument('-p',metavar='passwrod',dest='password',type=str,default=None,help='Using password or old password')
    if len(sys.argv)==1:
        sys.argv.append('-h')
    
    args = parser.parse_args()
    return args
