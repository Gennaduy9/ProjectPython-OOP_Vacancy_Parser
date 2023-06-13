from src.utils.desk import print_prettytable_hhru
from src.utils.desk import print_prettytable_sj
from src.utils.desk import print_prettytable_zp
from src.utils.desk import print_prettytable_tv


def print_welcome_user_1():
    print("\n---Анализ текущих вакансий---\n"
          "Получает информацию о вакансиях \n\nheadhunter.ru\nsuperjob.ru\nzarplata.ru\ntrudvsem.ru\n"
          "\nСохраняет информацию в файл JSON и позволяет удобно работать с ней (добавлять, фильтровать, удалять).")


def print_welcome_user_2():
    print("\n1. headhunter.ru\n2. superjob.ru\n3. zarplata.ru\n4. trudvsem.ru"
          "\n0. Выход\n")


def print_operations():
    print("1. Ввести поисковый запрос;"
          "\n2. Получить топ N вакансий по зарплате;"
          "\n3. Получить вакансии выбранного региона;"
          "\n4. Получить вакансии, по ключевому слову в описании.\n"
          "\n0. Назад.\n")


def print_result_search(platform, res, sorty="id"):
    if f"{platform()}" == "headhunter.ru":
        return print_prettytable_hhru(res, sorty)
    elif f"{platform()}" == "superjob.ru":
        return print_prettytable_sj(res, sorty)
    elif f"{platform()}" == "zarplata.ru":
        return print_prettytable_zp(res, sorty)
    elif f"{platform()}" == "trudvsem.ru":
        return print_prettytable_tv(res, sorty)