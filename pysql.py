import sqlite3
import math
from operator import itemgetter
import pandas as pd
connection = sqlite3.connect(r"D:\Documents\Ginger\ProjetPR\DB\Roads.db")#create connaction
cursor=connection.cursor()# in charge of communication with database
def save_dots(result,name,pr1L,pr2L):
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
def save_to_json(result,name,pr2L,pr1L):
    raw_string = r"{}".format(name)
    f = open(raw_string, "w")
    f.write('{\n"type": "FeatureCollection",\n"features": [\n{\n"type": "Feature",\n"properties": {},\n"geometry": {\n"type": "LineString",\n"coordinates":[')
    for i in range(0,len(result)):
        if i == 0:
            f.write("{},\n".format(str(pr1L)))
        else:
            f.write("{},\n".format(str(result[i])))
    f.write("{}\n".format(str(pr2L)))
    f.write('  ]\n      }\n    }  \n]}')
    f.close()
    print('file saved as {}'.format(raw_string))
def closest(x1,y1,route):
    listx = (x[0] for x in route)# list of all the x values
    listy = (x[1] for x in route)# list of all the y values
    distance = list(math.dist((x[0],x[1]),(x1,y1)) for x in route)# creates list of all the distcance values
    min_value = min(distance)# find the smallest distance value
    return distance.index(min_value)# find the index of the smallest distance
def troncon(route,prdeb,prfin,pr):
    select=route
    PR=pr
    start_dist=[]
    result = []
    print("pr deb = "+str(prdeb));print("pr fin = "+str(prfin))
    pr1=PR[prdeb];pr1x=pr1[0];pr1y=pr1[1];print("pr1y: {}, pr1x: {}".format(pr1y,pr1x))# x & y coordinates of start pr
    pr2=PR[prfin];pr2x=pr2[0];pr2y=pr2[1];print("pr2y: {}, pr2x: {}".format(pr2y,pr2x))# x & y coordinates of end pr
    start_index=closest(pr1x,pr1y,route);print("closest1: {}".format(start_index))# index of the dot closest to the start pr
    end_index=closest(pr2x,pr2y,route);print("closest2: {}".format(end_index))# index of the dot closest to the further pr
    select=(select[start_index:end_index])# create selection of all the values in between start and and pr
    return select

rte=input('==> ROUTE: ')
sens=input('==> SENS [G/D]: ')
cursor.execute("SELECT x,y,pr from T_PR WHERE route='{}' and cote='{}' ORDER BY cumul".format(rte,sens))
PR=cursor.fetchall()
route=pd.read_sql_query('SELECT * FROM vertex WHERE route="{}" and portee="{}"'.format(rte,sens),connection)
pr_deb=input('==> choose starting pr: ')
pr_fin=input('==> choose ending pr: ')
if sens == 'G':sensl = "2"
elif sens == "D":sensl = "1"
file_name="RTE{}_S{}_PRD{}_PRF{}".format(rte,sensl,pr_deb,pr_fin)
connection.close()
#==================================================
route["vertex_ind"]=route["vertex_ind"].astype(int)
route.sort_values(by="vertex_ind", ascending=True, inplace=True)
route["list1"]=route[['x','y']].apply(tuple,axis=1)
lisrte=route[['x','y']].values.tolist()# print the values directly to list so as to keep the brackets
#find index of strings

names = list(str(x[2]).strip() for x in PR)#create a seperate list to choose start pr and end pr number()
pr_deb_index=names.index("{}".format(str(pr_deb)));print("STARTING PR INDEX: "+str(pr_deb_index))# find the index of starting pr
pr_fin_index=names.index("{}".format(str(pr_fin)));print("ENDING PR INDEX: "+str(pr_fin_index))# find the index of ending pr

pr1=PR[pr_deb_index];pr1x=pr1[0];pr1y=pr1[1];print("pr1y: {}, pr1x: {}".format(pr1y,pr1x))# x & y coordinates of start pr
pr2=PR[pr_fin_index];pr2x=pr2[0];pr2y=pr2[1];print("pr2y: {}, pr2x: {}".format(pr2y,pr2x))# x & y coordinates of end pr
pr1L=[pr1x,pr1y]; pr2L=[pr2x,pr2y]
print(pr1L);print(pr2L)
# find index of starting and ending pr
result=troncon(lisrte,pr_deb_index,pr_fin_index,PR)
# order select by distance to starting dot at index [closest]
a = r"D:\Documents\Ginger\ProjetPR\Qgis\Input\Ausculation\{}.json".format(file_name)
save_to_json(result,a,pr2L,pr1L)
if input("==> CREATE DOT FILE [Y/N]: ")=="Y":
    a =r"D:\Documents\Ginger\ProjetPR\Qgis\Input\Ausculation\PTS_{}.json".format(file_name)
    save_dots(result,a,pr1L,pr2L)
exit()
