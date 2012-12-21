import sys
mypath ="D:\\ELECTIVES\\SELF_ORGA\\new_code\\" # "C:\\soa\\" 
if mypath not in sys.path:
    sys.path.append(mypath)

sys.modules.clear()
import main
main.run(locals())

