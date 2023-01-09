from django.db import models

# Create your models here.
class Emp_data (models.Model):
    DailyRate = models.FloatField(("DailyRate"))
    Department = models.CharField(("Department"), max_length=255)
    DistanceFromHome = models.IntegerField(("DistanceFromHome"))
    Education = models.IntegerField(("Education"))
    EducationField = models.CharField(("EducationField"), max_length=255)
    EmployeeNumber = models.IntegerField(("EmployeeNumber"))
    EnvironmentSatisfaction = models.IntegerField(("EnvironmentSatisfaction"))
    Gender = models.CharField(("Gender"), max_length=255)
    JobRole = models.CharField(("JobRole"), max_length=255)
    JobSatisfaction = models.IntegerField(("JobSatisfaction"))
    NumCompaniesWorked = models.IntegerField(("NumCompaniesWorked"))
    PercentSalaryHike = models.FloatField(("PercentSalaryHike"))
    PerformanceRating = models.IntegerField(("PerformanceRating"))
    RelationshipSatisfaction = models.IntegerField(("RelationshipSatisfaction"))
    TrainingTimesLastYear = models.IntegerField(("TrainingTimesLastYear"))
    WorkLifeBalance = models.IntegerField(("WorkLifeBalance"))
    YearsSinceLastPromotion = models.IntegerField(("YearsSinceLastPromotion"))