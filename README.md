# 🛍Prodavan

**Prodavan** — это чатбот интернет-магазин для Telegram, который позволяет пользователям удобно искать, выбирать и приобретать товары прямо в мессенджере.

## 🔧Технологии

- **Python**: Основной язык программирования для разработки чатбота.
- **pyTelegramBotAPI (telebot)**: Библиотека для работы с API Telegram.
- **PostgreSQL**: Реляционная база данных, используемая для хранения данных о товарах, заказах и пользователях.

## 🤖Основные возможности

- **Просмотр товаров**: Пользователи могут просматривать список доступных товаров и фильтровать их по категориям.
- **Добавление в корзину**: Простое добавление товаров в корзину для последующей покупки.
- **Оформление заказа**: Удобное оформление заказа с последующим отслеживанием его статуса

## ⚙️Начало работы

Чтобы начать использовать Prodavan, выполните следующие шаги:

1. Клонируйте репозиторий

```bash
 git clone https://github.com/teleboto/prodavan.git
```
2. Перейдите в папку TGBot

```bash
 cd TGBot
```
3. Установите библиотеки

```bash
 pip3 install -U -r requirements.txt
```
4. Создайте файл .env и добавьте в него данные

```bash
TELEBOT_API_KEY="Токен бота"
DB_HOST="IP адрес БД"
DB_PORT="Порт БД"
DB_NAME="Название БД"
DB_USER="Пользователь БД"
DB_PASSWORD="Пароль от БД"
```
5. Запустите бота

```bash
python main.py
```
## 📖Структура проекта

- **main.py:** Главный файл для запуска чатбота.
- **handlers/:** Модули для обработки различных типов сообщений и команд.
- **db/:** Содержит модули и репозитории для работы с базой данных.