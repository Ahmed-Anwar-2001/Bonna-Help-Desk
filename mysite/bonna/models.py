from django.db import models

# Model for District
class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model for Upozilla
class Upozilla(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.district.name})"


# Model for Union/Ward
class UnionWard(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    upozilla = models.ForeignKey(Upozilla, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.upozilla.name}, {self.district.name})"


# Model for Gram/Area
class GramArea(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    upozilla = models.ForeignKey(Upozilla, on_delete=models.CASCADE)
    union_ward = models.ForeignKey(UnionWard, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.union_ward.name}, {self.upozilla.name}, {self.district.name})"


# Model for Case
class Case(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    upozilla = models.ForeignKey(Upozilla, on_delete=models.CASCADE, null=True)
    union_ward = models.ForeignKey(UnionWard, on_delete=models.CASCADE, null=True)
    gram_area = models.ForeignKey(GramArea, on_delete=models.CASCADE, null=True, blank=True)
    num_people_to_rescue = models.IntegerField()
    description = models.TextField()
    location_google_map_link = models.URLField(max_length=200)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Case {self.id} - {self.district.name}, {self.upozilla.name}"


# Model for Volunteer Group
class VolunteerGroup(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    upozilla = models.ForeignKey(Upozilla, on_delete=models.CASCADE)
    union_ward = models.ForeignKey(UnionWard, on_delete=models.CASCADE)
    gram_area = models.ForeignKey(GramArea, on_delete=models.CASCADE, null=True, blank=True)
    phone_numbers = models.CharField(max_length=200)  # Comma-separated list of numbers
    life_jacket_available = models.BooleanField(default=False)
    boat_available = models.BooleanField(default=False)
    food_available = models.BooleanField(default=False)

    def __str__(self):
        return f"Volunteer Group - {self.district.name}, {self.upozilla.name}"
