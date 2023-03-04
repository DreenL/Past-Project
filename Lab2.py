#!/usr/bin/env python
# coding: utf-8

# In[1]:


def validWord(word:str)-> bool:
    value=0;
    word = word.lower();
    valid_characters = ['a','e','i','o','u','p','k','h','l','m','n','w',"'",' '];
    for character in word:
        if character in valid_characters:
            value+=1
        else:
            value=value
    answer = value==len(word);
    return answer





def individual_vowel(two:str)->str:
    list2 = ['p', 'k', 'h', 'l','m','n' ]
    one='';  
    if two== ' ' or two== "'":
        if two == " ":
            one=' ';
        else:
            one="'";
    elif two!= ' ' and two!= "'":
        if two =='a':
            one = 'ah-';
        elif two =='e':
            one = 'eh-';
        elif two =='i':
            one = 'ee-';
        elif two =='o':
            one = 'oh-';
        elif two =='u':
            one = 'oo-';
        elif two in list2:
            one=two
        elif two =='w':
            one='w'
    return one
            
         
            




def double_vowel(two)->str:
    if two =='ai':
        two='eye-';
    elif two =='ae':
        two='eye-';
    elif two =='ao':
        two='ow-';
    elif two =='au':
        two='ow-';
    elif two =='ei':
        two='ay-';
    elif two =='eu':
        two='eh-oo-';
    elif two =='iu':
        two='ew-';
    elif two =='oi':
        two='oy-';
    elif two =='ou':
        two='ow-';
    elif two =='ui':
        two='ooey-';
    return two
    





def pronunciate(phrase:str) -> str:
    list_vowelG=['ai','ae','ao','au','ei','eu','iu','oi','ou','ui'];
    list_delete=[]
    list_delete2=[];
    phrase=phrase.lower();
    list1=list(phrase);
    list2=list(phrase);
    phrase1='';
    list_end=[];
    k=0;
    if len(phrase)>1:
        while k <(len(list1)-1):
            connect =list1[k]+list1[k+1];
            if 'w' not in connect:
                if connect in list_vowelG:
                    list1[k] = double_vowel(connect);
                    list_delete.append(k+1);
                    k+=2
                    if k==len(list1)-1:
                        put_in = list1[k];
                        add_value = individual_vowel(put_in);
                        list1[k]=add_value
                    else:
                        k=k;
                
                else:
                    that_one=list1[k];
                    list1[k]=individual_vowel(that_one)
                    k+=1
                    if k==len(list1)-1:
                        put_in = list1[k];
                        add_value = individual_vowel(put_in);
                        list1[k]=add_value
                        k+=1
                    else:
                        k=k;
                
            else:
                if k==0 and connect[0]=='w':
                    list1[k]='w';
                    k+=1
                
                elif connect[0]!='w' and connect[1]=='w':
                    that_one=list1[k];
                    list1[k]=individual_vowel(that_one);
                    k+=1
                    if k==len(list1)-1:
                        put_in = list1[k];
                        add_value = individual_vowel(put_in);
                        list1[k]=add_value
                        k+=1
                    else:
                        k=k;
                
                elif k>=1 and connect[0]=='w':
                    that_value = list2[k-1]
                    if that_value=='a':
                        list1[k]='w';
                    elif that_value=='i' or that_value=='e':
                        list1[k]='v';
                    elif that_value=='u' or that_value=='o':
                        list1[k]='w';
                    elif that_value==' ' or that_value=="'":
                        list1[k]='w'
                    else:
                        list1[k]='w'
                    k+=1
                    if k==len(list1)-1:
                        put_in = list1[k];
                        add_value = individual_vowel(put_in);
                        list1[k]=add_value
                        k+=1
                    else:
                        k=k;
    
                
        for j in sorted(list_delete, reverse=True):
            del(list1[j])
        phrase1="".join(list1)
        list3=list(phrase1.capitalize())
        for b in range(len(list3)):
            if list3[b] == ' ':
                list3[b+1]=list3[b+1].upper();
        phrase="".join(list3)
        list4= list(phrase);
        for l in range(len(list4)):
            if list4[l]=='-':
                if l<len(list4)-1:
                    if list4[l+1]==' ' or list4[l+1]=="'":
                        list_delete2.append(l)
                else:
                    list_delete2.append(l)
        for c in sorted(list_delete2, reverse=True):
            del(list4[c])
        phrase="".join(list4)
    else:
        phrase=individual_vowel(phrase)
        list_end = list(phrase)
        for q in range(len(list_end)):
            if list_end[q]=="-":
                del(list_end[q])
        phrase="".join(list_end)
        phrase=phrase.capitalize()
    return phrase
        
        
        
    




def createGuide(inputFile:str, outputFile:str):
    word_list=[];
    word_need='';
    wrong_word='';
    input_list=[];
    one='';
    two=[];
    ccc=[];
    cc='';
    two=[]
    new=[]
    put_in=[]
    y_final=[]
    y_final2=[]
    list_end=[];
    try:
        infile = open(inputFile, 'r')
        outfile = open(outputFile, 'w')
        line2=infile.readlines()
        for j in line2:
            two.append(j.strip())
        for i in range(len(two)):
            two[i]=two[i].split()
        for k in range(len(two)):
            for p in range(len(two[k])):
                that_one=((two[k])[p]).lower()
                if that_one[-1]==",":
                    that_one2=that_one[:-1];
                    if validWord(that_one2)==True:
                        that_put = pronunciate(that_one2)+",";
                        (two[k])[p]=that_put;
                    else:
                        (two[k])[p]=''+'"'+that_one2+'"'+",";
                elif that_one[-1]==".":
                    that_one2=that_one[:-1];
                    if validWord(that_one2)==True:
                        that_put = pronunciate(that_one2)+".";
                        (two[k])[p]=that_put;
                    else:
                        (two[k])[p]=''+'"'+that_one2+'"'+".";
                
                else:
                    if validWord(that_one)==True:
                        that_put = pronunciate(that_one);
                        (two[k])[p]=that_put;
                    else:
                        (two[k])[p]=''+'"'+that_one+'"';
                
        for q in range(len(two)):
            for s in range(len(two[q])):
                (two[q])[s]=(two[q])[s]+" ";
        for u in range(len(two)):
            y= "".join(two[u])
            y_final.append(y)
        for x in y_final:
            list_end=list(x);
            del(list_end[-1])
            end="".join(list_end)
            y_final2.append(end)
        
        for num in y_final2:            
            outfile.write(num+'\n')        
        infile.close()        
        outfile.close()
    except IOError:        
        print("That file does not exist")
    except ValueError:        
        print("That is a not a valid number")


# In[ ]:




