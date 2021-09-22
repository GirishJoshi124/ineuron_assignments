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
            


high = 0

def if_dict(val):
    global high
    for m in val:
        if val[m]>high:
            return val[m]

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
    global high
    for i in x:
        if type(x[i]) in (list,tuple,set):
            high = if_list_tuple_set(x[i])

            
        elif type(x[i]) in (bool,int,float):
            high = if_int_float_bool(x[i])

            
        elif type(x[i])==dict:
            high = if_dict(x[i])

    return high
        

d = {"fl":393939.222,"ineouron":{"a":2,"b":4,"c":6555555555},'course':{'d':10,'e':123},"xyz":993,"zzz":[22,10332],\
"s":{3334,543,222,22}}



high = find_high(d)

print(high)



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

