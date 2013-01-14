##########################
#### NEW? begin here! ####
####    START-UP      ####
##########################
# this will launch the whole protocol. to get an idea of the protocol structutre, look the code architecture.ppt
# 1): change mypath to your code folder
# 2) open in gephi the file. 
# 2): COPY THE SCRIPT BELOW AND PASTE IT in the gephi script-console.

import sys
import os

jars = [
    "core.jar",
    "org-gephi-algorithms.jar",
    "org-gephi-graph-api.jar",
    "org-gephi-data-attributes.jar",
    "org-gephi-data-attributes-api.jar",
    "org-gephi-visualization-api.jar",
    "org-gephi-project-api.jar",
    "org-gephi-io-importer-api.jar",
]

def addpath(path):
    if path not in sys.path:
        sys.path.append(path)

def addpathjar(jarpath):
    addpath(jarpath)
    if jarpath not in os.environ['CLASSPATH']:
        os.environ['CLASSPATH'] += ";"+jarpath

mypath="D:\\ELECTIVES\\SELF_ORGA\\new_code\\" 
#mypath = "c:\\soa\\"
addpath(mypath)

def fixpaths():
    global jars # BE KIND TO OTHERS: do not cancel out their mypath, just comment it :)
    addpath(mypath)
    #toolpath= mypath # for those who have the toolkit under the same folder
    toolpath= "C:\\Users\\MangustaMegaMastar\\Downloads\\4gephi\\gephi-0.8.1-beta.sources\\gephi-0.8.1-beta.sources\\toolkit\\gephi-toolkit\\"
    tk_path = toolpath+"gephi-toolkit\\"
    for jar in jars:
        addpathjar(tk_path+jar)
    addpathjar(toolpath+"gephi-toolkit.jar")

def startup():
    fixpaths()
    sys.modules.clear()
    print "go!"
    import main
    main.series(globals())

# then type:
startup()

def help(obj = None) :
    """
    See help
    """
    if obj == None :
        print "Python console"
        print "Available functions : "
        print dir(sys.modules[__name__])
    else :
        try :
            print obj.__doc__
        except :
            print "Object has no documentation"

#sys.path.append("C:\\Users\\MangustaMegaMastar\\Downloads\\4gephi\\gephi-0.8.1-beta.sources\\gephi-0.8.1-beta.sources\\toolkit\\gephi-toolkit.jar")
