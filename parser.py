import json


def parserJsonFile(p):
    with open(p, "r", encoding="UTF-8") as file:
        json_content = json.load(file)
        counter = 0
        num_of_hours = float
        client_name = str
        while counter < len(json_content):
            try:
                num_of_hours = json_content[f"Клиент {counter}"]["КоличествоЧасов"]
                client_name = json_content[f"Клиент {counter}"]["Наименование"]
                time_by_sys_area = float(json_content[f"Клиент {counter}"]["ДоговорыКонтрагента"][0]["Участки"][2][
                                             "КоличествоЧасов"])

            except:
                time_by_sys_area = 0.00

            if num_of_hours > 2.0 and time_by_sys_area > 0.5:
                print(f"Наименование - {client_name}; Количество времени - {num_of_hours};"
                      f" Кол. Часов \"Системное администрирование\" - {time_by_sys_area}")

            counter += 1
