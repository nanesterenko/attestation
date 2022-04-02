"""Написать логику дла робота, разливающего напитки по бутылкам."""

import itertools
from typing import Dict, Optional

resources1 = [
    {
        "robot": 1,
        "resource": "вода",
        "limit": 4,
        "portion": 1
    },
    {
        "robot": 1,
        "resource": "сахар",
        "limit": 10,
        "portion": 1
    },
    {
        "robot": 2,
        "resource": "вода",
        "limit": 10,
        "portion": 0.5
    },
    {
        "robot": 1,
        "resource": "вишнёвая вкусовая добавка",
        "limit": 2,
        "portion": 1
    }
]
resources2 = [
    {
        "robot": 1,
        "resource": "вода",
        "limit": 2,
        "portion": 1
    },
    {
        "robot": 1,
        "resource": "сахар",
        "limit": 2,
        "portion": 1
    },
    {
        "robot": 1,
        "resource": "клубника",
        "limit": 2,
        "portion": 1
    },
    {
        "robot": 2,
        "resource": "вода",
        "limit": 3,
        "portion": 1
    },
    {
        "robot": 2,
        "resource": "сахар",
        "limit": 3,
        "portion": 1
    },
    {
        "robot": 2,
        "resource": "тархун",
        "limit": 2,
        "portion": 1
    }
]
resources3 = [
    {
        "robot": 1,
        "resource": "сахар",
        "limit": 2,
        "portion": 1
    },
    {
        "robot": 1,
        "resource": "яблочная вкусовая добавка",
        "limit": 2,
        "portion": 1
    }
]


class OutOfResourceError(Exception):
    """Исключение, если из имеющихся ресурсов не запланировать ни одного напитка"""

    def __init__(self, message: str):
        super().__init__(self)
        self.message = message

    def __str__(self) -> str:
        return "Недостаточно ресурсов"


def get_robot(item: Dict) -> Optional[int]:
    return item.get("robot")


def calculate(available_resources: list) -> list:
    """Функция принимает исходный список и возвращает список инструкций для роботов"""
    source_for_robot = itertools.groupby(available_resources, get_robot)
    all_instruction = list()
    robot_manager = dict()
    for key, group in source_for_robot:
        """Распределяем ресурсы между роботами"""
        if not robot_manager.get(key):
            robot_manager[key] = dict()
            robot_manager[key]["сахар"] = dict()
            robot_manager[key]["вода"] = dict()
            robot_manager[key]["supplement"] = list()
        for resource in group:
            if resource.get("resource") == "сахар":
                robot_manager[key]["сахар"] = resource
            elif resource.get("resource") == "вода":
                robot_manager[key]["вода"] = resource
            else:
                robot_manager[key]["supplement"].append(resource)
    for key, item in robot_manager.items():
        """Для напитка обязательны вода и сахар, добавки необязательны"""
        other_resources = item.get("supplement")
        other_resources = sorted(other_resources, key=lambda item: item.get('portion'))
        water = item.get("вода")
        sugar = item.get("сахар")
        try:
            max_buttle = min(int(water.get("limit") // water.get("portion")),
                             int(sugar.get("limit") // sugar.get("portion")))
        except TypeError:
            print("Не удалось вычислить возможное количество бутылок")
            break
        for other_resource in other_resources:
            try:
                portions_supplement = int(other_resource.get("limit") // other_resource.get("portion"))
            except TypeError:
                print("Не удалось вычислить сколько раз можем использовать добавки")
                break

            # Вычисляем сколько бутылок с полным комплектом
            bottles_with_full_set = min((max_buttle, portions_supplement))

            """Пополняем инструкции"""
            for x in range(max_buttle):
                if bottles_with_full_set > 0:

                    all_instruction.append({
                        water.get("resource"): water.get("portion"),
                        sugar.get("resource"): sugar.get("portion"),
                        other_resource.get("resource"): other_resource.get("portion"),
                        "robot": key
                    })
                else:
                    all_instruction.append(
                        {
                            water.get("resource"): water.get("portion"),
                            sugar.get("resource"): sugar.get("portion"),
                            "robot": key
                        }
                    )
                bottles_with_full_set -= 1
                portions_supplement -= 1

    if all_instruction == []:
        raise OutOfResourceError("insufficient resources")

    return all_instruction


c = calculate(resources2)
print(c)
