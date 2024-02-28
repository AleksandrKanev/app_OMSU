from django.db import models


class Application(models.Model):
    name_user = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    info_animal = models.CharField(max_length=300)
    address = models.CharField(max_length=100)
    register_date = models.DateField(auto_now_add=True)
    img = models.FileField()

    def __str__(self):
        return f'Заявка: {self.pk}, информация по заявке: {self.info_animal}'


class CardAnimal(models.Model):
    name_animal = models.CharField(max_length=100)
    info_animal = models.CharField(max_length=300)
    img_animal = models.FileField()
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Имя: {self.name_animal}, информация: {self.info_animal}'


class Report(models.Model):
    animal = models.ForeignKey(CardAnimal, on_delete=models.DO_NOTHING, null=True)
    application = models.OneToOneField(Application, on_delete=models.PROTECT, primary_key=True)
    info = models.CharField(max_length=300)
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.animal}'
