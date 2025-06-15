from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Удаляет все данные и добавляет тестовые продукты'

    def handle(self, *args, **kwargs):
        # Удаление всех данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создание категорий
        category1 = Category.objects.create(
            name='Напольные покрытия',
            description='Напольные покрытия для дома'
        )
        category2 = Category.objects.create(
            name='Электроника',
            description=''
        )
        category3 = Category.objects.create(
            name='Книги',
            description=''
        )

        # Создание продуктов
        Product.objects.create(
            name='Ламинат Дуб белый 2,05м2/упаковка',
            description='Ламинат из новой коллекции создаст в вашем доме атмосферу уюта и благородства.',
            image='',
            category=category1,
            purchase_price='600.00',
            created_at='2025-04-01',
            updated_at='2025-06-10'
        )

        Product.objects.create(
            name='Книга "Python для начинающих"',
            description='Учебник по Python',
            image='',
            category=category3,
            purchase_price='1500.00',
            created_at='2024-04-27',
            updated_at='2024-04-27'
        )

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно добавлены'))
