def find_cube_pairs(target):
    solutions=[]
    max_num=round(target ** (1/3)) #targ->target, ***->**

    for a in range(1,max_num+1): #ranges->range, Colon req
        for b in range(a,max_num+1): #ranges->range, Colon req
            if a**3 + b**3 == target: #targ->target, ***->**, Colon req
                solutions.append((a,b)) #sol->solutions, No semicolon req(Will still work)
    return solutions #sol->solutions


pairs=find_cube_pairs(1728) #1729->1728
print("Valid cube pairs for 1728:") #printf->print, No comma
for a,b in pairs: #pair->pairs, Colon req
    print(f"->{a}³+{b}³ = {a**3} + {b**3}= 1728") # printf->print, a*2->a**3,b*2->b**3
                
