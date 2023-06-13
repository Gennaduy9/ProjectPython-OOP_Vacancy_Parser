from src.abc.abc_vacancy_file import VacancyFile

import os

import json


class JobJSONFile(VacancyFile):
    """
    Класс, наследующий от абстрактного класса VacancyFile для работы с файлами в формате JSON.
    Он содержит переменные filename и file_path, которые хранят имя и путь к файлу,
    и методы init(), add_vacancy(), get_vacancies() и remove_vacancy()
    для добавления, удаления и получения вакансий из файла.
    """

    def __init__(self, filename):
        """
        Метод init() инициализирует переменную filename и вычисляет путь к файлу.
        :param filename путь к файлу.
        """
        self.filename = filename

    def add_vacancy(self, save_vacancy):
        """
        Метод принимает словарь save_vacancy, записывает его в файл в формате JSON
        и возвращает путь к файлу.
        :param: save_vacancy записывает его в файл в формате JSON.
        :return: Возвращает путь к файлу.
        """
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(save_vacancy, file, indent=2, ensure_ascii=False)
        return self.filename

    @staticmethod
    def testimony(data_dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами (Для разработки)"""
        print(json.dumps(data_dict, indent=2, ensure_ascii=False))

    def get_vacancies(self, platform, **kwargs):
        """
        Метод читает данные из файла и возвращает их в виде словаря.
        Данные могут быть отфильтрованы по платформе, передаваемой в качестве аргумента.
        """
        with open(self.filename, 'r', encoding="utf-8") as file:
            return self.testimony(json.load(file))

    def remove_vacancy(self, vacancy_id):
        """
        Метод удаляет вакансию из файла по ее id.
        Для этого он читает данные из файла, фильтрует их по id и записывает обратно в файл.
        """
        with open(self.filename, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        with open(self.filename, 'w', encoding="utf-8") as file:
            for line in lines:
                vacancy = json.loads(line)
                if vacancy.get('id') != vacancy_id:
                    file.write(line)