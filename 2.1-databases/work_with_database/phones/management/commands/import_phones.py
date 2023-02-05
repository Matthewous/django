import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.http import HttpResponse


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        string_num = 0
        for phone in phones:
            if string_num == 0:
                string_num += 1
            else:
                data = Phone(
                    id = phone[0],
                    name=phone[1],
                    price=phone[2],
                    image= phone[3],
                    image = phone[4],
                    release_date = phone[5],
                    lte_exists = phone[6]
                )
                data.save()
            return HttpResponse ('Данные импортированы')
                