from collections import Counter
t = int(input())
 
for _ in range(t):
    werq = list(input().strip())
    hbre_qal = list(input().strip())
    sem = []
    impossible = False
    c_were = Counter(werq)
    c_hbre = Counter(hbre_qal)
    for i in range(len(werq)):
        if c_were[werq[i]] > c_hbre[werq[i]]:
            impossible = True
            break
        else:
            impossible = False
 
    if impossible:
            print("Impossible")
            continue
 
    sem = hbre_qal
 
    for i in werq:
        if i in sem:
            sem.remove(i)
        
    sem.sort()
    hbre_qal = []
    werq_pointer = 0
    sem_pointer = 0
 
    while werq_pointer < len(werq) and sem_pointer < len(sem):
        if werq[werq_pointer] > sem[sem_pointer]:
            hbre_qal.append(sem[sem_pointer])
            sem_pointer += 1
        else:
            hbre_qal.append(werq[werq_pointer])
            werq_pointer += 1
 
    if sem_pointer < len(sem):
        hbre_qal.extend(sem[sem_pointer:])
    if werq_pointer < len(werq):
        hbre_qal.extend(werq[werq_pointer:])
    
    print("".join(hbre_qal))
