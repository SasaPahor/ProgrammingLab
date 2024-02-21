def sum_csv(file_name):
    somma=0
    my_file=open(file_name,'r')
    for line in my_file:
        if(len(line)==0):
            continue
        elif(','in line):
            elements=line.split(',')
            if(elements[0]!='Date'):
                somma+=float(elements[1])
    my_file.close()
    return somma
#Test utilizzo
#print(sum_csv('shampo_sales.csv'))