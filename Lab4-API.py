#!/usr/bin/env python
# coding: utf-8

# In[2]:


from urllib import request,parse
import json

class MapQuest:
    def __init__(self,API):
        self._BASE = 'http://open.mapquestapi.com/directions/v2/route'
        self._API = API
        self._gecode1="http://www.mapquestapi.com/geocoding/v1/address?key="
        self._map="http://www.mapquestapi.com/search/v4/place?key="
    def totalDistance(self, locations: list)->float:

        distance=0
        if len(locations)>1:
            values={"key":self._API,"from":locations[0],"to":locations[1:],"unit":"m"}
            data=parse.urlencode(values,True)
            req=request.Request(self._BASE+"?"+data)
            response=request.urlopen(req)
            dict=json.loads(response.read())
            distance= dict["route"]["distance"]
   
        else:
            distance = 0
        return distance
    def totalTime(self,locations:list)->int:
        we_need=0
        a_list=[]
        hours=0
        minutes=0
        seconds=0
        final=0
        final1=0
        if len(locations)>1:
            values={"key":self._API,"from":locations[0],"to":locations[1:],"unit":"m"}
            dete=parse.urlencode(values,True)
            reqq=request.Request(self._BASE+"?"+dete)
            response=request.urlopen(reqq)
            dict=json.loads(response.read())
            we_need= dict["route"]["formattedTime"]
            a_list=we_need.split(":")
            hours=a_list[0];
            minutes=a_list[1];
            seconds=a_list[2];
            final1=float(hours)+float(minutes)/60+float(seconds)/60/60
            final=final1*3600
        else:
            final = 0
        return final
    def directions(self,locations:list)->str:
        a=[]
        final=''
        if len(locations)>1:
            values={"key":self._API,"from":locations[0],"to":locations[1:],"unit":"m"}
            data=parse.urlencode(values,True)
            req=request.Request(self._BASE+"?"+data)
            response=request.urlopen(req)
            dict=json.loads(response.read())
            legs= dict["route"]["legs"]
            for i in legs:
                for k in i:
                    if k=='maneuvers':
                        for u in i[k]:
                            for p in u:
                                if p=='narrative':
                                    a.append(u[p])
            for i in a:
                final+=i+'\n'
        else:
            final=""
        return final
        
    def pointOfInterest(self, locations: str, keyword: str, results:int)->list:
        u1="&"
        u2="&limit="
        pp="&sort=distance&"
        gecode=self._gecode1+self._API+u1+parse.urlencode([("location",locations)])
        r1=request.urlopen(gecode)
        j1=json.load(r1)
        geo1=(j1["results"][0]["locations"][0]["latLng"]["lng"],j1["results"][0]["locations"][0]["latLng"]["lat"])
        r1.close()
        new_url=self._map+self._API+pp+"location="+",".join([str(k) for k in geo1])+"&"+parse.urlencode([("q",keyword)])+u2+str(results)
        '''response=request.urlopen(new_url)
        j=json.load(response)
        l=[]
        for i in j["results"]:
            l.apppend(i["displayString"])'''
        print(new_url)
        return new_url


# In[3]:


from tkinter import *
import tkinter.ttk as ttk
'''from Lab4 import MapQuest'''
def display():
    global zipEntry
    global zipEntry1
    global resultLabel
    
    cip = zipEntry.get()
    hip = zipEntry1.get()
    a = MapQuest("kIFuehCnGttL08YdDdB7ay3JBUVYWA2I")
    u = a.pointOfInterest(hip,cip,value.get())
    
    
    resultLabel.config(text = 'Result: ' + str(u))
    
    
    
root = Tk()
root.geometry('500x400')
root.title('Searching Information')

prompt = Label(root, text = 'location: ')
prompt.grid(row = 0)
'''prompt.pack()'''
zipEntry1 = Entry(root)
zipEntry1.grid(row = 0, column = 1)
'''zipEntry1.pack()'''

prompt2 = Label(root, text = 'keyword: ')
prompt2.grid(row = 1)
'''prompt2.pack()'''

zipEntry = Entry(root)
zipEntry.grid(row = 1, column = 1)
'''zipEntry.pack()'''


value= ttk.Combobox(root,values=[5,10,15])
value.grid(row = 3, column = 1)
'''b.place(relx=0.5, rely=0.5,x=-1,y=2)'''
go = Button(root, text = 'Search', command = display)
go.grid(row = 5)
'''go.pack(side = BOTTOM)'''
resultLabel = Label(root)
'''resultLabel.pack()'''
resultLabel.grid(row = 4, column = 1)


root.mainloop()


# In[ ]:




