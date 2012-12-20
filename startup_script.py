import sys
path = "C:\\soa\\"
if path not in sys.path:
    path.append(path)

sys.modules.clear()
import main
main.run(locals())

