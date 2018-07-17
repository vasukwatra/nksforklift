from django.db import models
class NKS(models.Model):
    first_name=models.CharField(max_length=20)
    middle_initial=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    province=models.CharField(max_length=20)
    postal_code=models.IntegerField()
    residential_phone=models.IntegerField()
    cell_phone=models.IntegerField()
    operator_number=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return "First Name = "+self.first_name+"\tMiddle Initial = "+self.middle_initial+"\tLast Name = "+self.last_name+"\tAddress = "+self.address+"\tCity = "+self.city+"\tProvince = "+self.province

    def __int__(self):
        return "Postal Code = "+self.postal_code+"\tResidential Phone = " + self.residential_phone + "\tCell Phone = " + self.cell_phone + "\tOperator Number = " + self.operator_number + "\tDate = " + self.date

