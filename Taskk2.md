3. Практика: задачи Met1–Met12
Met3

PUT
{
    "id": 2,
    "name": "X",

PATCH

{
    "id": 2,
    "name": "X",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "address": {
        "street": "Victor Plains",
        "suite": "Suite 879",
        "city": "Wisokyburgh",
        "zipcode": "90566-7771",
        "geo": {
            "lat": "-43.9509",
            "lng": "-34.4618"
        }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
        "name": "Deckow-Crist",
        "catchPhrase": "Proactive didactic contingency",
        "bs": "synergize scalable supply-chains"
    }
}
Met4

Статус : 200
{}
DELETE удалить ресурс нет 200 или 204
Все как в теоории
{
    "userId": 1,
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
   }
Met5
{
    "name": "Dup",
    "id": 1
}
{
    "name": "Dup",
    "id": 1
}

Да одинаковы  так как , повторная отправка того же тела просто
перезаписывает то же состояние

"id": 101
  "id": 101
   Метод Post «поле равно значению» идемпотентен, «прибавь
десять» — нет
Met6

| метод  | безопасен? | идемпотентен? | обоснование |
|--------|------------|---------------|-------------|
| GET    | да         | да            | Отправил `GET /users/1` дважды — ответы совпали: данные не изменились. |
| POST   | нет        | нет           | два одинаковых POST создают два разных ресурса (два заказа из двух нажатий). |
| PUT    | нет        | да            | повторная отправка того же тела просто перезаписывает то же состояние. |
| PATCH  | нет        | не всегда     | Выведено из теории 2.3, наблюдения нет: «поле = значение» идемпотентно, «прибавь 10» — нет. |
| DELETE | нет        | да            | Выведено из теории 2.3, наблюдения нет: ресурс удалён один раз, повтор даст другой статус, но мир не изменится. |



Met7.
где записано действие — в
пути, в query или нигде?  /api/getUsers - в пути,тк глагол getusers

/api?action=deleteUser&id=5, -  в quary,тк параметр action=deleteUser

/users/5/remove - в пути,тк глагол remove 

/posts/delete-all - в пути,тк глагол delete-all

/api/getUsers действие в пути. верная пара: GET /api/users
/api?action=deleteUser&... действие в query. верная пара: DELETE /api/users/5
/users/5/remove действие в пути. верная пара: DELETE /users/5
/posts/delete-all действие в пути. верная пара: DELETE /posts

Met8
Команда 1
curl -i -X POST https://jsonplaceholder.typicode.com/posts \
-H "Content-Type: application/json" \
-d '{"title": "Мой пост", "body": "Текст", "userId": 1}'

статусная строка: HTTP/1.1 201 Created

заголовки: Content-Type: application/json; charset=utf-8 и Location: /posts/101

Команда 2

curl -i https://jsonplaceholder.typicode.com/users/3

статусная строка: HTTP/1.1 200 OK

заголовки: Content-Type: application/json; charset=utf-8 и Cache-Control: max-age=43200

Met9

С Accept:
статус: 200 OK
начало тела: { "id": 1, "name": "Leanne Graham", ... }

Без Accept:

статус: 200 OK

начало тела: { "id": 1, "name": "Leanne Graham", ... }

изменилось: ничего - статус, длина и начало тела совпадают

вывод, смотрел ли сервер на Accept: нет, сервер проигнорировал заголовок Accept и вернул JSON в обоих случаях

Met10

Content-Type: application/json →

статус: 201 Created

тело: { "title": "T", "body": "B", "userId": 1, "id": 101 }

Content-Type: text/plain →

статус: 201 Created

тело: { "title": "T", "body": "B", "userId": 1, "id": 101 }

ничего — статус и тело идентичны

Met11

POST /get → статус: 405 Method Not Allowed

GET /post → статус: 405 Method Not Allowed

Код «метод не подходит»: 405 Method Not Allowed

Пришёл в запросе: в обоих — и POST /get, и GET /post.

Met12

A:

один адрес? да (POST /api на всё)

методы по назначению? нет (всё через POST, действие в теле)

статусы со смыслом? нет (один эндпоинт — один статус)

подсказки в ответе? нет

уровень: 0 (болото POX)

B:

один адрес? нет (у каждого ресурса свой адрес /users/1)

методы по назначению? да (GET/PUT/DELETE)

статусы со смыслом? да (200 и 404)

подсказки в ответе? нет

уровень: 2 (HTTP-глаголы)

C:

один адрес? нет

методы по назначению? да

статусы со смыслом? да

подсказки в ответе? да (приходят ссылки на связанные ресурсы)

уровень: 3 (HATEOAS)


