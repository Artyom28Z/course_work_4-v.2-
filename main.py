from src.json_worker import WorkWithJson
from src.parser import HH
from src.user_input import UserInput
from src.vacancy import Vacancy

if __name__ == "__main__":

    user = UserInput()
    keyword = input("""Введите название вакансии, которую ищете
""")
    n = int(input("""Ведите топ количество вакансий
"""))

    jw = WorkWithJson()
    hh = HH(keyword, n)
    sorted_list = []
    for vacancy in hh.load_vacancies():
        vac = Vacancy.new_vacancy(vacancy)
        user.vacancies_list.append(vac)
        sorted_list.append(vac)

    sort_by_salary = list(sorted(sorted_list, key=lambda x: x.salary, reverse=True))

    for i in sort_by_salary:
        print(i)

    jw.save_file(hh.load_vacancies())

    keywords_2 = input("""Введите ключевые слово для поиска вакансий
""")
    sorted_list_2 = []
    for vac_2 in user.get_vacancy_from_keyword(keywords_2):
        sorted_list_2.append(vac_2)

    sort_by_salary_2 = list(sorted(sorted_list_2, key=lambda x: x.salary, reverse=True))

    for i in sort_by_salary_2:
        print(i)
