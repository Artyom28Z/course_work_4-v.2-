class Vacancy:
    """
    Класс обработки информации о вакансии
    """
    def __init__(self, name, area, salary):
        self.name = self.__validation_name(name)
        self.area = self.__validation_area(area)
        self.salary = salary

    def __str__(self):
        """
        Магический метод для вывода строки с краткой информацией о одной вакансии
        :return:
        """
        if self.salary == 0:
            return (f"{self.name}\n"
                    f"Город: {self.area}\n"
                    f"З-п: Не указана\n")
        return (f"{self.name}\n"
                f"Город: {self.area}\n"
                f"З-п: {self.salary}\n")

    def __lt__(self, other):
        """
        Магический метод сравнения по зарплате
        :param other:
        :return:
        """
        if self.salary < other.salary:
            return True
        elif not self.salary or not other.salary:
            return "З/п не указана"
        else:
            return False

    @staticmethod
    def __validation_name(data):
        """
        Статический метод проверки на присутствие или отсутствие названия вакансии
        :param data:
        :return:
        """
        if data:
            return data
        else:
            return "Отсутствует название вакансии"

    @staticmethod
    def __validation_area(data):
        """
        Статический метод проверки на указание города
        :param data:
        :return:
        """
        if data:
            return data
        else:
            return "Не указан"

    @classmethod
    def new_vacancy(cls, vacancy):
        """
        Класс-метод сохранения свойств вакансии
        :param vacancy:
        :return:
        """
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
