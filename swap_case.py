def swap_case(s):
    slist = list(s)
    for i in range(len(slist)):
        if slist[i].islower() :
            slist[i] = slist[i].upper()
        else:
            slist[i] = slist[i].lower()
    return "".join(slist)
            
            
