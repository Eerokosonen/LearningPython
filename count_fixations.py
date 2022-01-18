import csv

# This script goes through the U'n'Eye created fixation/saccade propabilities, 
# and counts them accordingly

fixations = 0
fduration = 0
found = False
alldurations = []

subject = 's1'

predictions = open('%s/Labels_prob_class0.csv' %subject,'r') 
r = csv.reader(predictions)

with predictions:
    for row in r:  
        for i in row: #fixation=0 saccade=1
            if(i!='1.000000000000000000e+00') and (found==False): #fixation starts
                fixations+=1 
                fduration+=1                
                found = True    
            if(i!='1.000000000000000000e+00') and (found==True): #fixation continues
                fduration+=1
            if (i=='1.000000000000000000e+00') and (found==True): #saccade starts -> fixation ends                                                        
                alldurations.append(fduration/1000)
                fduration=0
                found = False 

print('fixation count:')
print(fixations)


print('avg fixation duration:')
#print(alldurations)
if len(alldurations) != 0:
    print(sum(alldurations)/len(alldurations))
               