#Function based code  for finding highest          


def if_dict(val,high):
    for m in val:
        if val[m]>high:
            high=val[m]
    return high

def if_int_float_bool(val,high):
    if(val>high):
        high = val
    return high


def if_list_tuple_set(val,high):
    for j in val:
        if(j>high):
            high = j
    return high
    
    


def find_high(x):
    highest=0
    for i in x:
        if type(x[i]) in (list,tuple,set):
            highest = if_list_tuple_set(x[i],highest)
            print("Within if_list_tuple_set",highest)
#            for j in x[i]:
#                if(j>highest):
#                    highest = j
#                    print(highest)


            
        elif type(x[i]) in (bool,int,float):
            highest = if_int_float_bool(x[i],highest)
            print("Within if_int_float_bool",highest)
            
#            if(x[i]>highest):
#               highest=x[i]
#               print(highest)
                

            
        elif type(x[i])==dict:
        
            highest = if_dict(x[i],highest)
            print("Within if_dict",highest)

    return highest
        

d = {"fl":39393.222,"ineouron":{"a":2,"b":4,"c":655},'course':{'d':10,'e':123},"xyz":11113,"zzz":[22,104323],"s":{323,543,222,22222222222}}

#,'course':{'d':10,'e':123},"xyz":993,"zzz":[22,10332],"s":{3334,543,222,22}
high = 0
high = find_high(d)

print("Highest is {}".format(high))

