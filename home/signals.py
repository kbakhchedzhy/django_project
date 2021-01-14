import re

import gender_guesser.detector as gender
from django.db.models.signals import pre_delete, pre_save  # noqa
from django.dispatch import receiver

from home.models import Student


@receiver(pre_save, sender=Student)
def pre_save_artifact(sender, instance, **kwargs):

    full_name = instance.name + ' ' + instance.surname
    instance.normalized_name = re.sub('[^\w\s]|_', '', full_name).lower() # noqa


@receiver(pre_save, sender=Student)
def pre_save_gender(sender, instance, **kwargs):  # noqa
    detector = gender.Detector()
    instance.sex = detector.get_gender(re.sub('[^\w\s]|_', '', instance.name).replace(' ', '')) # noqa


# @receiver(pre_delete, sender=Student)
# def to_do_normalized_name(sender, instance, **kwargs):
#     raise Exception("don't delete")
