import allure
import pytest
from data.urls import Urls
from data.user_data import PersonData
from web_pages import AuthPage

class TestRecoveryPassword:

    @allure.title('Проверка на переход по клику на Восстановить пароль на странице логина')
    def test_click_password_reset_button(self):
        auth_page = AuthPage()
        auth_page.click_on_account()
        auth_page.click_password_reset_link()
        current_url = auth_page.get_current_url()
        assert current_url == Urls.url_restore

    @allure.title('Проверка на ввод почты и переход после клика по кнопке "Восстановить"')
    def test_enter_email_and_click_reset(self):
        auth_page = AuthPage()
        auth_page.open_link(Urls.url_restore)
        auth_page.set_email_for_reset_password(PersonData.user_login)
        auth_page.click_reset_button()
        auth_page.find_save_button()
        current_url = auth_page.get_current_url()
        assert current_url == Urls.url_reset

    @allure.title('Проверка что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_make_field_active(self):
        auth_page = AuthPage()
        auth_page.open_link(Urls.url_restore)
        auth_page.set_email_for_reset_password(PersonData.user_login)
        auth_page.click_reset_button()
        auth_page.find_save_button()
        auth_page.click_on_show_password_button()
        assert auth_page.find_input_active()