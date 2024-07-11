import json
from abc import ABC, abstractmethod


class FileWork(ABC):
    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def save_file(self, data):
        pass

    @abstractmethod
    def delite_file(self):
        pass


class WorkWithJson(FileWork):
    """
    Класс работающий с JSON файлом вакансий
    """
    def __init__(self):
        self.file_name = ""
        self.abs_path = "data/vacancies.json"

    def read_file(self):
        with open(self.abs_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_file(self, data):
        with open(self.abs_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delite_file(self):
        pass
