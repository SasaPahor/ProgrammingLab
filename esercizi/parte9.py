class Model:
    def fit(self, data):
        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')


class TrendModel(Model):
    def __init__(self,window=3):
        self.window=window
    
    def validate_data(self, data):
        if len(data) != self.window:
            raise ValueError('Passati {} mesi'.format(len(data)) +
            ' ma il modello richiede di' +
            ' averne {}.'.format(self.window))
    def compute_avg_variation(self, data):
        variations = []
        item_prev = None
        for item in data:
            if item_prev is not None:
                variations.append(item-item_prev)
            item_prev = item
        avg_variation = sum(variations)/len(variations)
        return avg_variation
    
    def predict(self, data):
        self.validate_data(data)
        prediction = data[-1] + self.compute_avg_variation(data)
        return prediction


class FitTrendModel(TrendModel):
    def fit(self, data):
        self.historical_avg_variation = self.compute_avg_variation(data)
    def predict(self, data):
        try:
            self.historical_avg_variation
        except AttributeError:
            raise Exception('Il modello non è fittato!')
        self.validate_data(data)
        prediction = data[-1] + (self.historical_avg_variation +
        self.compute_avg_variation(data))/2
        return prediction

#trend_model=TrendModel()
#print(trend_model.predict([50,52,60]))