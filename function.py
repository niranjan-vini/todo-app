def old ():
    with open ("day.txt","r") as file:
        todos=file.readlines()
    return todos
    
def new(me):
    with open ("day.txt","w") as file :
        file.writelines(me)