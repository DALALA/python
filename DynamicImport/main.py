'''
Created on 2014/2/12

@author: Robert
'''
import sys
if __name__ == '__main__':
    print sys.argv
    modules = []
    for module in sys.argv:
        try:
            modules.append(__import__(module, globals(), locals(), [], -1))
        except ImportError:
            continue
    print len(modules)
    for module in modules:
        print module
        module.func()
        
    pass