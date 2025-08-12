import requests

def get_all_students():
    url = "http://127.0.0.1:8000/students/2"
    response = requests.get(url)
    print(response.status_code)  # Убедитесь, что статус 200
    print(response.text)  
    # return response.json()


students = get_all_students()
# for i in students:
#     print(i)

