#-----IMPORT A DAMN CLASS FROM THE TOOLKIT 
# the first step can be done in 2 ways:
# the long way is to follow these instructions and get lost(<-- https://wiki.gephi.org/index.php/How_to_build_the_Gephi_Toolkit )
# the short way is to exploit milombo's work and download the libs from the dropbox invitation 

# So...
# YOU SHOULD HAVE DOWNLOADED THE FILE FROM MY DROPBOX INVITATION IN YOUR MAIL>>> DO IT NOW!
# DO THAT
# NOW
#
# DONE?
# OK, NOW ADJUST THE PATH TO ACCESS THE SUBFOLDER gephi-toolkit
toolspath="C:\\Users\MangustaMegaMastar\\Downloads\\4gephi\\gephi-0.8.1-beta.sources\\gephi-0.8.1-beta.sources\\toolkit\\gephi-toolkit\\"

algopath= toolspath+"org-gephi-algorithms.jar"
graphpath= toolspath + "org-gephi-graph-api.jar"
attr_path= toolspath + "org-gephi-data-attributes-api.jar"
#attrtype_path=toolspath + " .jar"
viz_path=toolspath + "org-gephi-visualization-api.jar"
project_path=toolspath + "org-gephi-project-api.jar" 
ioimporter_path=toolspath + "org-gephi-io-importer-api.jar"

import java.io
import sys
sys.path.append(algopath)
sys.path.append(graphpath)
sys.path.append(algopath)
sys.path.append(attr_path)
sys.path.append(viz_path)
sys.path.append(project_path)

# Import single methods/interfaces as this:
from org.gephi.graph.api import GraphView
from org.gephi.algorithms.shortestpath import AbstractShortestPathAlgorithm
from org.gephi.algorithms.shortestpath  import BellmanFordShortestPathAlgorithm

#------------------------------------
# this allowed to import methods/interfaces that were PREVIOUSLY UNACCESSIBLE.
# WE NEED TO LEARN HOW TO USE THEM.
# PROBABLY MORE OBJECTS ARE NEEDED.
# IT IS NOW POSSIBLE TO DO THE SAME THAT THESE GUYS DO: http://wiki.gephi.org/index.php/Script_plugin
# BELOW AN EXAMPLE FROM GEPHI SCRIPT-PLUGIN DEVELOPERS: NOT YET WORKING
# GET INSPIRED BY IT AND MAKE IT WORKING (changing the import way as the 3 lines above)
#-----------------------------------

from org.gephi import graph.api
import org.gephi.graph.api as graph_api
import org.gephi.data.attributes.api as attributes_api
import org.gephi.data.attributes.api.AttributeType as AttributeType
import org.gephi.visualization.VizController as viz
import org.gephi.project.api as project_api
import org.gephi.io.importer.api as importer_api
import java.io

#----- STACKOVERFLOW gives 3 advices
#If you have the source for the .jar, open up the .java file containing the code you wish to utilise, and look for a line near the top that specifies the package. If you find a line that says something like package foo.bar.myJavaPackage;, then you must do one of
#import it like 
import foo.bar.myJavaPackage #, and use the contents like
obj = foo.bar.myJavaPackage.someClass #, or
#import it like 
from foo.bar import myJavaPackage #, and use the contents like 
obj = myJavaPackage.someClass #, or
#import it like 
from foo.bar.myJavaPackage import someClass #, and use it like 
obj = myClass #, but careful of name collisions using this method.
#--- OF WHICH< ONLY THE LAST WORKS FOR US:
>>> import sys
>>> sys.path.append("/var/javalib/some-thobe-package.jar") # add the jar to your path
>>> from org.thobe.somepackage import SomeClass # it's now possible to import the package
>>> some_object = SomeClass() # You can now use your java class


import os
os.chdir(toolspath)
os.curdir

"""
This file is loaded when the gephi script engine is used first (before the first user script execution)
It contains the specific gephi python api accessible from script
"""
 
 
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
 
def getGraphModel() :
    """
    getGraphModel() :
    Return the graph model of the currently displayed graph.
    """
    return gephi.getLookup().lookup(graph_api.GraphController).getModel()
 
def getAttributeModel() :
    """
    getAttributeModel() :
    Return the attribute model of the currently displayed graph
    """
    return gephi.getLookup().lookup(attributes_api.AttributeController).getModel()
 
 
#graph management
def getDirectedGraph() :
    """
    getDirectedGraph() :
    Get the currently displayed graph as a directed graph
 
    Example :
        dg = getDirectedGraph()
        #values :
        print "Nodes:", dg.getNodeCount(),"Edges: ", dg.getEdgeCount()
 
        #iterating :
        for e in dg.edges :
            print "source : ", e.getSource(), "dest:", e.getTarget()
        node2 = dg.getNode("n2") #using its id, see find_node to search with label.
 
        print "Degree:", dg.getDegree(node2)
    """
    return getGraphModel().getDirectedGraph()
 
def getGraph() :
    """
    getGraph() :
        Get the currently displayed graph as a non directed graph
 
    Example :
    dg = getDirectedGraph()
    #values :
    print "Nodes:", dg.getNodeCount(),"Edges: ", dg.getEdgeCount()
 
    #iterating :
    for e in dg.edges :
    print "source : ", e.getSource(), "dest:", e.getTarget()
    node2 = dg.getNode("n2") #using its id, see find_node to search with label.
 
    print "Degree:", dg.getDegree(node2)
    """
    return getGraphModel().getGraph()
 


#----alternative untested method
#In your case you probably want to use the path of your package to find the jar:
# yourpackage/__init__.py
import sys, os
if 'java' in sys.platform.lower():
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "your-lib.jar"))
    from jython_implementation import library
else:
    from cpython_implementation import library
#Hope that helps!