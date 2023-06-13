from src.abc.abc_vacancy_api import VacancyApi

from requests import *

import json


class HeadHunter(VacancyApi):
    """
    Класс, наследующийся от абстрактного класса VacancyApi.
    Он содержит переменную _api_link, которая хранит ссылку на API,
    и методы init() и str(), которые не имеют реализации в данном классе.
    """

    _api_link = "https://api.hh.ru/vacancies"

    def __init__(self):
        """
        Метод init() не имеет реализации в данном классе.
        """
        pass

    def __str__(self):
        """
        :return: Метод str() возвращает строку "headhunter.ru" вакансии.
        """
        return "headhunter.ru"

    def get_vacancies_api(self, **kwargs):
        """
        Метод get_vacancies_api() выполняет GET-запрос к API для получения данных о вакансиях
        с использованием переданных параметров поиска.

        :param kwargs: Именованные аргументы для параметров поиска в формате "ключ-значение".
        :return data_dict: Возвращает результат в виде словаря в формате JSON или None в случае ошибки.
        """

        params = {}
        for key, value in kwargs.items():
            params[key] = value

        response = get(self._api_link, params=params)

        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            return data_dict
        else:
            print("Ошибка при выполнении запроса:", response.status_code)
            return None

    def get_search_vacancies(self, search_data, n=30):
        """
        Возвращает список вакансий, соответствующих переданным параметрам поиска.

        :param search_data: Строка с данными для поиска вакансий.
        :type search_data: str
        :param n: Количество вакансий на странице (по умолчанию 30).
        :return: Список вакансий, связанных с переданными параметрами поиска.
        """
        return self.get_vacancies_api(text=search_data, per_page=n)

    def get_region_vacancies(self, region, n=30):
        """
        Возвращает список вакансий, связанных с указанным регионом.

        :param region: Регион для поиска вакансий.
        :type region: str
        :param n: Количество вакансий на странице (по умолчанию 30).
        :return: Список вакансий, связанных с указанным регионом.
        """
        return self.get_vacancies_api(area=region, per_page=n)

    def get_keywords_vacancies(self, keywords, n=30):
        """
        Возвращает список вакансий, связанных с указанными ключевыми словами.

        :param keywords: Ключевые слова для поиска вакансий.
        :type keywords: str
        :param n: Количество вакансий на странице (по умолчанию 30).
        :return: Список вакансий, связанных с указанными ключевыми словами.
        """
        return self.get_vacancies_api(text=keywords, per_page=n)
