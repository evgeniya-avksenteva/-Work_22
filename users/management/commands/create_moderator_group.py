from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу Модератор и назначает ей права'

    def handle(self, *args, **kwargs):
        group_name = 'Модератор продуктов'
        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            self.stdout.write(f'Группа "{group_name}" создана.')
        else:
            self.stdout.write(f'Группа "{group_name}" уже существует.')

        # Получаем права по codename
        perms_codenames = ['can_unpublish_product', 'can_delete_product']
        perms = Permission.objects.filter(codename__in=perms_codenames)

        # Проверка наличия прав
        found_codenames = perms.values_list('codename', flat=True)
        missing_perms = set(perms_codenames) - set(found_codenames)
        if missing_perms:
            self.stdout.write(f'Внимание: Не найдены права с codename: {", ".join(missing_perms)}')
            # Можно добавить создание этих прав вручную или через миграции
        else:
            # Назначаем права группе
            for perm in perms:
                group.permissions.add(perm)
                self.stdout.write(f'Добавлено право {perm.codename} группе {group_name}.')

        self.stdout.write('Готово.')
