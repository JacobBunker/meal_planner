import random

f = open('meals.txt', 'r')
o = f.read()
f.close()

o1 = o.split('\n')

meals_main = []
meals_side = []

for l in o1:
    o2 = l.split(',')
    i = int(o2[1].strip())
    if(i == 0):
        meals_side.append([o2[0], i])
    else:
        meals_main.append([o2[0], i])

#print(meals_main)
#print(meals_side)

print("generating random meal plan...")

main = []
side = []

days = 5

i = 0
while(i < days*2):
    main.append(-1)
    side.append(-1)
    i += 1
    
i = 0
while(i < days*2):
    if(i < days and main[i] == -1):
        t = -1
        r = 0
        while(r == 0):
            t = random.randint(0,len(meals_main)-1)
            if(not(t in main)):
                main[i] = t
                if(meals_main[t][1] > 1):
                    main[i+2] = t
                    if(meals_main[t][1] > 2):
                        main[i+4] = t
                r = 1
    t = -1
    r = 0
    while(r == 0):
        t = random.randint(0,len(meals_side)-1)
        if(not(side[i-1] == t)):
            side[i] = t
            r = 1
    i += 1
    
i = 0
while(i < len(main)):
    if(main[i] != -1):
        print("day %d main dish is %s with a side of %s"%(i, meals_main[main[i]][0], meals_side[side[i]][0]))
    else:
        print("day %d unplanned"%(i))
    i += 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    