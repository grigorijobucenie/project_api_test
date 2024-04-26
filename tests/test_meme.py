import allure


@allure.title('Получение списка всех мемов')
def test_get_all_list_meme(meme_page, new_token):
    meme_page.get_list_all_meme(new_token)
    meme_page.check_get_leist_meme()


@allure.title('Получение информации о меме по id')
def test_meme_for_id(meme_page, new_token):
    meme_page.get_list_all_meme(new_token)
    meme_page.get_one_meme(new_token)
    meme_page.check_info_about_meme_for_id()


@allure.title('Создание нового мема')
def test_add_new_meme(meme_page, new_token):
    meme_page.add_new_meme(new_token)


@allure.title('Обновление информации о меме')
def test_update_meme(meme_page, new_token, create_meme_and_delete):
    meme_page.update_data_meme(new_token, create_meme_and_delete)


@allure.title('Удаление мема')
def test_delete_meme(meme_page, new_token):
    meme_page.add_new_meme(new_token)
    id_meme = meme_page.created_new_meme.json()['id']
    meme_page.delete_meme(new_token, id_meme)
