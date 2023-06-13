
class Vacancies:
    """
    Класс для хранения данных о вакансии.
    Атрибуты:
        - id: идентификатор вакансии;
        - name: название вакансии;
        - salary: зарплата вакансии;
        - company_name: название компании, предлагающей вакансию;
        - description: описание вакансии;
        - link: ссылка на вакансию;
        - region: регион, где расположена компания.
    """
    def __init__(self, id: str, name: str, salary: str, company_name: str, description: str, link: str, region: str):
        self.id = self.validate_str(id, "id")
        self.name = self.validate_str(name, "title")
        self.salary = self.validate_int_float(salary, "salary")
        self.company_name = self.validate_str(company_name, "company_name")
        self.description = self.validate_str(description, "description")
        self.link = self.validate_str(link, "link")
        self.region = self.validate_str(region, "region")

    @staticmethod
    def validate_str(string_data, name_col):
        """
        Проверяет, является ли переданный аргумент строкой. Если да, то метод возвращает эту строку.
        Если нет, то метод вызывает ошибку ValueError.
        """
        if isinstance(string_data, str):
            return string_data
        raise ValueError(f"Invalid {name_col}, {name_col} must be a string.")

    @staticmethod
    def validate_int_float(int_float, name_col):
        """
        Проверяет, является ли переданный аргумент числом (int или float).
        Если да, то метод возвращает это число. Если нет, то метод вызывает ошибку ValueError.
        """
        if isinstance(int_float, (int, float)):
            return int_float
        raise ValueError(f"Invalid {name_col}, {name_col} must be a number.")

    def __eq__(self, other):
        """
        Сравнивает зарплаты текущей и переданной вакансий.
        Метод возвращает True, если зарплаты равны, и False в противном случае.
        """
        if not self.salary or not other.salary:
            return False
        return str_to_digit(self.salary) == str_to_digit(other.salary)

    def __lt__(self, other):
        """
        Сравнивает зарплаты текущей и переданной вакансий.
        Метод возвращает True, если зарплата текущей вакансии меньше зарплаты переданной вакансии,
        и False в противном случае.
        """
        if not self.salary or not other.salary:
            return False
        return str_to_digit(self.salary) < str_to_digit(other.salary)

    def __gt__(self, other):
        """
        Сравнивает зарплаты текущей и переданной вакансий.
        Метод возвращает True, если зарплата текущей вакансии больше зарплаты переданной вакансии,
        и False в противном случае.
        """
        if not self.salary or not other.salary:
            return False
        return str_to_digit(self.salary) > str_to_digit(other.salary)


def str_to_digit(input_str):
    if isinstance(input_str, str):
        return int(input_str.split(" ")[0])
    raise ValueError("Неверная входная строка, должна быть строкой.")