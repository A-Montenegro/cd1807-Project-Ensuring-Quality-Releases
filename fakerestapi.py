import json
from http.server import BaseHTTPRequestHandler, HTTPServer

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

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/v1/employees":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            response = {
                "status": "success",
                "data": employees,
                "message": "Successfully! All records have been fetched."
            }
            
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/v1/create":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            json_data = json.loads(data.decode())
            
            new_employee = {
                "name": json_data["name"],
                "salary": json_data["salary"],
                "age": json_data["age"],
                "id": 1511
            }
            employees.append(new_employee)
            
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            response = {
                "status": "success",
                "data": new_employee,
                "message": "Successfully! Record has been added."
            }
            
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server_address = ("", 80)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()
