from flask import Flask,jsonify,request
from salary_pred import pred_salary
from addition import addition
model_path = "./models/salary_pred.pkl"

app= Flask(__name__)

@app.route("/")
def home():
    response = "hello texas...."
    return jsonify({'response': response})

@app.route("/pred",methods=["POST"])
def pred():

    json_data = request.get_json()
    experience = json_data["experience"]
    print(json_data)
    predicted_salary = pred_salary(model_path,experience)
    return jsonify({'predicted_salary':predicted_salary})

@app.route('/sum',methods=["POST"])
def sum():
    json_data =request.get_json()
    a,b = json_data["a"], json_data["b"]
    sum=addition(a,b)
    return jsonify ({"sum":sum})

if __name__ == "__main__":
    app.run(debug=True)