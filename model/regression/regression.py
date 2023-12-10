import numpy as np
import pandas as pd
class Processor():  
    def __init__(self):
        self.model_feature_names_in_ = np.array(['side dish', 'white rice', 'purple rice', 'brown rice', 'plate',
       'box', 'main_dish_25', 'main_dish_30', 'main_dish_40',
       'side_dishes_n'])
        self.model_coef_ = np.array([ 11.54031221, -19.96180313, -19.66237169, -23.35313679,
        -2.65625959,  -2.91208389,   3.67859321,   1.15122184,
         2.32304665,  -2.91490648])
        self.model_intercept_ = 12.785702021623191
        self.class_id_to_name = ['plate', 'box', 'white rice', 'brown rice', 'purple rice', 'side dish', 'main_dish_25', 'main_dish_30', 'main_dish_40']
        self.name_to_money = {'side dish': 10, 'white rice': 20, 'purple rice': 20, 'brown rice': 20, 'main_dish_25': 25, 'main_dish_30': 30, 'main_dish_40': 40}
        self.containers = ["box", "plate"]
        self.side_dishes = ["side dish"]
        
    def _cal_area(self, width, height):
        return width * height
    
    def process_output(self, output):
        data = pd.DataFrame(columns=self.model_feature_names_in_)
        dic = {}
        side_dishes_n = 0
        for _, value in output.items():
            class_name = self.class_id_to_name[value["number"]]
            area = self._cal_area(value["location"][2], value["location"][3])
            dic[class_name] = dic.get(class_name, 0) + area
            # if is side dish
            if class_name in self.side_dishes:
                side_dishes_n += 1
        
        # If dic has container, calculate the ratio
        if sum([dic.get(key, 0) for key in self.containers]) != 0:
            overall_container = sum([dic.get(key, 0) for key in self.containers])
            for key in dic.keys():
                dic[key] = dic[key] / overall_container
        # Else calculate the ratio of all
        else: 
            overall = sum(dic.values())
            for key in dic.keys():
                dic[key] = dic[key] / overall

        dic["side_dishes_n"] = side_dishes_n
        
        data = pd.concat([data, pd.DataFrame(dic, index=[0])]).fillna(0)
        return data
    
    def _calc_fair_price(self, data):
        fair_price = 0
        for key in data.keys():
            if key in self.containers or key in self.side_dishes:
                continue
            if data[key].values[0] == 0:
                continue
            if key == "side_dishes_n":
                fair_price += data[key].values[0] * self.name_to_money["side dish"]
                continue
            
            fair_price += self.name_to_money[key]
        return fair_price
    
    def predict_one(self, output,ground):
        Have_stuff = False
        for _, item in output.items():
            if item['number'] not in [0, 1]:
                Have_stuff = True
                break
        if( not Have_stuff):
            return 0


        data = self.process_output(output)
        # Calc fair price
        fair_price = self._calc_fair_price(data)
        #print(fair_price)
        # Predict diff
        diff = np.dot(data, self.model_coef_) + self.model_intercept_
        # Add back fair price
        pred_price = diff + fair_price
        if ground:
            return int(round(pred_price[0] / 5) * 5)
        else:
            return pred_price[0]
    