Ответы на задачи Web3-Web12
Web 3

Метод : GET
Статус : 304
Type : document
Кол-во пользователей : 10
Запрос со статусом не 200 : Нет

Web 4
Вернулось комментариев : 5

Web 5
Обьектов пришло 3 
Айди 1-1 Айди 2-2 Айди 3-3

Web 6
Количество ответов для postId=3:5
Количество ответов для postId=4:5
Это погинация показывает на какой странице находиться user

Web 7

Гипотеза : Думаю,что параметр _limit задает ограничение обьектов в ответе

https://jsonplaceholder.typicode.com/posts?_limit=2 кол-во ответов -2
https://jsonplaceholder.typicode.com/posts?_limit=7 кол-во ответов -7

Web 8 

ссылка 1 https://jsonplaceholder.typicode.com/comments?postId=7&_limit=4
схема = https://
хост= jsonplaceholder.typicode.com
порт = 443
путь = comments
Query = postId=7&_limit=4

ссылка 2 http://localhost:8080/tasks?page=2&sort=date
схема- http://
хост - localhost:8080
порт - 8080
путь - tasks
Query - page=2&sort=date

ссылка 3 https://api.example.com:3000/users/42/posts?status=active.
схема- https://
порт- 3000
путь- users/42
Query- posts?status=active.

web 9

https://jsonplaceholder.typicode.com/posts?userId=2 = обьектов 10
https://jsonplaceholder.typicode.com/users/2/posts = обьектов 10
Результат один и тот же,дороги были разные

web 10

СТАТУС 200 GET /users/1, = https://jsonplaceholder.typicode.com/users/1 =вывел 1 из user
СТАТУС 404  GET /users/11 = не найдено
СТАТУС 200 GET /users/1?foo=bar =  https://jsonplaceholder.typicode.com/users/1?foo=bar = пользователь отмечает 11 пользователя,это ломает ресурс

web 11

https://jsonplaceholder.typicode.com/users
Content-Type
application/json; charset=utf-8 application/json; charset=utf-8
Content-Length
1847
Это ответы Json




web 12

Первая страница (_page=1) : 5 обьектов , id первого обьекта - 1
вторая страница (_page=2) : 5 обьектов , id первого обьекта - 6
параметр _page указывает номер отображаемой при пагинации , сдвигая последовательность id дальше
