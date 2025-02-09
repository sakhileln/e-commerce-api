CREATE TABLE "Users"(
    "id" SERIAL NOT NULL DEFAULT 'None',
    "email" VARCHAR(255) NOT NULL,
    "username" VARCHAR(255) NOT NULL,
    "password_hash" VARCHAR(255) NOT NULL,
    "first_name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "role" VARCHAR(255) NOT NULL DEFAULT 'customer',
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "updated_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "Users" ADD PRIMARY KEY("id");
ALTER TABLE
    "Users" ADD CONSTRAINT "users_email_unique" UNIQUE("email");
ALTER TABLE
    "Users" ADD CONSTRAINT "users_username_unique" UNIQUE("username");
COMMENT
ON COLUMN
    "Users"."role" IS '''admin'' or ''customer''';
CREATE TABLE "Categories"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "description" VARCHAR(255) NOT NULL,
    "parent_category_id" BIGINT NOT NULL
);
ALTER TABLE
    "Categories" ADD PRIMARY KEY("id");
CREATE INDEX "categories_parent_category_id_index" ON
    "Categories"("parent_category_id");
CREATE TABLE "Products"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "description" TEXT NULL,
    "price" DECIMAL(8, 2) NOT NULL,
    "stock" INTEGER NULL DEFAULT '0',
    "category_id" BIGINT NULL,
    "image_url" TEXT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "updated_at" BIGINT NOT NULL
);
ALTER TABLE
    "Products" ADD PRIMARY KEY("id");
CREATE TABLE "Orders"(
    "id" SERIAL NOT NULL,
    "user_id" BIGINT NOT NULL,
    "order_date" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "status" VARCHAR(255) NOT NULL DEFAULT 'processing',
    "total" DECIMAL(8, 2) NOT NULL,
    "shipping_address" TEXT NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "updated_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "Orders" ADD PRIMARY KEY("id");
COMMENT
ON COLUMN
    "Orders"."status" IS '''pending'' ''processing'' ''shipped'' ''delivered'' ''cancelled''';
CREATE TABLE "OrderItems"(
    "id" SERIAL NOT NULL,
    "order_id" BIGINT NOT NULL,
    "product_id" BIGINT NOT NULL,
    "quantity" BIGINT NOT NULL,
    "price_at_order" DECIMAL(8, 2) NOT NULL,
    "subtotal" DECIMAL(8, 2) NOT NULL
);
ALTER TABLE
    "OrderItems" ADD PRIMARY KEY("id");
CREATE TABLE "Cart"(
    "id" SERIAL NOT NULL,
    "user_id" BIGINT NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "Cart" ADD PRIMARY KEY("id");
CREATE TABLE "CartItems"(
    "id" SERIAL NOT NULL,
    "cart_id" BIGINT NOT NULL,
    "product_id" BIGINT NOT NULL,
    "quantity" BIGINT NOT NULL
);
ALTER TABLE
    "CartItems" ADD PRIMARY KEY("id");
ALTER TABLE
    "CartItems" ADD CONSTRAINT "cartitems_cart_id_unique" UNIQUE("cart_id");
ALTER TABLE
    "CartItems" ADD CONSTRAINT "cartitems_product_id_unique" UNIQUE("product_id");
CREATE TABLE "Reviews"(
    "id" SERIAL NOT NULL,
    "user_id" BIGINT NOT NULL,
    "product_id" BIGINT NOT NULL,
    "rating" SMALLINT NOT NULL,
    "comment" TEXT NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "updated_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "Reviews" ADD PRIMARY KEY("id");
CREATE TABLE "Payment"(
    "id" SERIAL NOT NULL,
    "order_id" BIGINT NOT NULL,
    "payment_method" VARCHAR(255) NOT NULL DEFAULT 'cash',
    "payment_status" VARCHAR(255) NOT NULL,
    "transaction_id" VARCHAR(255) NOT NULL,
    "amount" DECIMAL(8, 2) NOT NULL,
    "payment_date" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "Payment" ADD PRIMARY KEY("id");
COMMENT
ON COLUMN
    "Payment"."payment_method" IS '''stripe'' ''paypal'' ''cash''';
CREATE TABLE "Shipping"(
    "id" SERIAL NOT NULL,
    "order_id" BIGINT NOT NULL,
    "shipping_method" VARCHAR(255) NOT NULL,
    "tracking_number" VARCHAR(255) NOT NULL,
    "shipping_status" VARCHAR(255) NOT NULL,
    "estimated_delivery" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "shipped_date" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "Shipping" ADD PRIMARY KEY("id");
ALTER TABLE
    "Shipping" ADD CONSTRAINT "shipping_order_id_unique" UNIQUE("order_id");
COMMENT
ON COLUMN
    "Shipping"."shipping_method" IS '''standard'' ''express''';
COMMENT
ON COLUMN
    "Shipping"."shipping_status" IS '''pending'' ''shipped'' ''delivered''';
ALTER TABLE
    "Categories" ADD CONSTRAINT "categories_id_foreign" FOREIGN KEY("id") REFERENCES "Products"("id");
ALTER TABLE
    "Users" ADD CONSTRAINT "users_id_foreign" FOREIGN KEY("id") REFERENCES "Reviews"("id");
ALTER TABLE
    "Orders" ADD CONSTRAINT "orders_id_foreign" FOREIGN KEY("id") REFERENCES "Payment"("id");
ALTER TABLE
    "Users" ADD CONSTRAINT "users_id_foreign" FOREIGN KEY("id") REFERENCES "Cart"("id");
ALTER TABLE
    "Categories" ADD CONSTRAINT "categories_id_foreign" FOREIGN KEY("id") REFERENCES "Categories"("id");
ALTER TABLE
    "Orders" ADD CONSTRAINT "orders_id_foreign" FOREIGN KEY("id") REFERENCES "Users"("id");
ALTER TABLE
    "Products" ADD CONSTRAINT "products_id_foreign" FOREIGN KEY("id") REFERENCES "Reviews"("id");
ALTER TABLE
    "Products" ADD CONSTRAINT "products_id_foreign" FOREIGN KEY("id") REFERENCES "CartItems"("id");
ALTER TABLE
    "Cart" ADD CONSTRAINT "cart_id_foreign" FOREIGN KEY("id") REFERENCES "CartItems"("id");
ALTER TABLE
    "Products" ADD CONSTRAINT "products_id_foreign" FOREIGN KEY("id") REFERENCES "OrderItems"("id");
ALTER TABLE
    "Orders" ADD CONSTRAINT "orders_id_foreign" FOREIGN KEY("id") REFERENCES "Shipping"("id");
ALTER TABLE
    "Orders" ADD CONSTRAINT "orders_id_foreign" FOREIGN KEY("id") REFERENCES "OrderItems"("id");