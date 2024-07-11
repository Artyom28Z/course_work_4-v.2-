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
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': keyword, 'page': 0, 'per_page': top}

    def load_vacancies(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        vacancies = response.json()['items']
        vacancies.extend(vacancies)
        self.params['page'] += 1
        return vacancies
