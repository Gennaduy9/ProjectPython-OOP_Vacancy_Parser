from src.abc.abc_vacancy_api import VacancyApi

from requests import *

import json


class SuperJob(VacancyApi):
    """
    Класс SuperJob, наследующийся от абстрактного класса VacancyApi.
    Он содержит переменные __API_KEY (private, для обращения только внутри класса) и
    _api_link (protected, для обращения внутри класса и во всех дочерних классах),
    которые хранят ключ API и ссылку на API SuperJob,
    и методы str(), get_vacancies_api(), get_search_vacancies() и get_region_vacancies().
    Класс содержит необходимые методы для получения списка вакансий по поисковому запросу или региону.
    """

    __API_KEY = "v3.r.137586941.f8b5c1d6c7ceb995c050acb9474a789e4ab49761.8cab32a4e53a3040d3f44b75eb5336b86fe9a2a3"
    _api_link = "https://api.superjob.ru/2.0/vacancies"

    def __init__(self):
        pass

    def __str__(self):
        """
        :return: Возвращает строку "superjob.ru".
        """
        return "superjob.ru"

    def get_vacancies_api(self, **kwargs):
        """
        Метод get_vacancies_api() выполняет GET-запрос к API для получения данных о вакансиях
        с использованием переданных параметров поиска.

        :param kwargs: Именованные аргументы для параметров поиска в формате "ключ-значение".
        :return data_dict: Возвращает результат в виде словаря в формате JSON или None в случае ошибки.
        """
        params = {}
        headers = {
            'X-Api-App-Id': self.__API_KEY
        }

        for key, value in kwargs.items():
            params[key] = value

        response = get(self._api_link, headers=headers, params=params)
        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            return data_dict
        else:
            print("Ошибка при выполнении запроса.")
            return []

    def get_search_vacancies(self, search_data, n=30):
        """
        Возвращает список вакансий, соответствующих переданным параметрам поиска.

        :param search_data: Строка с данными для поиска вакансий.
        :type search_data: str
        :param n: Количество вакансий на странице (по умолчанию 30).
        :return: Список вакансий, связанных с переданными параметрами поиска.
        """
        return self.get_vacancies_api(keyword=search_data, count=n)

    def get_region_vacancies(self, region, n=30):
        """
        Возвращает список вакансий, связанных с указанным регионом.

        :param region: Регион для поиска вакансий.
        :type region: str
        :param n: Количество вакансий на странице (по умолчанию 30).
        :return: Список вакансий, связанных с указанным регионом.
        """
        return self.get_vacancies_api(town=region, count=n)

    def get_keywords_vacancies(self, keywords, n=30):
        """
        Возвращает список вакансий, связанных с указанными ключевыми словами.

        :param keywords: Ключевые слова для поиска вакансий.
        :type keywords: str
        :param n: Количество вакансий на странице (по умолчанию 30).
        :return: Список вакансий, связанных с указанными ключевыми словами.
        """
        return self.get_vacancies_api(text=keywords, count=n)
