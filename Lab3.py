#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Assignment:
    def __init__(self,description,score,total):
        self._description = description
        self._score=score
        self._total=total
        
    def getDescription(self)->str:
        return self._description
    
    def getScore(self)->float: 
        return self._score
    
    def getTotal(self)->float:
        return self._total
    
    def changeScore(self,score:float):
        self._score=score
        




class CategoryAssignment(Assignment):
    def __init__(self,description,category,score,total): 
        Assignment.__init__(self,description,score,total)
        self._category = category
        
    def getCategory(self)->str:
        return self._category
    
    
    





class Student:
    def __init__(self,integer):
        self._Id=integer
        self.assignment=[]
        
    def getId(self)->int:
        return self._Id
    
    def getScore(self,assignmentName:str)->float:
        for i in self.assignment:
            if i._description == assignmentName:
                return i._score
            else:
                continue
            
    def getScores(self)->list:
        return self.assignment
    
    def addAssignment(self,score: Assignment): 
        self.assignment.append(score)
    
    def changeScore(self,assignmentName: str, score: float):
        for b in self.assignment:
            if b._description == assignmentName:
                b._score = score
            else:
                continue
    def removeScore(self,assignmentName: str):
        for k in self.assignment:
            if k._description == assignmentName:
                self.assignment.remove(k)
            else:
                continue
        
        
        
        
        
        




class Gradebook:
    def __init__(self):
        self.s=[]
    def addStudent(self,student: Student):
        self.s.append(student)
    def dropStudent(self, id: int): 
        for i in self.s:
            if i.getId()==id:
                self.s.remove(i)
    def search(self,id:int)->Student:
        for b in self.s:
            if b.getId()==id:
                return b
    def addAssignment(self,id: int, score: Assignment):
        for c in self.s:
            if c.getId()==id:
                for i,b in enumerate(c.assignment):
                    if score._description == b.getDescription():
                        c.assignment[i]=score
                        return
                c.assignment.append(score)
                
        





class TotalPointsGradebook(Gradebook):
    def __init__(self):
        Gradebook.__init__(self)
    def writeGradebookRecord(self,id: int, fileName: str):
        points=0
        total=0
        outFile=open(fileName,'w')
        for a in self.s:
            if a.getId()==id:
                outFile.write(str(id)+'\n')
                for k in a.assignment:
                    outFile.write('%s\n'%k._description)
                    outFile.write('%d/%d\n'%(k._score,k._total))
                    points+=k._score
                    total+=k._total
                outFile.write('Total: %d/%d\n'%(points,total))
                outFile.write('Percentage: '+str((points/total)*100))
                outFile.close()
                return
        outFile.write('Student Not Found')
        outFile.close()
        
    def classAverage(self)->float:
        points=0
        total=0
        final=0
        for i in self.s:
            for a in i.assignment:
                points+=a._score
                total+=a._total
        
        final=(points/total)*100
        return final
    
    
    
    
    
    
    
    
    
    



class CategoryGradebook(Gradebook):
    def __init__(self):
        Gradebook.__init__(self)
        self.f={}
    def addCategory(self,description: str, weight: float):
        self.f[description]=weight
        
    def isBalanced(self)->bool:
        final=''
        percent=0
        for k in self.f:
            percent+=self.f[k]
        if percent==100:
            final=True
        else:
            final=False
        return final
    
    def writeGradebookRecord(self,id: int, fileName: str):
        lab=0
        points=0
        total=0
        outFile=open(fileName,'w')
        for a in self.s:
            if a.getId()==id:
                outFile.write(str(id)+'\n')
                for k in a.assignment:
                    outFile.write(str(k.getCategory())+': '+str(k.getDescription())+'\n')
    
                    outFile.write('%d/%d\n'%(k.getScore(),k.getTotal()))
        for a in self.s:
            if a.getId()==id:
                for key in self.f.keys():
                    points=0
                    total=0
                    for b in a.assignment:
                        if b.getCategory()==key:
                            points+=b.getScore()
                            total+=b.getTotal()
                    lab+=points/total*self.f[key]
                
                    outFile.write(str(key)+': '+str(points/total*100)+'\n')
                outFile.write('Percentage: '+str(lab))
                outFile.close()
                return
        outFile.write('Student Not Found')
        outFile.close()
        
    def classAverage(self)->float:
        final=0
        final2=0
        for i in self.s:
            for b in self.f:
                points=0
                total=0
                for k in i.assignment:
                    if k.getCategory()==b:
                        points+=k.getScore()
                        total+=k.getTotal()
                final+=points/total*self.f[b]
            
        final2=final/len(self.s)
        return final2


# In[ ]:




