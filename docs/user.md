# API | Пользователи

## Оглавление
* [Авторизация](#auth) <img src="https://img.shields.io/badge/-All-green">
* [Регистрация нового пользователя](#reg) <img src="https://img.shields.io/badge/-All-green">
* [Редактирование пользователя](#edit) <img src="https://img.shields.io/badge/-All-green">
* [Получить список пользователей](#getAll) <img src="https://img.shields.io/badge/-Auth-red">
* [Получить информацию о себе](#getMe) <img src="https://img.shields.io/badge/-Auth-red">
* [Получить информацию о пользователе](#getOnce) <img src="https://img.shields.io/badge/-Auth-red">
* [Удалить пользователя](#delete) <img src="https://img.shields.io/badge/-Auth-red">


<a name="auth"></a>
#### Авторизация
`PUT` /api/user/login
##### Параметры
``` json
{
    "email" : "admin2@mail.ru",
    "hash_pass" : "123"
}
```
|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|email|Электронная почта|Строка|✅|
|password|Пароль в MD5|Текст|✅|

##### Ответ в случае успеха
Код ответа `201`
``` json
{
    "detail": {
        "type": "success",
        "data": {
            "created": "1681131473643",
            "token": "a8feee1dde344911a526ebd78ae9d289"
        }
    }
}
```

##### Ответ в случае ошибки
Код ответа `401`
``` json
{
    "detail": {
        "type": "error"
    }
}
```

<a name="reg"></a>
#### Регистрация нового пользователя
`PUT` /api/user
##### Параметры
``` json
{
    "name" : "Иван Иванович",
    "email" : "admin2@mail.ru",
    "password" : "123"
}
```
|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|name|Имя пользователя|Строка|✅|
|email|Электронная почта|Строка|✅|
|password|Пароль в MD5|Текст|✅|

##### Ответ в случае успеха
Код ответа `201`
``` json
{
    "detail": {
        "type": "success",
        "email": "admin2@mail.ru"
    }
}
```

##### Ответ в случае ошибки
Код ответа `302`
> Пользователь с такой почтой уже зарегистрирован
``` json
{
    "detail": {
        "type": "error",
        "email": "admin2@mail.ru"
    }
}
```


<a name="edit"></a>
#### Редактирование пользователя
`POST` /api/user
##### Параметры
``` json
{
    "name" : "Иван Иванович",
    "photo" : BASE64,
    "email" : "admin2@mail.ru",
    "password" : "123",
    "roles" : [ "admin" ]
}
```

|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|name|Имя пользователя|Строка|❌|
|photo|Картинка в формате base64|Текст|❌|
|email|Электронная почта|Строка|❌|
|password|Пароль в MD5|Текст|❌|
|roles|Массив строк с кодом роли|Текст|❌|

##### Ответ
Код ответа `302`
``` json
{
    "detail": {
        "type": "success"
    }
}
```

<!-- 
<a name="getAllSession"></a>
#### Получить информацию о всех сессиях
`GET` /api/sessions
##### Параметры
Отсутствуют

##### Ответ
Код ответа `200`
``` json
[
    {
        "user": "admin@mail.ru",
        "created": "1680871298570",
        "token": "14139e2eb0354bedb65e326caf3d1ec7"
    },
    {
        "user": "admin2@mail.ru",
        "created": "1680871270238",
        "token": "3c47e64550d446e29b6fca1f4342e068"
    }
]
``` -->

<a name="getAll"></a>
#### Получить список всех пользователей
`GET` /api/user
##### Параметры
Отсутствуют

##### Ответ
Код ответа `200`
``` json
[
    {
        "number": 1,
        "name": "Анастасия",
        "photo": null,
        "email": "admin@mail.ru",
        "roles": [
            "admin"
        ]
    },
    {
        "number": 22,
        "name": "Иван",
        "photo": null,
        "email": "user@mail.ru",
        "roles": [
            "user"
        ]
    }
]
```

<a name="getMe"></a>
#### Получить информацию о себе

> Информация о пользователе предоставляется только авторизированному пользователю под своей учетной записью

`GET` /api/user/me
##### Параметры
Отсутствуют

##### Ответ
Код ответа `200`
``` json
{
    "number": 1,
    "name": "Анастасия",
    "photo": null,
    "email": "admin@mail.ru",
    "orders": [
        {
            "created": "1681476061340",
            "author": "admin@mail.ru",
            "sum": 130,
            "number": 1,
            "description": null,
            "status": "closed",
            "positions": [
                {
                    "number": 1,
                    "name": "Чай",
                    "category": "water",
                    "price": 55,
                    "description": "Черный/Зеленый"
                },
                {
                    "number": 2,
                    "name": "Кофе",
                    "category": "water",
                    "price": 80,
                    "description": "Крепкий"
                }
            ]
        }
    ],
    "roles": [
        "admin"
    ]
}
```

<a name="getOnce"></a>
#### Получить информацию о пользователе

> Информация о пользователе предоставляется только авторизированному пользователю с правами администратора

`GET` /api/user/1
##### Параметры
1 - Номер пользователя

##### Ответ
Код ответа `200`
``` json
{
    "me": true,
    "number": 1,
    "created": null,
    "name": "Анастасия",
    "photo": null,
    "email": "admin@mail.ru",
    "roles": [
        "admin"
    ],
    "orders": [
        {
            "number": 1,
            "created": "1681476061340",
            "status": "closed",
            "sum": 130,
            "description": null,
            "positions": [
                {
                    "number": 1,
                    "name": "Чай",
                    "category": "water",
                    "price": 55,
                    "description": "Черный/Зеленый"
                },
                {
                    "number": 2,
                    "name": "Кофе",
                    "category": "water",
                    "price": 80,
                    "description": "Крепкий"
                }
            ]
        }
    ]
}
```

<a name="delete"></a>
#### Удалить пользователя
`DELETE` /api/user
##### Параметры
``` json
{
    "email" : "admin@mail.ru"
}
```
|Название|Описание|Тип|Обязательность|
|--------|--------|---|:--------------:|
|email|Электронная почта|Строка|✅|

##### Ответ
Код ответа `200`
``` json
{
    "detail": {
        "type": "success"
    }
}
```