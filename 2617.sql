SELECT products.name AS product, providers.name AS provider FROM products JOIN providers ON products.id_providers = providers.id WHERE providers.name = 'Ajax SA';
