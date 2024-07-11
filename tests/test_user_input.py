import pytest

from src.user_input import UserInput
from src.vacancy import Vacancy


@pytest.fixture
def test():
    test = UserInput()
    test.get_vacancies_list = [Vacancy(f"test_name {i}", f"test_area {i}", {"to": i * 1000}) for i in range(10)]
    return test
