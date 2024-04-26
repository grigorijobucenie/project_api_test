import allure


@allure.title("Проверка токена на дееспособность")
def test_is_live_token(token):
    token.get_new_token()
    token.check_response_token_is_correct()
