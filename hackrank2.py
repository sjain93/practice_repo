
def jumpingOnClouds(c):
    possib = {'single':0, 'double':0}
    path=[]
    for index, cloud in enumerate(c):
        print(index,cloud)
        if index+1 == len(c):
            break
        elif c[index-1]==0 and c[index+1]==0:
            continue
        elif cloud == 0 and c[index+2] == 0:
            possib['double'] += 1
            path.append(index)
            continue
        elif cloud == 0 and c[index+1] == 0:
            possib['single'] += 1
            path.append(index)
        else:
            continue
    print(possib)

      

n = 7
c = [0,0,1,0,0,1,0]
jumpingOnClouds(c)
