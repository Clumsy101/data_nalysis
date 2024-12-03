import os
import pickle
import numpy as np


model_path = "./models/salary_pred.pkl" 
def pred_salary(model_path, years_of_experience)->float:
    with open(model_path, 'rb')as file:
        salary_pred_model = pickle.load(file)
    
    years_of_experience = np.array(years_of_experience).reshape(1,1)
    predicted_salary= salary_pred_model.predict(years_of_experience)
    return predicted_salary[0][0]

if __name__ == '__main__':
    years_of_experience =5 
    predicted_salary= pred_salary(model_path , years_of_experience)
    predicted_salary = round(predicted_salary, 2)
    print(f"predicted salary for employing having {years_of_experience} years of experience : ${predicted_salary}")

