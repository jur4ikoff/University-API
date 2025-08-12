import json


def dict_list_to_json(dict_list, filename):
    try:
        json_str = json.dump(dict_list, ensure_ascii=False)
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json_str)
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при преобразовании списка словарей в JSON")
        return None


def json_to_dict_list(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            json_str = file.read()
            print(json_str)
            dict_list = json.loads(json_str)
        return dict_list

    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при чтении JSON из файла или преобразовании")
        return None