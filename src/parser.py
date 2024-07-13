from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """
    Абстрактный класс
    """
    @abstractmethod
    def load_vacancies(self):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self, keyword, top):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': keyword, 'page': 0, 'per_page': top}

    def load_vacancies(self):
        """
        Метод загрузки информации о вакансиях от API Head Hunter
        :return:
        """
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        vacancies = response.json()['items']
        vacancies.extend(vacancies)
        self.__params['page'] += 1
        return vacancies
