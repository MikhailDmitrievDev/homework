# Мини Таск менеджер.

### requirements:

- poetry
- fastapi
- uvicorn

## Для проверки корректности работы рекомендую запустить тесты.

## Суть задания:
```
У нас есть 2 маршрута. Создать задачу/прочитать все задачи. 

- Функционал прочитать есть, но работает с ошибкой. (Надо исправить)
- Фунционал создания с валидицией данных нужно дописать. Что будете использовать для валидации
не принципиально.
- Для удобство обернуть в докер.
- Написать как это запустить...
```

## Будет плюсом если:
```
- Добавить комментарии.
- Добавить функционал для хранения данных в другом хранилище. (SQL, NoSQL и пр..)
- Написать в док к JSONStorage, почему это не лучшее решение.
```

### Сущность Task:
```
 id: int
 title: string
 completed: bool
 created_at: datetime
 updated_at: datetime
```
