from django.db import models


# Create your models here.
class Order(models.Model):
    start_date = models.DateTimeField('start_date')
    end_date = models.DateTimeField('end_date')
    customer_name = models.CharField('customer_name', max_length=64, default='unknown')
    manager_name = models.CharField('staff_name', max_length=64, default='unknown')
    storage_num = models.IntegerField('storage_num', default=0)

    def __str__(self):
        return 'Order from {start_date} to {end_date} for customer: {customer_name}'\
            .format(start_date=self.start_date,
                    end_date=self.end_date,
                    customer_name=self.customer_name)

