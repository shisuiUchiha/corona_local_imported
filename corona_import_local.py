import requests
import matplotlib.pyplot as plt
import numpy as np


def check_key(dick,key):
	if key in dick.keys():
		dick[key]=dick[key]+1
		return dick
	else:
		dick[key]=1
		return dick

r=requests.get("https://api.covid19india.org/raw_data.json")

data=r.json()
data_list=data["raw_data"]
imported={}
locall={}
no_data={}
for patient in data_list:
	if patient["typeoftransmission"]=="Imported":
		imported=check_key(imported,patient["detectedstate"])
	elif patient["typeoftransmission"]=="Local":
		locall=check_key(locall,patient["detectedstate"])
	else:
		no_data=check_key(no_data,patient["detectedstate"])

list_of_keys=["Maharashtra","Tamil Nadu","Delhi","Kerala","Telangana","Andhra Pradesh","Madhya Pradesh","Rajasthan","Karnataka","Uttar Pradesh"]
y_axis_import=[]
y_axis_local=[]
for keys in list_of_keys:
	y_axis_import.append(imported[keys])
print(y_axis_import)
for keys in list_of_keys:
	y_axis_local.append(locall[keys])
print(y_axis_local)
	

y_pos=np.arange(0,len(list_of_keys))
para_wid=0.2
to_be_added=[(para_wid)]*len(list_of_keys)
label_add=[(para_wid/2)]*len(list_of_keys)
print(to_be_added)
second_y_pos=np.add(y_pos,to_be_added)
label_y_pos=np.add(y_pos,label_add)
plt.bar(x=y_pos,height=y_axis_import,width=para_wid,label="Imported Cases")
plt.bar(x=second_y_pos,height=y_axis_local,width=para_wid,label="Local Transmission")
plt.xticks(ticks=label_y_pos,labels=list_of_keys,fontsize="xx-small")
plt.ylabel("Number of Cases")
plt.legend()
plt.show()
