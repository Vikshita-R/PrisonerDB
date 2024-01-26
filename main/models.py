from django.db import models

# Create your models here.

class Prisoner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    mobile_numbers = models.TextField(help_text="Enter mobile numbers, separated by commas")
    email = models.EmailField()
    join_date = models.DateField()
    duration = models.CharField(max_length=100)
    exit_date = models.DateField()
    ward = models.CharField(max_length=100)
    

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def get_mobile_numbers(self):
        return [number.strip() for number in self.mobile_numbers.split(',')]

    def set_mobile_numbers(self, numbers):
        self.mobile_numbers = ','.join(numbers)

    mobile_numbers_list = property(get_mobile_numbers, set_mobile_numbers)


class FIR(models.Model):
    fir_number = models.CharField(max_length=20)
    description = models.TextField()
    date_of_registration = models.DateField()
    ps_id_no = models.CharField(max_length=100)

    def __str__(self):
        return f"FIR {self.fir_number}"


class Crime(models.Model):
    prisoner = models.ForeignKey(Prisoner, on_delete=models.CASCADE, related_name='crimes')
    crime_type = models.CharField(max_length=200)
    crime_location = models.CharField(max_length=200)
    crime_date = models.DateField()
    fir = models.OneToOneField(FIR, on_delete=models.CASCADE, related_name='fir', null=True, blank=True)

    def __str__(self):
        return f"{self.prisoner.name} committed {self.crime_type} on {self.crime_date}"
    

class Court(models.Model):
    court_name = models.CharField(max_length=100)
    court_location = models.CharField(max_length=200)   
    prisoner = models.ForeignKey(Prisoner, on_delete=models.CASCADE, related_name='courts')

    def __str__(self):
        return f"Court: {self.court_name}"
    
class Visitor(models.Model):
    visitor_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    prisoner = models.ForeignKey(Prisoner, on_delete=models.CASCADE, related_name='visitor', null=True, blank=True)
    log_in_time = models.DateTimeField()
    log_out_time = models.DateTimeField()
    
    def __str__(self):
        return f"Visitor: {self.visitor_name}, Relationship: {self.relationship}"
    
class Lawyer(models.Model):
    name = models.CharField(max_length=100)
    bar_no = models.CharField(max_length=100)
    prisoners = models.ForeignKey(Prisoner, on_delete=models.CASCADE, related_name="prisoners", null=True, blank=True)
    

    def __str__(self):
        return self.name
