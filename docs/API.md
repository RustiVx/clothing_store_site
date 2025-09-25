# API спецификация

## Публичные страницы HTML

*   GET/ - главная страница.
*   POST/shop/<id> - страница оформления заявки на товар.

## JSON API

GET/api/product - список товаров

```
 <img src="{{ url_for('static', filename='img/' ~ product[4]) }}" alt="{{ product[1] }}" style="border-radius: 8px; width: 100%; height: auto; margin-bottom: 12px;">
 <h3 style="font-size: 24px; margin: 8px 0;">{{ product[1] }}</h3>
 <p style="font-size: 16px; margin: 4px 0;">Для роста: {{ product[5] }}</p>
 <p class="price" style="font-weight: bold; margin: 12px 0; font-size: 20px; color: #0077cc;">{{ product[3] }} ₽</p>
```

POST/api/orders - офррмление заявки на товар

```
 <input type="text" name="name" placeholder="Ваше имя" required style="padding: 10px; font-size: 16px; border-radius: 8px; border: 1px solid #ccc;">
 <input type="tel" name="phone" placeholder="Телефон" required pattern="[\d\s\+\-\(\)]{7,}" style="padding: 10px; font-size: 16px; border-radius: 8px; border: 1px solid #ccc;">
 <textarea name="comment" placeholder="Комментарий к заказу" style="padding: 10px; font-size: 16px; border-radius: 8px; border: 1px solid #ccc; resize: vertical;"></textarea>
```

## Статусы и ошибки

Ошибка 404 - страница не найдена.