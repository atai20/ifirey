from django.db import models

class Announcement(models.Model):
    user = models.ForeignKey(User,
                             default=1,
                             null=True,
                             on_delete=models.SET_NULL
                             )
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=400)
    img = models.ImageField(upload_to='media')
    up_total = models.PositiveIntegerField(default=0)
    down_total = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name: "Announcement"
        verbose_name_plural: "Announcement"
        indexes = [models.Index(fields=["created"]),
                   models.Index(fields=["user"])]

    def __str__(self):
        return self.title

