from abc import ABC, abstractmethod


class VacancyApi(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_vacancies_api(self):
        """Подключение к API и получение вакансий"""
        pass