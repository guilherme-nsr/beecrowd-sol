SELECT categories.name, SUM(products.amount) FROM categories JOIN products ON products.id_categories = categories.id GROUP BY categories.id;