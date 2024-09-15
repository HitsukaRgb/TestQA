Корневая папка проекта должна содержать файл «.env» со следующими полями:

```env
TOKEN="GITHUB_TOKEN"                   # Токен от GitHub
USERNAME="GITHUB_USERNAME"             # Имя пользователя GitHub
REPONAME="GITHUB_REPONAME"             # Имя создаваемого или удаляемого репозитория
SWAGLABS_LOGIN="standard_user"         # Логин от сайта SwagLabs
SWAGLABS_PASSWORD="secret_sauce"       # Пароль от сайта SwagLabs
```
Установка зависимостей

Для установки всех необходимых зависимостей используйте следующую команду в терминале:

```bash
pip install -r requirements.txt
```
Установка браузеров для Playwright  
После установки зависимостей необходимо установить браузеры для Playwright с помощью команды:

```bash
playwright install
```
Запуск тестов
Для запуска тестов в терминале выполните команду:

```bash
pytest
```
