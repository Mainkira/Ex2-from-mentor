import pytest
from pages.second_task import SecondTask


class TestSecondTask:
# Параметризация для всех радиобаттонов
    @pytest.mark.parametrize("radio_button_value, expected_text", [
        ("one", "one"),
        ("two", "two"),
        ("three", "three"),
    ])
    def test_radio_button_selection(self, driver, radio_button_value, expected_text):
        checkboxes_page = SecondTask(driver)
        checkboxes_page.open_page()

        # Выбираем радиобаттон
        checkboxes_page.select_radio_button(radio_button_value)

        # Нажимаем кнопку "Get Results"
        checkboxes_page.click_get_results_button()

        # Получаем текст результата
        results_text = checkboxes_page.get_results_text()

        # Проверяем, что текст результата соответствует ожидаемому тексту
        assert results_text == expected_text, f"Expected '{expected_text}', but got '{results_text}'"