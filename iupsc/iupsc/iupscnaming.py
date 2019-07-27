import re
from . import opengl_demo
#2,3-methylebromo propane
def devide(s):
    substute =[]
    mainchain=[]
    bonding =[]
    no_substistute=0
    chemical_substitute_prefix =['methyl','bromo','cloro']
    chemical_main_chaine =['meth','eth','prop','but','pent','hex','hept','oct','non','dec']
    chemiacl_main_sufix =('ane','ene','yne')
    chemical_list = s.split()
    for x in chemical_substitute_prefix:
        y = re.search(x ,chemical_list[0])
        if y :
            val = y.string[y.span()[0]:y.span()[1]]
            substute.append((val, chemical_list[0][no_substistute]))
            no_substistute+=2
    for x in chemical_main_chaine:
        y = re.search(x ,chemical_list[1])
        if y :
            val = y.string[y.span()[0]:y.span()[1]]
            mainchain.append((val, chemical_main_chaine.index(val)+1))
    
   

    for x in chemiacl_main_sufix[1:]:
        y = re.search(x ,chemical_list[1])
        if y :
            print
            val = y.string[y.span()[0]:y.span()[1]]
            bonding.append((val, chemical_list[1][y.span()[0]-2]))
    
    dic ={'C_N':mainchain,'substute':substute,'bond':bonding,'Name':s}
    return dic

def callbridge(s):
    opengl_demo.main(devide(s))
    print("In call bridge")
    return 