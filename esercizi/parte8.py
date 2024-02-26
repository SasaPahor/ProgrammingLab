class Model:
    pass

class TrendModel(Model):
    def __init__(self,window=3):
        self.window=window
    def predict(self,data):
        if(len(data)!=self.window):
            raise ValueError('Passati {} mesi'.format(len(data)) +
            ' ma il modello richiede di averne {}.'.format(self.window))
        
        variazioni=[]
        item_prev=None
        for item in data:
            if(item_prev is not None):
                variazioni.append(item-item_prev)
            item_prev=item
        prediction=data[self.window-1]+(sum(variazioni)/len(variazioni))
        return prediction


trend_model=TrendModel()
print(trend_model.predict([50,52,60]))