import json
from json_db_lite import JSONDatabase

small_db = JSONDatabase(file_path="./../students.json")


def dict_list_to_json(dict_list, filename):
    try:
        json_str = json.dump(dict_list, ensure_ascii=False)
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json_str)
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при преобразовании списка словарей в JSON")
        return None


def json_to_dict_list():
    return small_db.get_all_records()

def add_student(student: dict):
    student["date_of_birth"] = student["date_of_birth"].strftime('%Y-%m-%d')
    small_db.add_records(student)
    return True

def upd_student(upd_filter: dict, new_data: dict):
    small_db.update_record_by_key(upd_filter, new_data)
    return True

def dell_student(key: str, value: str):
    small_db.delete_record_by_key(key, value)
    return True


