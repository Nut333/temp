name = "shelfTool"

version = "0.0.1"

build_command = False #"python {root}/install.py"

requires = [ "nshoudini"]

def commands():
    if 'HOUDINI_TOOLBAR_PATH' in list(env.keys()):
        env.HOUDINI_TOOLBAR_PATH.set(env.HOUDINI_OTLSCAN_PATH.get().replace('&', ''))
        print("houdini_path in")
    else:
        print("not")
        env.HOUDINI_TOOLBAR_PATH.append("{root};&")
                                        
        print env.HOUDINI_TOOLBAR_PATH
        
#        print(env.HOUDINI_PATH)
#    else:
#        print("no")
