def startup():
    import sys
    path = "D:\\ELECTIVES\\SELF_ORGA\\new_code\\"
    if path not in sys.path:
        sys.path.append(path)
    sys.modules.clear()
    import main
    print "go!"
    main.run(globals())

    
    
    
##########################
#### NEW? begin here! ####
####    START-UP      ####
##########################
# this will launch the whole protocol. to get an idea of the protocol structutre, look the code architecture.ppt
# 1): change mypath to your code folder
# 2) open in gephi the file. 
# 2): COPY THE SCRIPT BELOW AND PASTE IT in the gephi script-console.

mypath = "D:\\ELECTIVES\\SELF_ORGA\\new_code\\"  # "C:\\soa\\" 
def startup():
    import sys
    if mypath not in sys.path:
        sys.path.append(mypath)
    sys.modules.clear()
    import main
    print "go!"
    main.run(globals())
# then type:
startup()