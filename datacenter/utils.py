from django.core.exceptions import ObjectDoesNotExist

from .models import Schoolkid, Commendation, Lesson

def fix_marks(schoolkid):
    schoolkid.mark_set.filter(points__lte=3).update(points=5)


def remove_chastisements(schoolkid):
    schoolkid.chastisement_set.all().delete()

def create_commendation(full_name, subject_title):
    child = Schoolkid.objects.get(full_name__contains=full_name)
    lesson = Lesson.objects.filter(
        year_of_study=child.year_of_study,
        group_letter=child.group_letter,
        subject__title=subject_title
    ).order_by('date').last()
    Commendation.objects.create(
        schoolkid=child,
        subject=lesson.subject,
        teacher=lesson.teacher,
        created=lesson.date,
        text='Хвалю!',
    )
