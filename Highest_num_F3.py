#The below code finds the highest number from a dictionary

def if_str_comp():
    pass

def if_dict(val,high):
    if type(val) != dict:
        print("Boss! Enter a dictionary")
        return
    
    for m in val:
        
        if type(val[m]) in (bool,int,float):
            high = if_int_float_bool(val[m],high)

        elif type(val[m]) in (list,tuple,set):
            high = if_list_tuple_set(val[m],high)
        
        elif type(val[m]) == dict:
            high = if_dict(val[m],high)
            
        elif type(val[m]) in (str,complex):
            if_str_comp()        

    return high

def if_list_tuple_set(val,high):
    
    for j in val:
        if type(j) in (int,bool,float):
            high = if_int_float_bool(j,high)
        
        elif type(j) == dict:
            high = if_dict(j,high)

        elif type(j) in (list,tuple,set):
            high = if_list_tuple_set(j,high)
                    
        elif type(j) in (str,complex):
            if_str_comp()
            
    return high


def if_int_float_bool(val,high):
    if(val>high):
        high = val
    return high

 #d = [222,333,555555]       

d = {"fl":"39393.222","ineouron":{"a":2,"b":4,"c":{"ll":999,"ss":88837,"sss":{"383838":27727}}},'course':{'d':10,'e':123},"xyz":11113,"zzz":[22,{"sss":(22222,7373737373737)}],"s":{323,543,222,2222}}
#d = {"sss":"sss","sss":3+4j}
#,'course':{'d':10,'e':123},"xyz":993,"zzz":[22,10332],"s":{3334,543,222,22}
high = 0
high = if_dict(d,high)

print("Highest is {}".format(high))
