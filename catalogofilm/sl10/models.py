from django.db import models

# Create your models here.

class Immagine(models.Model) :
    img = models.CharField(max_length = 500)

    def __str__(self):
        return self.img

class Lingua(models.Model) :
    name = models.CharField(max_length = 50)
    img = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Attore(models.Model) :
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    date_born = models.DateTimeField()

    def __str__(self):
        return self.name + " : " +  self.surname

class Categoria(models.Model) :
    tipo = models.CharField(max_length = 50)
    descrizione = models.TextField(max_length = 1500)

    def __str__(self):
        return self.tipo

class Film(models.Model) : 
    idFilm = models.IntegerField()
    title = models.CharField(max_length = 100)
    year = models.DateField()
    director = models.CharField(max_length = 100)

    categories = models.ManyToManyField(Categoria,blank = True)
    actors = models.ManyToManyField(Attore,blank = True)

    languages = models.ManyToManyField(Lingua,blank = True)
    immages = models.ManyToManyField(Immagine,blank = True)

    def __str__(self):
        return self.title

