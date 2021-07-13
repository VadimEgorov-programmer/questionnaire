# questionnaire
Тестовое задание.

Задача: спроектировать и разработать API для системы опросов пользователей.

Функционал для администратора системы:

- авторизация в системе(регистраниця не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название,
 дата старта, дата окончания, описание. 
 После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст
 вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ
  с выбором нескольких вариантов)


Функционал для пользователей системы:
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве 
идентификатора пользователя в API передаётся числовой ID, по которому 
сохраняются ответы пользователя на вопросы; один пользователь может 
участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по 
ответам (что выбрано) по ID уникальному пользователя


Использовать следующие технологии:
Django 2.2.10, Django REST framework.

Результат выполнения задачи:
- исходный код приложения в github(только на github, публичный репозиторий)
- инструкция  по разворачиванию приложения (в docker или локально)
- документация по API

При написании кода использовал Python 3.7

Создал документацию с помощью плагина drf-yasg (автогенерация).

Документация доступна по ссылкам:

Внимание! Документация лучше в swagger

``http://127.0.0.1:8000/redoc/`` 

и

``http://127.0.0.1:8000/swagger/``


Установка зависимостей из файла requirements.txt

`pip install -r requirements.txt`

Не забудьте выполнить следующие команды:

Команды миграций

` python manage.py makemigrations`

` python manage.py migrate `

Для создания суперпользователя вводим команду:

` python manage.py createsuperuser` 
К примеру пользователь admin с паролем 123456

Команда для запуска приложения 

` python manage.py runserver`

Приложение будет доступно по стандартному адресу (локальному)

Для получения токена пользователя можно использовать команду:

Использую Git Bash для написания команд ниже которые находятся ниже.

Пример написания команды(подставляйте ваши данные):

``curl --location --request GET 'http://localhost:8000/api/login/'
 --form 'username=admin'  --form 'password=123456'`` 

Для создания опроса можно использовать команду: 

Пример написания команды(подставляйте ваши данные):

``curl --location --request POST 'http://localhost:8000/api/pollsApp/create/'
 --header 'Authorization: Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'
  --form 'poll_name=test'  --form 'pub_date=2021-02-03T14:18:15Z'
    --form 'end_date=2021-02-03T14:18:15Z'  --form 'poll_description=test'``
    
Для обновления опроса можно использовать команду:

Пример написания команды(подставляйте ваши данные):

``curl --location --request PATCH 
'http://localhost:8000/api/pollsApp/update/1/'  --header 'Authorization: 
Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'  --form 'poll_name=test'  
--form 'end_date=2021-02-03T14:18:15Z' --form 'poll_description=test'``

Для удаления опроса можно использовать команду:

Пример написания команды:

``curl --location --request DELETE 
'http://localhost:8000/api/pollsApp/update/1/'  --header 
'Authorization: Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'``

Для просмотра всех опросов можно использовать команду:

Пример написания команды:

``curl --location --request GET 'http://localhost:8000/api/pollsApp/view/'  
--header 'Authorization: Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'``

Для просмотра текущих опросов:

Пример написания команды:

``curl --location --request GET 
'http://localhost:8000/api/pollsApp/view/active/'  --header 
'Authorization: Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'``

Создание вопроса:

Пример написания команды:

``curl --location --request POST 'http://localhost:8000/api/question/create/'
  --header 'Authorization: Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'
    --form 'poll=4'  --form 'question_text=test'  --form 'question_type=one'``
    
Обновляем вопрос:

Пример написания команды:

``curl --location --request PATCH 
'http://localhost:8000/api/question/update/1/'
  --header 'Authorization: Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'
    --form 'poll=5' --form 'question_text=test2'
      --form 'question_type=test2'``
      
Для удаления вопроса:

Пример написания команды:

``curl --location --request 
DELETE 'http://localhost:8000/api/question/update/1/'
  --header 'Authorization: Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'``
  
Для создания выбора:

Пример написания команды:

``curl --location --request POST 'http://localhost:8000/api/choice/create/'
  --header 'Authorization: Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'
    --form 'question=2'  --form 'choice_text=choice'``
    
Для обновления выбора:

Пример написания команды:

``curl --location --request PATCH
 'http://localhost:8000/api/choice/update/15/'
   --header 'Authorization: Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'
     --form 'question=test'  --form 'choice_text=test'``
     
     
Для удаления выбора:

Пример написания команды:

`` curl --location --request DELETE
 'http://localhost:8000/api/choice/update/15/'
   --header 'Authorization: Token
    04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1' \ ``
    
Для создания ответа:

Пример написания команды:

`` curl --location --request POST 'http://localhost:8000/api/answer/create/'
  --header 'Authorization: Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'
    --form 'poll=5'  --form 'question=test'
      --form 'choice=7'  --form 'choice_text=test'``
      
Для обновления ответа:

Пример написания команды:

``curl --location --request PATCH
 'http://localhost:8000/api/answer/update/5'
   --header 'Authorization: Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'
     --form 'poll=2'  --form 'question=4'  --form 'choice=null'
       --form 'choice_text=null'``
       
Для удаления ответа:

Пример написания команды:

``curl --location --request DELETE
 'http://localhost:8000/api/answer/update/2'
   --header 'Authorization:
    Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'``
    
Для показа ответов пользователя:

Пример написания команды:

``curl --location
 --request GET
  'http://localhost:8000/api/answer/view/  user_id    '
    --header 'Authorization:
     Token 04dbb6d9af2b8ec8e0ad0edb606adeff1a2748e1'``


















