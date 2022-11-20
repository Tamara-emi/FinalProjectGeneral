from collections import OrderedDict
great,major,strong,moderate,inc,regionName,mag,region_Name=[],[],[],[],[],[],[],[]
with open(r"C:\Users\Bridget Kwofie\OneDrive - Ashesi University\Desktop\py\earthquakes (1).txt",'r') as file:
    for line in file:
        line=line.split()
        regionName.append(line[7:])
        mag.append(line[1])
mag.pop(0)
regionName.pop(0)
newMag=[float(i) for i in mag]
for i in regionName:
    string=' '.join(f for f in i)
    region_Name.append(string)
earthDict={}
for i in region_Name:
    if i not in earthDict:
        earthDict[i]=[0]*6
for i,j in zip(region_Name,newMag):
    if 5<=j<=5.9:
        earthDict[i][1]+=1
        earthDict[i][5]+=1
    elif 6<=j<=6.9:
        earthDict[i][2]+=1
        earthDict[i][5]+=1
    elif 7<=j<=7.9:
        earthDict[i][3]+=1
        earthDict[i][5]+=1
    elif 8<=j:
        earthDict[i][4]+=1
        earthDict[i][5]+=1
    else:
        earthDict[i][0]+=1
        earthDict[i][5]+=1
earthDict=OrderedDict(sorted(earthquake.items()))




for a,b in earthDict.items():
    print(f"{a} {b})
          
names,inconsequential,moderate,strong,major,great,overall=[],[],[],[],[],[],[]
for i,j in earthDict.items():
    names.append(i)
    for a,b,c,d,e,f in j:
          inconsequential.append(a)
          moderate.append(b)
          strong.append(c)
          major.append(d)
          great.append(e)
          overall.append(f)         
