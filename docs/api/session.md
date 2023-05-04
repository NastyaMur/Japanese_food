# API | Сессии авторизации

## Оглавление
* [Получить весь список сессий](#getAll) <img src="https://img.shields.io/badge/-Auth-red">
* [Получить список сессий пользователя](#getUser) <img src="https://img.shields.io/badge/-Auth-red">

<a name="getAll"></a>
#### Получить весь перечень сессий
`GET` /api/session
##### Параметры
Отсутствуют

##### Ответ
Код ответа `200`
``` json
[
    {
        "user": "admin@mail.ru",
        "created": "1681487098706"
    },
    {
        "user": "user@mail.ru",
        "created": "1681473275649"
    }
]
```

<a name="getUser"></a>
#### Получить список сессий пользователя
`GET` /api/session/user/1
##### Параметры
1 - Номер пользователя

##### Ответ
Код ответа `200`
``` json
[
    {
        "user": "admin@mail.ru",
        "created": "1681487098706"
    }
]
```
