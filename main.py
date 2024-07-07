from src.json_worker import WorkWithJson
from src.parser import HH
from src.user_input import UserInput
from src.vacancy import Vacancy

if __name__ == "__main__":


    keyword = input("""Введите название вакансии, которую ищете
""")

    user = UserInput()
    vacancies_list = user.get_vacancies_list(keyword)

    for vacancy in user.get_vacancies_list(keyword):
        vac = Vacancy.new_vacancy(vacancy)
        print(vac)
        user.vacancies_list.append(vac)

    for vacancy in user.get_top_salary():
        print(vacancy)
