class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=30)


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'price', 'release_date', 'lte_exists', 'slug']


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