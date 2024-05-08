# Selenium Grid для автоматизированного тестирования банковского веб-приложения

## Описание

Этот проект демонстрирует, как настроить тестовое окружение для автоматизированного тестирования банковского веб-приложения с использованием Selenium Grid. В проекте используются язык программирования Python, библиотека Selenium WebDriver и фреймворк для тестирования Pytest.

## Установка зависимостей

1. Установите Python, если у вас его нет. Можно скачать его с [официального сайта](https://www.python.org/downloads/).
2. Установите необходимые библиотеки, выполнив команду:

pip install selenium pytest allure-pytest


## Настройка Selenium Grid

1. Скачайте и установите [Selenium Grid](https://www.selenium.dev/documentation/en/grid/).
2. Запустите Selenium Hub и Selenium Node на вашем компьютере или на удаленных серверах.

## Запуск тестов

1. Укажите адрес удаленного хоста Selenium Grid в `remote_url` в файле `conftest.py`.
2. Запустите тесты, выполнив команду:

pytest


## Структура проекта

- `page_objects.py`: содержит классы, представляющие страницы веб-приложения.
- `utils.py`: содержит вспомогательные методы, такие как расчет чисел Фибоначчи.
- `conftest.py`: содержит фикстуры для настройки тестового окружения.
- `test_bank_operations.py`: содержит тесты операций с банковским аккаунтом.
- `test_login.py`: содержит тесты входа в систему.

## Использование

1. При запуске тестов будет создан удаленный драйвер браузера Chrome, который будет подключаться к Selenium Grid.
2. Тесты будут выполняться на удаленном хосте, а не на локальной машине.
3. Результаты тестирования будут отображаться в отчете Allure.
