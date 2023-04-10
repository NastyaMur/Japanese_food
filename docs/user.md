# API | Пользователи

## Оглавление
* [Получить информацию о всех сессиях](#getAllSesions) <img src="https://img.shields.io/badge/-Auth-red">
* [Получить информацию о пользователе](#getMe) <img src="https://img.shields.io/badge/-Auth-red">
* [Создание нового пользователя](#create) <img src="https://img.shields.io/badge/-All-green">
* [Авторизация](#login) <img src="https://img.shields.io/badge/-All-green">
* [Удалить пользователя](#delete) <img src="https://img.shields.io/badge/-Auth-red">


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
```

<a name="getMe"></a>
#### Получить информацию о пользователе

> Информация о пользователе предоставляется только авторизированному пользователю под своей учетной записью

`GET` /api/user
##### Параметры
Отсутствуют

##### Ответ
Код ответа `200`
``` json
{
    "name": "Админ",
    "email": "admin@mail.ru",
    "roles": []
}
```

<a name="create"></a>
#### Создание нового пользователя
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

<a name="login"></a>
#### Авторизация
`PUT` /api/login
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