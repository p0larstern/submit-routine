import sys
print('count:',len(sys.argv))
print('type:',type(sys.argv))
for arg in sys.argv:
    print("argument",arg)