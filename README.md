Проект по автоматизации тестирования на примере заполнения формы регистрации.


Для корректной работы следовать строго инструкции:

•	Скачать проект

•	Положите проект в корневой диск С:

•	Зайти в PyCharm

•	Открыть проект

•	Установить зависимости

•	Перейти в терминал

•	Зайти в корень проекта C:\projectDemo> 

•	Ввести команду для запуска теста в терминале: python -m pytest --alluredir=tests_results/ tests/test_form.py

•	После успешного прохождения теста

•	Открыть командную строку Windows

•	Указать путь к проекту: cd C:\projectDemo

•	Ввести команду для генерации отчета: allure serve tests_results/


Ожидаемый результат:

•	Тест пройден успешно

•	Сформирован отчет Allure