from django.contrib.admin import site

from dates import models


site.register([models.Date, models.DateRange])

