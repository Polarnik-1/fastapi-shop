# backend/seed_data.py
"""
Скрипт для заполнения базы данных тестовыми данными.
Создает категории и товары для демонстрации работы приложения.
Использует placeholder изображения с unsplash.com.
"""

from app.database import SessionLocal, init_db
from app.models.category import Category
from app.models.product import Product


def create_categories(db):
    """
    Создает категории товаров.

    Args:
        db: Сессия SQLAlchemy

    Returns:
        dict: Словарь созданных категорий {slug: Category}
    """
    categories_data = [
        {"name": "Электроника", "slug": "electronics"},

        {"name": "Книги", "slug": "books"},
        {"name":"Канцелярские принадлежности", "slug":"konzel"}
    ]

    categories = {}
    for cat_data in categories_data:
        category = Category(**cat_data)
        db.add(category)
        categories[cat_data["slug"]] = category

    db.commit()

    # Обновляем объекты после commit для получения ID
    for category in categories.values():
        db.refresh(category)

    return categories


def create_products(db, categories):
    """
    Создает товары в различных категориях.

    Args:
        db: Сессия SQLAlchemy
        categories: Словарь категорий
    """
    products_data = [
        # Electronics


        {
            "name": "Подставка для ноутбуку",
            "description": "Подставка для ноутбука и планшета портативная, алюминиевая, складная с регулировкой высоты и угла на стол.",
            "price": 9.99,
            "category_id": categories["electronics"].id,
            "image_url": "https://cdn1.ozone.ru/s3/multimedia-g/6350696284.jpg"
        },
        {
            "name": "USB-C Hub",
            "description": "USB-разветвитель Ugreen CM473 позволяет увеличить количество доступных USB-разъемов. Устройство особенно полезно при наличии ноутбуков, ПК или моноблоков, в которых не хватает выходов для подсоединения всей необходимой периферии..",
            "price": 10.99,
            "category_id": categories["electronics"].id,
            "image_url": "https://static.re-store.ru/upload/resize_cache/iblock/297/100500_800_140cd750bba9870f18aada2478b24840a/fiwfhshdycl0g94lwytgpera8bdyny4f.jpg"
        },
        {
            "name": "Type-c",
            "description": "Compact wireless keyboard with mechanical switches. Long battery life and ergonomic design. Perfect for both work and gaming.",
            "price": 4.99,
            "category_id": categories["electronics"].id,
            "image_url": "https://ir.ozone.ru/s3/multimedia-1-b/7077794123.jpg"
        },



        # Books
        {
            "name": "Мёртвые Души",
            "description": "«Мертвые души» — произведение Николая Васильевича Гоголя, жанр которого сам автор обозначил как поэму. Изначально задумано как трёхтомное произведение. Первый том был издан в 1842 году. Практически готовый второй том был утерян, но сохранилось несколько глав в черновиках. Третий том был задуман и не начат, о нём остались только отдельные сведения.",
            "price": 2.99,
            "category_id": categories["books"].id,
            "image_url": "https://content.img-gorod.ru/pim/products/images/10/50/0199eace-bab7-7c01-b32b-6cfd9e6c1050.jpg"
        },
        {
            "name": "Преступление и наказание",
            "description": "«Преступление и наказание» — гениальный роман, главные темы которого: преступление и наказание, жертвенность и любовь, свобода и гордость человека — обрамлены почти детективным сюжетом. Многократно экранизированный и не раз поставленный на сцене, он и по сей день читается на одном дыхании.",
            "price": 2.99,
            "category_id": categories["books"].id,
            "image_url": "https://avatars.mds.yandex.net/get-mpic/5426148/img_id3824017904095478322.jpeg/orig"
        },
        {
            "name": "Отцы и Дети",
            "description": "Отцы и дети — знаменитый роман Тургенева, ставший чуть ли не самым значительным произведением в истории о взаимоотношениях поколений. Споры главного героя Евгения Базарова, называающего себя нигилистом и отрицающего расхожие представления о жизни, искусстве, морали, природе человека, и его антагониста Павла Кирсанова, аристократа до мозга костей, состаляют главную проблематику романа.",
            "price": 2.99,
            "category_id": categories["books"].id,
            "image_url": "https://ir.ozone.ru/s3/multimedia-1-t/7557603833.jpg"
        },

        {
            "name": "Набор ручек",
            "description": "Элегантный, стильный, практичный, деловой, оригинальный, изящный, представительный, компактный, качественный, фирменный, классический, удобный, дорогой, эксклюзивный, универсальный набор ручек",
            "price": 1.99,
            "category_id": categories["konzel"].id,
            "image_url": "https://cdn.metro-cc.ru/ru/ru_pim_389677001001_01.png"
        },



        {
            "name": "Набор карандашей",
            "description": "Яркий, мягкий, точный, идеальный, насыщенный, натуральный, тёплый, уютный, разнообразный, выразительный набор карандашей",
            "price": 1.99,
            "category_id": categories["konzel"].id,
            "image_url": "https://ir.ozone.ru/s3/multimedia-y/6269441890.jpg"
        },



        {
            "name": "Набор линеек",
            "description": "Слишком крутые линейки",
            "price": 1.5,
            "category_id": categories["konzel"].id,
            "image_url": "https://i.yapx.ru/dKBue.jpg"
        },




    ]






    for product_data in products_data:
        product = Product(**product_data)
        db.add(product)

    db.commit()
    print(f"✅ Created {len(products_data)} products")


def seed_database():
    """
    Главная функция для заполнения базы данных.
    Создает таблицы, категории и товары.
    """
    print("🚀 Starting database seeding...")

    # Инициализируем БД (создаем таблицы)
    init_db()
    print("✅ Database tables created")

    # Создаем сессию
    db = SessionLocal()

    try:
        # Проверяем, не заполнена ли уже БД
        existing_categories = db.query(Category).count()
        if existing_categories > 0:
            print("⚠️  Database already contains data. Skipping seed.")
            return

        # Создаем категории
        print("📁 Creating categories...")
        categories = create_categories(db)
        print(f"✅ Created {len(categories)} categories")

        # Создаем товары
        print("📦 Creating products...")
        create_products(db, categories)

        print("🎉 Database seeding completed successfully!")

    except Exception as e:
        print(f"❌ Error during seeding: {e}")
        db.rollback()
    finally:
        db.close()




    print("✅ Tables cleared")


def clear_database(db):
    """
    Удаляет все товары и категории из базы данных.

    Args:
        db: Сессия SQLAlchemy
    """
    print("🧹 Clearing existing data...")
    try:
        # Сначала удаляем товары (Foreign Key зависимость)
        num_products = db.query(Product).delete()
        # Затем удаляем категории
        num_categories = db.query(Category).delete()

        db.commit()
        print(f"✅ Deleted {num_products} products and {num_categories} categories.")
    except Exception as e:
        db.rollback()
        print(f"❌ Error during clearing: {e}")
        raise



def seed_database1(force_clear=False):
    """
    Главная функция для заполнения базы данных.

    Args:
        force_clear (bool): Если True, сначала очистит БД.
    """
    print("🚀 Starting database seeding...")
    init_db()
    db = SessionLocal()

    try:
        if force_clear:
            clear_database(db)

        # Проверяем наличие данных, если не была вызвана принудительная очистка
        if not force_clear and db.query(Category).count() > 0:
            print("⚠️  Database already contains data. Use force_clear=True to reset.")
            return

        # ... (далее ваш код создания категорий и продуктов)
        categories = create_categories(db)
        create_products(db, categories)

        print("🎉 Database seeding completed successfully!")

    except Exception as e:
        print(f"❌ Error during seeding: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    # Вы можете менять этот флаг на True, если хотите пересоздать данные
    seed_database1(force_clear=True)