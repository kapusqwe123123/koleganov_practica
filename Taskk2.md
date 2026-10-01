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

/api/getUsers действие в: пути верная пара: ____
/api?action=deleteUser&... действие в: query верная пара: ____
/users/5/remove действие в: пути верная пара: ____
/posts/delete-all действие в: пути верная пара: ____
