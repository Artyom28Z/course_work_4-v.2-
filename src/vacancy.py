class Vacancy:
    """
    Класс обработки информации о вакансии
    """
    def __init__(self, name, area, salary):
        self.name = self.__validation_name(name)
        self.area = self.__validation_area(area)
        self.salary = salary

    def __str__(self):
        if self.salary == 0:
            return (f"{self.name}\n"
                    f"Город: {self.area}\n"
                    f"З-п: Не указана\n")
        return (f"{self.name}\n"
                f"Город: {self.area}\n"
                f"З-п: {self.salary}\n")

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
    def __validation_area(data):
        if data:
            return data
        else:
            return "Не указан"

    @classmethod
    def new_vacancy(cls, vacancy):
        name = vacancy.get("name")
        area = vacancy.get("area").get("name")
        if vacancy.get("salary"):
            if vacancy.get("salary").get("from"):
                salary = vacancy.get("salary").get("from")
            elif vacancy.get("salary").get("from") == None and vacancy.get("salary").get("to"):
                salary = vacancy.get("salary").get("to")
            else:
                salary = 0
        else:
            salary = 0
        return cls(name, area, salary)
