#Classe del file CSV
class CSVFile:
    #Metodo di istanziazione dell' oggetto
    def __init__(self,file_name):
        self.name=file_name
        self.errore=True
        #Verifica dell'esistenza del file
        try:
            my_file=open(self.name,'r')
            line=my_file.readline()
        except Exception as e:
            #Stampa l'errore in caso di problemi durante l'apertura del file
            print('Errore operazione di apertura del file con errore:"{}"'.format(e))
        else:
            #Stampa e chiude il file se non si sono verificati problemi
            self.errore=False
            print('Il parametro del file è corretto e il file si è aperto con successo.')
            my_file.close()

    #Funzione che torna la lista di liste dei dati del file CSV
    def get_data(self):
        #Creo una lista vuota
        data=[]
        if(not self.errore ):
            #Apro il file e ne leggo il contenuto
            my_file=open(self.name,'r')
            for line in my_file:
                if(',' in line):
                    elemento=line.split(',')
                    elemento[1]=elemento[1].strip()
                    if(elemento[0]!='Date'):
                        #Aggiungo la lista di elementi alla lista di dati
                        data.append(elemento)
            my_file.close()
        return data


#Creo la classe NumericalCSVFile e lo estendo a CSVFile
class NumericalCSVFile(CSVFile):

    #Creo un metodo get data che sovrascrive il metodo di CSVFile
    def get_data(self):
        #Chiamo la funzione della classe genitore tramite il metodo built-in super
        my_list=super().get_data()
        #Leggo il contenuto del file e verifico se si possono manifestare vari errori
        for element in my_list:
            if(element[0]!='Date'):
                try:
                    element[1]=float(element[1])
                except ValueError:
                    print('Errore il valore di {} non puo essere convertito a float percio verra assegnato il valore 0.0.'.format(element[1]))
                    element[1]=0.0
                except TypeError:
                    print('Errore il tipo dati {} non puo essere convertito a float percio verra assegnato il valore -1.0.'.format(element[1]))
                    element[1]=-1.0
                except Exception as e:
                    print('Errore generico:{}'.format(e))
        return my_list


#csv=CSVFile('shampo_sales.csv')
#print(csv.get_data())
#numerical_csv=NumericalCSVFile(file_name='shampo_sales.csv')
#print(numerical_csv.get_data())