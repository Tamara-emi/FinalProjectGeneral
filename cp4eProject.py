with open(r"C:\Users\Bridget Kwofie\OneDrive - Ashesi University\Desktop\py\earthquakes (1).txt",'r') as file:
    great = []
    major = []
    strong = []
    moderate=[]
    inc=[]
    mag=[]
    regionName = []
    region_Name = []#withour repition 
    generalList = []
    for line in file:
        line=line.split()
        regionName.append(line[7:])
        mag.append(line[1])
mag.pop(0)
regionName.pop(0)
newMag=[float(i) for i in mag]
string=''
for i in regionName:
    for b in i:
        string=string+b+' '
    region_Name.append(string)
#print(newMag)
val=[0,0,0,0,0,0]
earthDict={}
for i in region_Name:
    earthDict[i]=val
for i,j in zip(region_Name,newMag):
    if 5<=j<=5.9:
        earthDict[i][3]+=1
        earthDict[i][4]+=1
    elif 6<=j<=6.9:
        earthDict[i][2]+=1
        earthDict[i][4]+=1
    elif 7<=j<=7.9:
        earthDict[i][1]+=1
        earthDict[i][4]+=1
    elif 8<=j:
        earthDict[i][0]+=1
        earthDict[i][4]+=1
    else:
        earthDict[i][5]+=1
        earthDict[i][4]+=1

for a,b in earthDict.items():
    print(a,b)