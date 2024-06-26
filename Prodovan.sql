-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://github.com/pgadmin-org/pgadmin4/issues/new/choose if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.cart
(
    cart_id serial NOT NULL,
    user_id integer,
    product_id integer,
    quantity integer,
    date_added timestamp without time zone,
    CONSTRAINT cart_pkey PRIMARY KEY (cart_id)
);

CREATE TABLE IF NOT EXISTS public.categories
(
    category_id bigserial NOT NULL,
    name character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT categories_pkey PRIMARY KEY (category_id)
);

CREATE TABLE IF NOT EXISTS public.orders
(
    order_id serial NOT NULL,
    user_id integer,
    total_amount numeric(10, 2),
    date_ordered timestamp without time zone,
    status character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT orders_pkey PRIMARY KEY (order_id)
);

CREATE TABLE IF NOT EXISTS public.orderitems
(
    item_id serial NOT NULL,
    order_id integer,
    product_id integer,
    price numeric(10, 2),
    quantity integer,
    total_amount numeric(10, 2),
    CONSTRAINT orderitems_pkey PRIMARY KEY (item_id)
);

CREATE TABLE IF NOT EXISTS public.products
(
    product_id bigserial NOT NULL,
    name character varying(255) COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    category_id integer,
    price numeric(10, 2),
    CONSTRAINT products_pkey PRIMARY KEY (product_id)
);

CREATE TABLE IF NOT EXISTS public.users
(
    user_id bigserial NOT NULL,
    first_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    email character varying(250) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS public.special
(
    special_id serial NOT NULL,
	name character varying(255) COLLATE pg_catalog."default",
    discount integer,
    description text COLLATE pg_catalog."default",
    CONSTRAINT special_pkey PRIMARY KEY (special_id)
);

ALTER TABLE public.products
    ADD COLUMN special_id integer NULL;

ALTER TABLE IF EXISTS public.cart
    ADD CONSTRAINT cart_product_id_fkey FOREIGN KEY (product_id)
    REFERENCES public.products (product_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.cart
    ADD CONSTRAINT cart_user_id_fkey FOREIGN KEY (user_id)
    REFERENCES public.users (user_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.orders
    ADD CONSTRAINT orders_user_id_fkey FOREIGN KEY (user_id)
    REFERENCES public.users (user_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.products
    ADD CONSTRAINT products_category_id_fkey FOREIGN KEY (category_id)
    REFERENCES public.categories (category_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.products
    ADD CONSTRAINT products_special_id_fkey FOREIGN KEY (special_id)
    REFERENCES public.special (special_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.orderitems
    ADD CONSTRAINT orderitems_order_id_fkey FOREIGN KEY (order_id)
    REFERENCES public.orders (order_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.orderitems
    ADD CONSTRAINT orderitems_product_id_fkey FOREIGN KEY (product_id)
    REFERENCES public.products (product_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

END;