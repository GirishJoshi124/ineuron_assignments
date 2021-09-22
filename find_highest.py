d = {"ineouron":{"a":2,"b":4,"c":6},'course':{'d':10,'e':123},"xyz":993,"zzz":[22,10332],"s":{3334,543,222,22},"fl":393939.222}
high = 0
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
        
print(high)
print("s")
