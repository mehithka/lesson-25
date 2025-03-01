class Employe:
    def __init__(self):
        print('Employee created ')

    def __del__(self):
        print('Destructor called')

def Create_OBJ():
    print('making object')
    obj = Employe()
    print('fucnction end... ')
    del obj

print('calling Create_obj() function... ')
obj = Create_OBJ()
print('program end... ')