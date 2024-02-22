class CSVFile:

    def __init__(self, name):
        self.name = name
        self.can_read = True
        if (not type(self.name)==str):
            raise ValueError('Errore il valore passato non è una stringa.')
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))


    def get_data(self,start = None, end=None):
        data = []
        if not self.can_read:
            print('Errore, file non aperto o illeggibile')
            return None
        elif(start is None and end is None):
            print('Il file verra stampato completamente perché lo start e la fine non sono stati impostati')
            my_file = open(self.name, 'r')
            for line in my_file:
                elements = line.split(',')
                elements[-1] = elements[-1].strip()
                if elements[0] != 'Date':
                    data.append(elements)
            my_file.close()
        else:
            errore=False
            try:
                start=int(start)
                end=int(end)
            except ValueError:
                print('Errore il valore {} oppure {} non possono essere convertiti a int'.format(start,end))
            except TypeError:
                print('Errore il tipo {} oppure {} non puo essere convertito a int'.format(start,end))
            except Exception as e:
                print('Errore generico:{}'.format(e))
            else:
                errore=True
            if(not errore):
                raise Exception('Errore gli input forniti non sono corretti.')
                
            if(end<0):
                end*=-1
                
            if(start<0):
                start*=-1
                
            if(end<start):
                tmp=start
                start=end
                end=tmp
                
            if(start==0):
                print('Il valore di start non puo essere 0; il suo valore verra modificato in 1.')
                start=1
                
            if(end==0):
                print('Il valore di end non puo essere 0; il suo valore verra modificato in 1.')
                end=1

            my_file = open(self.name, 'r')
            verifica=True
            for i,line in enumerate(my_file):
                if(start<=i and i<=end):
                    verifica=False
                    elements = line.split(',')
                    elements[-1] = elements[-1].strip()
                    if elements[0] != 'Date':
                        data.append(elements)
            my_file.close()
            
            if(verifica):
                print('Il numero di righe del file è minore del parametro start perciò sara ritornata una lista vuota.')
        return data

class NumericalCSVFile(CSVFile):
    
    def get_data(self):
        string_data = super().get_data()
        numerical_data = []
        for string_row in string_data:
            numerical_row = []
            for i,element in enumerate(string_row):

                if i == 0:
                    numerical_row.append(element)

                else:
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data



mio_file = CSVFile(name='shampo_sales.csv')
print('Dati contenuti nel file: #"{}"'.format(mio_file.get_data(2,3)))

#mio_file_numerico = NumericalCSVFile(name='shampo_sales.csv')
#print('Nome del file: "{}"'.format(mio_file_numerico.name))
#print('Dati contenuti nel file: "{}"'.format(mio_file_numerico.get_data()))
