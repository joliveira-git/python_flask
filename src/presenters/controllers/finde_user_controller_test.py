from faker import Faker
from .find_user_controller import FindUserController
from src.data.test.find_user_spy import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest


faker = Faker()

def test_handler():
    """Testing Handle method"""
    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(query={"user_id": faker.random_number(), "user_name": faker.word()})
    response = find_user_controller.handle(http_request)

    assert find_user_use_case.by_id_and_name_param["user_id"] == http_request.query["user_id"]
    assert find_user_use_case.by_id_and_name_param["user_name"] == http_request.query["user_name"]

    assert response.status_code == 200
    assert response.body

def test_handler_no_query_param_fail():
    """Testing Handle method"""
    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest()
    response = find_user_controller.handle(http_request)

    assert find_user_use_case.by_id_and_name_param == {}
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}


    assert response.status_code == 400
    assert "error" in response.body

def test_handler_invalid_query_param_fail():
    """Testing Handle method"""
    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(query={"fake": 'fake'})
    response = find_user_controller.handle(http_request)

    assert find_user_use_case.by_id_and_name_param == {}
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}


    assert response.status_code == 422
    assert "error" in response.body