from django.db import models, IntegrityError


class Candidate(models.Model):
    name = models.CharField(max_length=250)
    no_challenges_solved = models.IntegerField()
    votes = models.IntegerField(default=0)
    python_rating = models.IntegerField(default=1)
    dsa_rating = models.IntegerField(default=1)
    cplus_rating = models.IntegerField(default=1)
    java_rating = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Vote(models.Model):
    ip_address = models.CharField(
        max_length=50,
        default="None",
        unique=True
    )
    candidate = models.ForeignKey(
        to=Candidate,
        on_delete=models.CASCADE,
        related_name='vote'
    )

    def save(self, commit=True, *args, **kwargs):

        if commit:
            try:
                self.candidate.votes += 1
                self.candidate.save()
                super(Vote, self).save(*args, **kwargs)

            except IntegrityError:
                self.candidate.votes -= 1
                self.candidate.save()
                raise IntegrityError

        else:
            raise IntegrityError

    def __str__(self):
        return self.candidate.name
