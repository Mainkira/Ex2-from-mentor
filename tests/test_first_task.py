from pages.first_task import FirstTask


class TestFirstTask:
    def test_button_click(self, driver):
        button_page = FirstTask(driver)
        button_page.open_page()
        button_page.click_button()
        result_text = button_page.get_result_text()
        assert result_text == "Excellent!", f"Expected 'Excellent!', but got '{result_text}'"
