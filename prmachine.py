#%%
import sqlite3
import math
from operator import itemgetter
import pandas as pd
import traceback
#%%
failed= []

def save_dots(result,name,pr1L,pr2L):#pr1l and pr2l can be replaced with last dot
    raw_string=r"{}".format(name)
    g=open(raw_string,"w")
    g.write('{\n"type": "FeatureCollection",\n"features": [')
    for i in range (0,len(result)):
        g.write('{\n"type": "Feature",\n"properties": {')
        g.write('"index":"');g.write(str(i));g.write('"},')
        g.write('\n"geometry": {\n"type": "Point",\n"coordinates":')
        g.write("{}\n".format(str(result[i])))
        if i<len(result)-1:g.write('  }\n      },\n')
        else: g.write('  }\n      }\n')
    g.write(' \n]}')
    g.close()
    print('file saved as {}'.format(raw_string))
def save_to_json(result,name,pr2L,pr1L):#pr1l and pr2l can be replaced with last dot
    raw_string = r"{}".format(name)
    f = open(raw_string, "w")
    f.write('{\n"type": "FeatureCollection",\n"features": [\n{\n"type": "Feature",\n"properties": {},\n"geometry": {\n"type": "LineString",\n"coordinates":[')
    for i in range(0,len(result)):
        if i == 0:
            #f.write("{},\n".format(str(pr1L)))
            pass
        else:
            if i < len(result)-1:
                f.write("{},\n".format(str(result[i])))
            else:
                f.write("{}\n".format(str(result[i])))
    #f.write("{}\n".format(str(pr2L)))
    f.write('  ]\n      }\n    }  \n]}')
    f.close()
    print('file saved as {}'.format(raw_string))
def closest(x1,y1,route):
    listx = (x[0] for x in route)# list of all the x values
    listy = (x[1] for x in route)# list of all the y values
    distance = list(math.dist((x[0],x[1]),(x1,y1)) for x in route)# creates list of all the distcance values
    min_value = min(distance)# find the smallest distance value
    return distance.index(min_value)# find the index of the smallest distance
def troncon(route,prdeb,prfin,pr,absfin,absdeb):
    plus = absfin
    select=route
    PR=pr
    start_dist=[]
    result = []; extra =[]; minus =[]
    #print("pr deb = "+str(prdeb));print("pr fin = "+str(prfin))
    pr1=PR[prdeb];pr1x=pr1[0];pr1y=pr1[1];#print("pr1y: {}, pr1x: {}".format(pr1y,pr1x))# x & y coordinates of start pr
    pr2=PR[prfin];pr2x=pr2[0];pr2y=pr2[1];#print("pr2y: {}, pr2x: {}".format(pr2y,pr2x))# x & y coordinates of end pr
    start_index=closest(pr1x,pr1y,route);#print("closest1: {}".format(start_index))# index of the dot closest to the start pr
    end_index=closest(pr2x,pr2y,route);#print("closest2: {}".format(end_index))# index of the dot closest to the further pr
    select2=(select[start_index:end_index])# create selection of all the values in between start and and pr
    i=0
    select3=[]
    #getting out of range of select
    while plus > 0 and (i+end_index+1<len(select)-1):
            plus -= math.dist(select[end_index+i],select[end_index+i+1])
            extra.append(select[end_index+i])
            i+=1

    select3= select2+extra
    j=0

    while j<len(select3)-1 and absdeb > 0:
        absdeb-=math.dist(select3[j],select3[j+1])
        j +=1
    select4 = select3[j:]

    """
    j=0
    while absdeb>0:
        absdeb -= math.dist(select[start_index+i],select[start_index+i+1])
        j+=1
    if j != 0 and j-1<len(select):
        select3=select[j-1:]
    """
    return select4
#%%
df=pd.read_excel(r'D:\Documents\Ginger\ProjetPR\Python\autopy\input\input.xlsx',sheet_name=0)
df.columns
#%%
df=df[['Axe', 'Sens', 'PR_Deb', 'PR_Fin', 'Abs_deb', 'Abs_fin']]
df=df.dropna()

df["PR_Deb"]=df["PR_Deb"].astype(int)
df["PR_Fin"]=df["PR_Fin"].astype(int)
df["Abs_deb"]=df["Abs_deb"].astype(int)
df["Abs_fin"]=df["Abs_fin"].astype(int)

#%%

for i in range(0,len(df.index)):
    try:
        connection = sqlite3.connect(r"D:\Documents\Ginger\ProjetPR\DB\Roads.db")#create connection
        cursor=connection.cursor()# in charge of communication with database
        if len (df.at[i,'Axe']) == 2:
            rte=df.at[i,'Axe'][:1]+"000"+df.at[i,'Axe'][1:]
        if len (df.at[i,'Axe']) == 3:
            rte=df.at[i,'Axe'][:1]+"00"+df.at[i,'Axe'][1:]
        if len (df.at[i,'Axe']) == 4:
            rte=df.at[i,'Axe'][:1]+"0"+df.at[i,'Axe'][1:]
        #print(rte)
        if int(df.at[i,'Sens'])==1: sens="D"
        elif int(df.at[i,'Sens'])==2: sens="G"

        cursor.execute("SELECT x,y,pr from T_PR WHERE route='{}' and cote='{}' ORDER BY cumul".format(rte,sens))
        PR=cursor.fetchall()
        route=pd.read_sql_query('SELECT * FROM vertex WHERE route="{}" and portee="{}"'.format(rte,sens),connection)

        pr_deb=str(df.at[i,'PR_Deb'])
        #print("Pr_deb: "+str(pr_deb))
        pr_fin=df.at[i,'PR_Fin']
        if sens == 'G':sensl = "2"
        elif sens == "D":sensl = "1"
        absdeb=df.at[i,'Abs_deb']; absfin=df.at[i,'Abs_fin']
        file_name="RTE{}_S{}_PRD{}absd{}_PRF{}absf{}".format(rte,sensl,pr_deb,absdeb,pr_fin,absfin)

        #==================================================
        route["vertex_ind"]=route["vertex_ind"].astype(int)
        route.sort_values(by="vertex_ind", ascending=True, inplace=True)

        route["list1"]=route[['x','y']].apply(tuple,axis=1)
        lisrte=route[['x','y']].values.tolist()# print the values directly to list so as to keep the brackets
        #find index of strings
        names = list(str(x[2]).strip() for x in PR)#create a seperate list to choose start pr and end pr number()

        pr_deb_index =names.index("{}".format(str(pr_deb)));#print("STARTING PR INDEX: "+str(pr_deb_index))# find the index of starting pr
        pr_fin_index =names.index("{}".format(str(pr_fin)));#print("ENDING PR INDEX: "+str(pr_fin_index))# find the index of ending pr
        #if (absdeb > 1000): pr_deb_index +=1
        #if (absfin > 1000): pr_deb_index +=1
        pr1=PR[pr_deb_index];pr1x=pr1[0];pr1y=pr1[1];#print("pr1y: {}, pr1x: {}".format(pr1y,pr1x))# x & y coordinates of start pr
        pr2=PR[pr_fin_index];pr2x=pr2[0];pr2y=pr2[1];#print("pr2y: {}, pr2x: {}".format(pr2y,pr2x))# x & y coordinates of end pr
        pr1L=[pr1x,pr1y]; pr2L=[pr2x,pr2y]
        #print(pr1L);print(pr2L)
        # find index of starting and ending pr
        result=troncon(lisrte,pr_deb_index,pr_fin_index,PR,absfin,absdeb)

        # order select by distance to starting dot at index [closest]
        a = r"D:\Documents\Ginger\ProjetPR\Python\autopy\OUTPUT\{}.json".format(file_name)
        save_to_json(result,a,pr2L,pr1L)
        """
        if input("==> CREATE DOT FILE [Y/N]: ")=="Y":
            a =r"D:\Documents\Ginger\ProjetPR\Python\autopy\OUTPUT\PTS_{}.json".format(file_name)
            save_dots(result,a,pr1L,pr2L)
    """
        connection.close()
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        failed.append(file_name)

print("{} roads where not able to be traced".format(str(len(failed))))
print("failed to compute these roads: ", failed)
exit()
