from django.db import models
from datetime import datetime
import datetime


class AwardsAndRecognition(models.Model):
    project_name = models.CharField(max_length=20, blank=True, null=True)
    award_title = models.CharField(max_length=10, blank=True, null=True)
    designation = models.CharField(max_length=15, blank=True, null=True)
    award_received_year = models.DateTimeField(auto_now_add=True)
    award_received_month = models.IntegerField(blank=True, null=True)
    award_category = models.CharField(max_length=50, blank=True, null=True)
    award_received_by_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'awards_and_recognition'


class Awards(models.Model):
    award_title = models.CharField(max_length=30, blank=True, null=True)
    winner_name = models.CharField(max_length=30, blank=True, null=True)
    award_category = models.CharField(max_length=30, blank=True, null=True)
    award_id = models.AutoField(primary_key=True)
    awarded_year = models.IntegerField(blank=True, null=True)
    winner_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'awards'


class Comments(models.Model):
    section_title = models.CharField(max_length=30, blank=True, null=True)
    comment_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class Forum(models.Model):
    forum_content_description = models.TextField(blank=True, null=True)
    created_by_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    forum_title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forum'

class ImageFiles(models.Model):
    image_type = models.ImageField()
    id = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'image_files'


class LatestNews(models.Model):
    created_by_id = models.AutoField(primary_key=True)
    news_content = models.TextField(blank=True, null=True)
    news_title = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'latest_news'


class Vacancy(models.Model):
    job_title = models.CharField(primary_key=True, max_length=30)
    candidate_location = models.CharField(max_length=30, blank=True, null=True)
    role_overview = models.TextField(blank=True, null=True)
    eligibility_criteria = models.TextField(blank=True, null=True)
    no_of_openings = models.IntegerField()
    mandatory_skills = models.CharField(max_length=100)
    secondary_skills = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacancy'


class ReferCandidates(models.Model):
    candidate_name = models.CharField(max_length=20, blank=True, null=True)
    candidate_experience = models.IntegerField()
    candidate_email_id = models.CharField(max_length=40, blank=True, null=True)
    candidate_phone_number = models.BigIntegerField(blank=True, null=True)
    candidate_location = models.CharField(max_length=50, blank=True, null=True)
    candidate_qualification = models.CharField(max_length=40, blank=True, null=True)
    refered_at = models.DateTimeField(blank=True, null=True)
    candidate_skills = models.CharField(max_length=500, blank=True, null=True)
    job_title = models.CharField(max_length=35, blank=True, null=True)
    refer_by_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refer_candidates'


class StaffDirectory(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(unique=True, max_length=40)
    phone_number = models.BigIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    doj = models.DateField(blank=True, null=True)
    designation = models.CharField(max_length=40, blank=True, null=True)
    permanent_address = models.CharField(max_length=300, blank=True, null=True)
    current_address = models.CharField(max_length=300, blank=True, null=True)
    password = models.CharField(max_length=25, blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    image_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_directory'
