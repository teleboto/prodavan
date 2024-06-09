INSERT INTO categories (category_id, name) VALUES (1, 'Смартфоны');
INSERT INTO categories (category_id, name) VALUES (2, 'Телевизоры');
INSERT INTO categories (category_id, name) VALUES (3, 'Смарт-часы');


INSERT INTO products ("name", "description", "category_id", "price") VALUES
(
	'Nokia C01 Plus',
	'5.45" Смартфон Nokia C01 Plus 16 ГБ синий [ядер - 8x(1.6 ГГц), 1 ГБ, 2 SIM, IPS, 1440x720, камера 5 Мп, 4G, GPS, FM, 3000 мА*ч]',
	1,
	3499
);

INSERT INTO products ("name", "description", "category_id", "price") VALUES
(
	'Coolpad N7 Air',
	'6.51" Смартфон Coolpad N7 Air 16 ГБ черный [ядер - 4x(1.3 ГГц), 2 ГБ, 2 SIM, IPS, 1200x540, камера 13+0.3+0.3 Мп, 4G, GPS, FM, 4000 мА*ч]',
	1,
	3999
);

INSERT INTO products ("name", "description", "category_id", "price") VALUES
(
	'Infinix SMART 7 Plus',
	'6.6" Смартфон Infinix SMART 7 Plus 64 ГБ голубой [ядер - 8x(1.6 ГГц), 3 ГБ, 2 SIM, IPS, 1612x720, камера 13+0.08 Мп, 4G, GPS, FM, 6000 мА*ч]',
	1,
	4249
);



INSERT INTO products ("name", "description", "category_id", "price") VALUES
(
	'Aceline 24HEN1',
	'24" (61 см) LED-телевизор   черный [Direct LED, HD, 60 Гц, HDMI х 3, USB х 2 шт]',
	2,
	12399
);
INSERT INTO products ("name", "description", "category_id", "price") VALUES
(
	'Telefunken TF-LED24S19T2',
	'24" (60 см) LED-телевизор Telefunken TF-LED24S19T2 черный [HD, HDMI х 1, USB х 1 шт]',
	2,
	13200
);
INSERT INTO products ("name", "description", "category_id", "price") VALUES
(
	'Topdevice TDTV24BN02HBK',
	'24" (60 см) LED-телевизор Topdevice TDTV24BN02HBK черный [Direct LED, HD, 60 Гц, HDMI х 3, USB х 2 шт]',
	2,
	14501
);
INSERT INTO products ("name", "description", "category_id", "price") VALUES
(
	'Irbis 24H1T017B',
	'24" (60 см) LED-телевизор Irbis 24H1T017B черный [Direct LED, HD, HDMI х 1, USB х 1 шт]',
	2,
	14349
);



INSERT INTO products ("name", "description", "category_id", "price") VALUES
(
	'KENSHI C55A',
	'Смарт-часы KENSHI C55A [корпус - черный, ремешок - синий, 1.43", AMOLED, 466x466, IP67, Bluetooth, для Android 5.1 и выше, Android 8.0 и выше]',
	3,
	2999
);
INSERT INTO products ("name", "description", "category_id", "price") VALUES
(
	'Canyon Sanchal SW-73',
	'Смарт-часы Canyon Sanchal SW-73 + доп. ремешок [корпус - черный, ремешок - черный, 1.3", IPS, 240x240, IP68, Bluetooth, для Android 5.0 и выше, iOS 10 и выше]',
	3,
	3299
);
INSERT INTO products ("name", "description", "category_id", "price") VALUES
(
	'HUAWEI WATCH FIT 2 Active Edition',
	'Смарт-часы HUAWEI WATCH FIT 2 Active Edition [корпус - черный, ремешок - черный, 1.74", AMOLED, 480x336, Bluetooth, для Android 6.0 и выше, iOS 9 и выше]',
	3,
	8999
);
INSERT INTO products ("name", "description", "category_id", "price") VALUES
(
	'FOSSIL Venture HR',
	'Смарт-часы FOSSIL Venture HR [корпус - золотистый, ремешок - серый, 1.19", AMOLED, 390x390, Bluetooth, NFC, Wi-Fi, для Android 6.0 и выше, iOS 10 и выше]',
	3,
	9100
);

INSERT INTO special ("special_id", "name", "description", "discount") VALUES
(
	1,
	'Летняя распродажа',
	'Спешите купить товары со скидкой 10%',
	10
);

INSERT INTO special ("special_id", "name", "description", "discount") VALUES
(
	2,
	'Осенняя распродажа',
	'Спешите купить товары со скидкой 20%',
	20
);

UPDATE "products"
SET "special_id" = 1
WHERE "product_id" = 2;

UPDATE "products"
SET "special_id" = 1
WHERE "product_id" = 4;
