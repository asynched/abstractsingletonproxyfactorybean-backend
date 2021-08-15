from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4


class Teacher(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=63)
    imageUrl = models.CharField("Image url", max_length=255)
    email = models.EmailField(max_length=63)
    about = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')


class Task(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    attachments = models.URLField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    dueDate = models.DateField("Due date")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')


class Class(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Class')
        verbose_name_plural = _('Classes')


class Lesson(models.Model):
    class WeekDays(models.TextChoices):
        SEGUNDA = 'SEG', _('Segunda Feira')
        TERCA = 'TER', _('Terça Feira')
        QUARTA = 'QUA', _('Quarta Feira')
        QUINTA = 'QUI', _('Segunda Feira')
        SEXTA = 'SEX', _('Sexta Feira')

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    cls = models.ForeignKey(Class, verbose_name="Class", on_delete=models.CASCADE)
    schedule = models.CharField(max_length=15)
    weekDay = models.CharField(
        "Week day", choices=WeekDays.choices, max_length=15
    )  # TODO - Text choices

    def __str__(self):
        return f"{self.cls} - {self.schedule}"

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')


class Resource(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    cls = models.ForeignKey(Class, verbose_name="Class", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Resource')
        verbose_name_plural = _('Resources')


class Notice(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    text = models.TextField()
    cls = models.ForeignKey(Class, verbose_name="Class", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Notice')
        verbose_name_plural = _('Notices')
