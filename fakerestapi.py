from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {
        "id": 1,
        "employee_name": "Tiger Nixon",
        "employee_salary": 320800,
        "employee_age": 61,
        "profile_image": ""
    },
    {
        "id": 2,
        "employee_name": "Garrett Winters",
        "employee_salary": 170750,
        "employee_age": 63,
        "profile_image": ""
    },
    # ... (Add remaining employee objects)
    {
        "id": 24,
        "employee_name": "Doris Wilder",
        "employee_salary": 85600,
        "employee_age": 23,
        "profile_image": ""
    }
]

@app.route("/api/v1/employees", methods=["GET"])
def get_employees():
    return jsonify({
        "status": "success",
        "data": employees,
        "message": "Successfully! All records have been fetched."
    })

@app.route("/api/v1/create", methods=["POST"])
def create_employee():
    data = request.get_json()
    new_employee = {
        "name": data["name"],
        "salary": data["salary"],
        "age": data["age"],
        "id": 1511
    }
    employees.append(new_employee)
    return jsonify({
        "status": "success",
        "data": new_employee,
        "message": "Successfully! Record has been added."
    })

if __name__ == "__main__":
    app.run()
