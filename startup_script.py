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

def fixpaths():
    global jars
    path = "c:\\soa\\"
    addpath(path)
    tk_path = path+"gephi-toolkit\\"
    for jar in jars:
        addpathjar(tk_path+jar)
    addpathjar(path+"gephi-toolkit.jar")

def startup():
    fixpaths()
    sys.modules.clear()
    print "go!"
    import main
    main.run(globals())

# then type:
startup()

