def startup():
    import sys
    path = "C:\\soa\\"
    if path not in sys.path:
        sys.path.append(path)
    sys.modules.clear()
    import main
    print "go!"
    main.run(globals())
