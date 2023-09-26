location = input('Nhap vi tri: ') #A (trái ) hoặc B (phải)
status = input('Nhap trang thai: ') #Dirty or Clean

def Reflex_Vacuum_Agent(location, status):
    if status == 'Dirty':
        print('Suck')
    elif location == 'A':
        print('Right')
    elif location == 'B':
        print('Left')
    else:
        print('End')

Reflex_Vacuum_Agent(location, status)