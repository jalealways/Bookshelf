from .. import models

def findISBN():
    return models.TbBookBaseInfo.objects.all()