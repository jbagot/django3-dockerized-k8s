from django.db import migrations


def create_animal_types(apps, schema_editor):
    AnimalType = apps.get_model('api', 'AnimalType')

    AnimalType.objects.create(name='Amphibian')
    AnimalType.objects.create(name='Bird')
    AnimalType.objects.create(name='Fish')
    AnimalType.objects.create(name='Invertebrate')
    AnimalType.objects.create(name='Mammal')
    AnimalType.objects.create(name='Reptile')


def create_animals(apps, schema_editor):
    AnimalType = apps.get_model('api', 'AnimalType')
    Animal = apps.get_model('api', 'Animal')

    amphibian = AnimalType.objects.get(name='Amphibian')
    Animal.objects.create(name='Frog', animal_type=amphibian)

    bird = AnimalType.objects.get(name='Bird')
    Animal.objects.create(name='Penguin', animal_type=bird)
    Animal.objects.create(name='Crow', animal_type=bird)

    fish = AnimalType.objects.get(name='Fish')
    Animal.objects.create(name='Shark', animal_type=fish)
    Animal.objects.create(name='Cod', animal_type=fish)

    invertebrate = AnimalType.objects.get(name='Invertebrate')
    Animal.objects.create(name='Snail', animal_type=invertebrate)

    mammal = AnimalType.objects.get(name='Mammal')
    Animal.objects.create(name='Elephant', animal_type=mammal)
    Animal.objects.create(name='Dog', animal_type=mammal)
    Animal.objects.create(name='Cat', animal_type=mammal)
    Animal.objects.create(name='Lion', animal_type=mammal)

    reptile = AnimalType.objects.get(name='Reptile')
    Animal.objects.create(name='Snake', animal_type=reptile)
    Animal.objects.create(name='Komodo dragon', animal_type=reptile)


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial')
    ]

    operations = [
        migrations.RunPython(
            create_animal_types
        ),
        migrations.RunPython(
            create_animals
        ),
    ]
