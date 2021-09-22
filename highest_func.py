#Enter Python code here and hit the Run button.
 

'''def if_int_float_bool(val,high):
    if(val>high):
        return val
    else:
        return high

def if_list_tuple_set(a,high):
    for i in a:
        if type(i) in (list,tuple,set):
            return if_list_tuple_set(i,high)
            
        if type(i) in (bool,int,float):
            return if_int_float_bool(i,high)
            
        if type(i)==dict:
            return if_dict(i,high)'''
            


def if_dict(val,high):
    for m in val:
        if val[m]>high:
            high=val[m]
    return high

def if_int_float_bool(val):
    global high
    if(val>high):
        return val


def if_list_tuple_set(val):
    global high
    for j in val:
        if(j>high):
            high = j
    return high
    
    


def find_high(x):
    highest=0
    for i in x:
        if type(x[i]) in (list,tuple,set):
            for j in x[i]:
                if(j>highest):
                    highest = j
                    print(highest)
            #high = if_list_tuple_set(x[i])

            
        elif type(x[i]) in (bool,int,float):
            if(x[i]>highest):
                highest=x[i]
                print(highest)
                
            #high = if_int_float_bool(x[i])

            
        elif type(x[i])==dict:
        
            highest = if_dict(x[i],highest)
            print(highest)

    return highest
        

d = {"fl":393939.222,"ineouron":{"a":2,"b":4,"c":655},'course':{'d':10,'e':123},"xyz":9911111113,"zzz":[22,10432],"s":{33343,543,222,22}}

#,'course':{'d':10,'e':123},"xyz":993,"zzz":[22,10332],"s":{3334,543,222,22}
high = 0
high = find_high(d)

print("Highest is {}".format(high))



'''
for x in d:
    if type(d[x]) in (int,float,bool):
        if(d[x]>high):
            high = d[x]
    elif type(d[x])==dict:
        for i in d[x]:
            if(d[x][i]>high):
                high = d[x][i]
    elif type(d[x]) in (set,list,tuple):
        for j in d[x]:
            if(j>high):
                high=j
'''

