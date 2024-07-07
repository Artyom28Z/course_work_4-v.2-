from src.parser import HH


class UserInput:
    def __init__(self):
        self.vacancies_list = []

    @staticmethod
    def get_vacancies_list(keyword):
        hh = HH(keyword)
        return hh.load_vacancies()

    def get_top_salary(self):
        n = int(input("""Ведите топ количество вакансий
"""))
        sort_by_salary = list(sorted(self.vacancies_list, key=lambda x: x.salary, reverse=True))
        return sort_by_salary[:n]

    def get_vacancy_from_keyword(self):
        keywords = input("""Введите ключевые слово для поиска вакансий
""")
        res = []
        for i in self.vacancies_list:
            if i.name.find(keywords) != 1:
                res.append(i)
        return res
