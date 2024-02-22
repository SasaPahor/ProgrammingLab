#Classe del file CSV
class CSVFile:
    #Metodo di istanziazione dell' oggetto
    def __init__(self,file_name):
        self.name=file_name
        #Verifica dell'esistenza del file
        try:
            my_file=open(self.name,'r')
            line=my_file.readline()
        except Exception as e:
            #Stampa l'errore in caso di problemi durante l'apertura del file
            print('Errore operazione di apertura del file con errore:"{}"'.format(e))
        else:
            #Stampa e chiude il file se non si sono verificati problemi
            print('Il parametro del file è corretto e il file si è aperto con successo.')
            my_file.close()

    #Funzione che torna la lista di liste dei dati del file CSV
    def get_data(self):
        #Creo una lista vuota
        data=[]
        #Apro il file e ne leggo il contenuto
        my_file=open(self.name,'r')
        for line in my_file:
            elemento=line.split(',')
            elemento[1]=elemento[1].strip()
            if(elemento[0]!='Date'):
                #Aggiungo la lista di elementi alla lista di dati
                data.append(elemento)
        my_file.close()
        return data
#csv=CSVFile('shampo_sales.csv')
#print(csv.get_data())