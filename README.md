# tspu_433_db_advanced

### Как установить?
1) Клонируйте и перейдите в репозиторий
```
git clone https://github.com/slippyslime/tspu_433_db_advanced.git
cd tspu_433_db_advanced
```
2) Создайте и запустите виртуальное окружение
```
python -m venv venv
source venv/bin/activate
```
3) Установите зависимости
```
pip install -r requirements.txt
```
4) Перейдите в репозиторий core и выполните миграции
```
cd practice
python manage.py migrate
```
5) Запустите сервер и следуйте инструкциям в консоли
```
python manage.py runserver
```
### Опционально
6) Если нужно зайти в админку создайте нового пользователя с правами
```
python manage.py createsuperuser
```

Пет-проект пользователя slippyslime размещенный для заполнения портфолио
