import csv

# This script goes through the dataset with x/y values and some not unnecessary values 
# in the same file, and creates two distinct files to store values for further calculations

subject = 's23' # The required dataset subject 

originalfile = open('orig_dataset.csv','r') # Full dataset
r = csv.reader(originalfile)

xvalues = open('%s_x.csv' % subject, 'w') # File to store x values
writex = csv.writer(xvalues)

yvalues = open('%s_y.csv' % subject, 'w') # File to store y values
writey = csv.writer(yvalues)

with originalfile:
    for row in r:           
        if (row[0] == subject):
            #print(row[0])
            del row[:2] # Delete unnecessary values
            writex.writerow(row[::2]) # Every other value is x
            writey.writerow(row[1::2]) # Every other value is y
            
        




        