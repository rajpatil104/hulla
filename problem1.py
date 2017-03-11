
adfafafdafasf
def copy():
    global tmp
    tmp = []
    f0tmp = [["","",""],["","",""],["","",""]]
    f1tmp = [["","",""],["","",""],["","",""]]
    f2tmp = [["","",""],["","",""],["","",""]]
    f3tmp = [["","",""],["","",""],["","",""]]
    f4tmp = [["","",""],["","",""],["","",""]]
    f5tmp = [["","",""],["","",""],["","",""]]
    
    
    for i in range(0,3):
        for j in range(0,3):
            f0tmp[i][j]=faces[0][i][j]
            tmp.append(f0tmp)
            f1tmp[i][j]=faces[1][i][j]
            tmp.append(f1tmp)
            f2tmp[i][j]=faces[2][i][j]
            tmp.append(f2tmp)
            f3tmp[i][j]=faces[3][i][j]
            tmp.append(f3tmp)
            f4tmp[i][j]=faces[4][i][j]
            tmp.append(f4tmp)
            f5tmp[i][j]=faces[5][i][j]
            tmp.append(f5tmp)

def makecube():
    global faces
    faces = []
    
    f0=[["a","a","a"],
        ["a","a","a"],
        ["a","a","a"]]
    f1=[["b","b","b"],
        ["b","b","b"],
        ["b","b","b"]]
    f2=[["c","c","c"],
        ["c","c","c"],
        ["c","c","c"]]
    f3=[["d","d","d"],
        ["d","d","d"],
        ["d","d","d"]]
    f4=[["e","e","e"],
        ["e","e","e"],
        ["e","e","e"]]
    f5=[["f","f","f"],
        ["f","f","f"],
        ["f","f","f"]]

    faces.append(f0)
    faces.append(f1)
    faces.append(f2)
    faces.append(f3)
    faces.append(f4)
    faces.append(f5)
    
    
    

def anticlock(a):
    copy()
    for i in range(0,3):
        for j in range(0,3):
            faces[a][i][j]=tmp[a][j][(2*i+2)%3]

def u():
    copy()
    faces[0][0] = tmp[2][0]
    faces[4][0] = tmp[0][0]
    faces[5][0] = tmp[4][0]
    faces[2][0] = tmp[5][0]
    anticlock(1)
    printcube()
def b():
    copy()
    faces[0][2] = tmp[2][2]
    faces[4][2] = tmp[0][2]
    faces[5][2] = tmp[4][2]
    faces[2][2] = tmp[5][2]
    anticlock(3)
    anticlock(3)
    anticlock(3)
    printcube()
    
def r():
    copy()
    for i in range(0,3):
        faces[1][i][2]=tmp[0][i][2]
    for i in range(0,3):
        faces[0][i][2]=tmp[3][i][2]
    for i in range(0,3):
        faces[5][i][0]=tmp[1][(2*i+2)%3][2]
    for i in range(0,3):
        faces[3][i][2]=tmp[5][(2*i+2)%3][0]
    anticlock(4)
    anticlock(4)
    anticlock(4)
    printcube()

def l():
    copy()
    for i in range(0,3):
        faces[1][i][0]=tmp[0][i][0]
    for i in range(0,3):
        faces[0][i][0]=tmp[3][i][0]
    for i in range(0,3):
        faces[5][i][2]=tmp[1][(2*i+2)%3][0]
    for i in range(0,3):
        faces[3][i][0]=tmp[5][(2*i+2)%3][2]
    anticlock(2)
    printcube()

def printcube():
    for i in range(0,3):
        print("   "+str(faces[1][i][0])+str(faces[1][i][1])+str(faces[1][i][2])+"      ")
    for i in range(0,3):
        print(str(faces[2][i][0])+str(faces[2][i][1])+str(faces[2][i][2])+str(faces[0][i][0])+str(faces[0][i][1])+str(faces[0][i][2])+str(faces[4][i][0])+str(faces[4][i][1])+str(faces[4][i][2])+str(faces[5][i][0])+str(faces[5][i][1])+str(faces[5][i][2]))
    for i in range(0,3):
        print("   "+str(faces[3][i][0])+str(faces[3][i][1])+str(faces[3][i][2])+"      ")
makecube()


printcube()





            
        
    
