from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    GENDER = (
        ('M', "Male"),
        ('F', "Female"),
    )

    @staticmethod
    def to_gender(key):
        for item in Profile.GENDER:
            if item[0]==key:
                return item[1]
        return "None"

    firstname = models.CharField(blank=True, max_length=50)
    lastname = models.CharField(blank=True, max_length=50)
    sex = models.CharField(blank=True, max_length=1, choices=GENDER)
    phone = models.CharField(blank=True, max_length=10)


    def get_populated_fields(self):
        """
        To collect form data
        :return:
        """
        fields= {}
        if self.firstname is not None:
            fields['firstname'] = self.firstname
        if self.lastname is not None:
            fields['lastname'] = self.lastname
        if self.sex is not None:
            fields['sex'] = self.sex
        if self.phone is not None:
            fields['phone'] = self.phone

        return fields

    def __str__(self):
        return self.firstname + " " + self.lastname


class Account(models.Model):
    ACCOUNT_UNKNOWN = 0
    ACCOUNT_ADMIN = 1
    ACCOUNT_MEMBER = 2
    ACCOUNT_TYPES = (
        (ACCOUNT_UNKNOWN, "Unknown"),
        (ACCOUNT_ADMIN, "Admin"),
        (ACCOUNT_MEMBER, "Member")
    )

    USER_TYPES = (
        (ACCOUNT_MEMBER, "Member"),
        (ACCOUNT_ADMIN, "Admin")
    )

    @staticmethod
    def to_name(key):
        """
        Parses an integer value to a string representing an account role.
        :param key: The account role as a int
        :return: The integer representation of the account role
        """
        key = key.lower()
        for item in Account.ACCOUNT_TYPES:
            if item[1].lower() == key:
                return item[0]
        return 0

    role = models.IntegerField(default=0, choices=ACCOUNT_TYPES)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.profile.__str__()