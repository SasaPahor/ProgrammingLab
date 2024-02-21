def somma(file_name):
    somma=0
    my_file=open(file_name)
    for line in my_file:
        elements=line.split(',')
        if(elements[0]!='Date'):
            somma+=float(elements[1])
    return somma