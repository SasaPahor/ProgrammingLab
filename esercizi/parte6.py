class EccezioneInput (Exception):
    pass


#==============================
#  Classe per file CSV
#==============================

class CSVFile:

    def __init__(self, name):

        # Setto il nome del file
        self.name = name
        if(not type(self.name)== str):
            raise EccezioneInput('Il nome del file non è una stringa')
        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))


    def get_data(self,start=None,end=None):
        if not self.can_read:

            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            raise EccezioneInput('File non aperto o illeggibile.')

        else:
            data = []
            my_file = open(self.name, 'r')
            if(start is None and end is None):
                # Inizializzo una lista vuota per salvare tutti i dati
                # Apro il file
                # Leggo il file linea per linea
                for line in my_file:
        
                    # Faccio lo split di ogni linea sulla virgola
                    elements = line.split(',')
        
                    # Posso anche pulire il carattere di newline 
                    # dall'ultimo elemento con la funzione strip():
                    elements[-1] = elements[-1].strip()
        
                    # p.s. in realta' strip() toglie anche gli spazi
                    # bianchi all'inizio e alla fine di una stringa.
        
                    # Se NON sto processando l'intestazione...
                    if elements[0] != 'Date':
        
                        # Aggiungo alla lista gli elementi di questa linea
                        data.append(elements)
            elif(start is not None or end is not None):
                if(end is not None and start is None):
                    raise EccezioneInput('Il valore start è None.')
                elif(start ==0):
                    raise EccezioneInput('Il valore di start non puo essere uguale a 0.')
                elif(type(start)==list or type(end)==list):
                    raise EccezioneInput('Errore tipo lista non valido.')
                elif(type(start)==dict or type(end)==dict):
                    raise EccezioneInput('Errore tipo dictonary non valido.')
                elif(type(start)== complex or type(end)==complex):
                    raise EccezioneInput('Errore tipo complex non valido.')
                elif(type(start)==tuple or type(end)==tuple):
                    raise EccezioneInput('Errore tipo tuple non valido')
                elif(type(start)==range or type(end)==range):
                    raise EccezioneInput('Errore tipo range non valido.')
                elif(type(start)==set or type(end)==set):
                    raise EccezioneInput('Errore tipo set non valido.')
                elif(type(start)==frozenset or type(end)==frozenset):
                    raise EccezioneInput('Errore tipo frozenset non valido.')
                elif(type(start)==bool or type(end)==bool):
                    raise EccezioneInput('Errore tipo bool non valido.')
                elif(type(start)==bytes or type(end)==bytes):
                    raise EccezioneInput('Errore tipo bytes non valido.')
                elif(type(start)==bytearray or type(end)==bytearray):
                    raise EccezioneInput('Errore tipo bytearray non valido.')
                elif(type(start)==memoryview or type(end)==memoryview):
                    raise EccezioneInput('Errore tipo memoryview non valido.')
                else:
                    if(type(start)==str or type(start)==float):
                        try:
                            start=int(start)
                        except Exception:
                            raise EccezioneInput('Errore il valore {} non è valido per int'.format(start))
                    
                    if(type(end)==str or type(end)==float):
                        try:
                            end=int(end)
                        except Exception:
                            raise EccezioneInput('Errore il valore {} non è valido per int'.format(end))
                    number_lines=my_file.readlines()
                    if(start<0):
                        raise EccezioneInput('Il valore start è minore di 0.')
                    if(start>len(number_lines)):
                        raise EccezioneInput('Errore il valore di start è maggiore di {}'.format(len(number_lines)))
                    if(end is None):
                        i=0
                        for line in number_lines:
                            elements = line.split(',')
                            if(start<=i):
                                if elements[0] != 'Date':
                                    elements[-1] = elements[-1].strip()
                                    data.append(elements)
                            i+=1
                    else:       
                        if(end<start):
                            raise EccezioneInput('Errore il valore di end è minore di start')
                        elif(end<0 or start <0):
                            raise EccezioneInput('Errore argomenti minori di 0')
                        if(start>len(number_lines)):
                            raise EccezioneInput('Errore il valore di start è maggiore di {}'.format(len(number_lines)))
                        elif(end>len(number_lines)):
                            raise EccezioneInput('Errore il valore di end è maggiore di {}'.format(len(number_lines)))
                        i=0
                        for line in number_lines:
                            elements = line.split(',')
                            if(start<=i and i<=end):
                                if elements[0] != 'Date':
                                    elements[-1] = elements[-1].strip()
                                    data.append(elements)
                            i+=1
        # Chiudo il file
        my_file.close()
        # Quando ho processato tutte le righe, ritorno i dati
        return data



#==============================
# Classe per file NumericalCSV
#==============================

class NumericalCSVFile(CSVFile):

    def get_data(self,start=None,end=None):

        # Chiamo la get_data del genitore 
        string_data = super().get_data(start,end)

        # Preparo lista per contenere i dati ma in formato numerico
        numerical_data = []

        # Ciclo su tutte le "righe" corrispondenti al file originale 
        for string_row in string_data:

            # Preparo una lista di supporto per salvare la riga
            # in "formato" nuumerico (tranne il primo elemento)
            numerical_row = []

            # Ciclo su tutti gli elementi della riga con un
            # enumeratore: cosi' ho gratis l'indice "i" della
            # posizione dell'elemento nella riga.
            for i,element in enumerate(string_row):

                if i == 0:
                    # Il primo elemento della riga lo lascio in formato stringa
                    numerical_row.append(element)

                else:
                    # Converto a float tutto gli altri. Ma se fallisco, stampo
                    # l'errore e rompo il ciclo (e poi saltero' la riga).
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break

            # Alla fine aggiungo la riga in formato numerico alla lista
            # "esterna", ma solo se sono riuscito a processare tutti gli
            # elementi. Qui controllo per la lunghezza, ma avrei anche potuto
            # usare una variabile di supporto o fare due break in cascata.
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data



#==============================
#  Esempio di utilizzo
#==============================

#mio_file = CSVFile(name='shampo_sales.csv')
#print('Nome del file: "{}"'.format(mio_file.name))
#print('Dati contenuti nel file: #"{}"'.format(mio_file.get_data(1,3)))

#mio_file_numerico = NumericalCSVFile(name='shampoo_sales.csv')
#print('Nome del file: "{}"'.format(mio_file_numerico.name))
#print('Dati contenuti nel file: "{}"'.format(mio_file_numerico.get_data()))
