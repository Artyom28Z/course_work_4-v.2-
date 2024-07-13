from src.json_worker import WorkWithJson


class UserInput(WorkWithJson):
    """
    Класс работы с вводом пользователя
    """
    def __init__(self):
        super().__init__()
        self.vacancies_list = []

    def get_vacancy_from_keyword(self, keywords):
        """
        Метод поиска вакансий по ключевому слову
        :param keywords:
        :return:
        """
        res = []
        for i in self.vacancies_list:
            if i.name.find(keywords) != 1:
                res.append(i)
        return res
