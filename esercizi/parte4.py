#Classe del file CSV
class CSVFile:
    #Metodo di istanziazione dell' oggetto
    def __init__(self,file_name):
        self.name=file_name
    #Funzione che torna la lista di liste dei dati del file CSV
    def get_data(self):
        #Creo una lista vuota
        data=[]
        #Apro il file
        my_file=open(self.name,'r')
        for line in my_file:
            elemento=line.split(',')
            elemento[1]=elemento[1].strip()
            if(elemento[0]!='Date'):
                data.append(elemento)
        my_file.close()
        return data

#csv=CSVFile('shampo_sales.csv')
#print(csv.get_data())