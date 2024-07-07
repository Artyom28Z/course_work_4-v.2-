class Vacancy:
    def __init__(self, name, area, salary, url, snippet):
        self.name = self.__validation_name(name)
        self.area = self.__validation_area(area)
        self.salary = self.__validation_salary(salary)

        self.url = url
        self.snippet = snippet

    def __str__(self):
        return (f"{self.name}\n"
                f"Город: {self.area}\n"
                f"Зарплата: {self.salary}\n")

    def __lt__(self, other):
        if self.salary < other.salary:
            return True
        elif not self.salary or not other.salary:
            return "З/п не указана"
        else:
            return False

    @staticmethod
    def __validation_name(data):
        if data:
            return data
        else:
            return "Отсутствует название вакансии"

    @staticmethod
    def __validation_salary(data):
        if data:
            salary_from = data.get("from")
            salary_to = data.get("to")
            if salary_from == None and salary_to != None:
                return f"до {salary_to}"
            elif salary_from != None and salary_to == None:
                return f"от {salary_from}"
            return f"от {salary_from} до {salary_to}"
        else:
            return "Не указана"

    @staticmethod
    def __validation_area(data):
        if data:
            return data
        else:
            return "Не указан"

    @classmethod
    def new_vacancy(cls, vacancy):
        name = vacancy.get("name")
        area = vacancy.get("area").get("name")
        salary = vacancy.get("salary")

        url = vacancy.get("url")
        snippet = vacancy.get("snippet")
        return cls(name, area, salary, url, snippet)
