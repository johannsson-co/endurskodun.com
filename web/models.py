from django.db import models

# Create your models here.

class HomePage(models.Model):

    page1_title = models.CharField(max_length=128, help_text='Use <span> tag to highlight words')
    page1_subtitle = models.CharField(max_length=128)
    

    page2_title = models.CharField(max_length=128)
    page2_subtitle = models.CharField(max_length=128)
    
    page2_bullet_title = models.CharField(max_length=128, blank=True, null=True)
    page2_bullet1_title = models.CharField(max_length=64, blank=True, null=True)
    page2_bullet1_text = models.CharField(max_length=256, blank=True, null=True)
    page2_bullet2_title = models.CharField(max_length=64, blank=True, null=True)
    page2_bullet2_text = models.CharField(max_length=256, blank=True, null=True)
    page2_bullet3_title = models.CharField(max_length=64, blank=True, null=True)
    page2_bullet3_text = models.CharField(max_length=256, blank=True, null=True)
    page2_sidebullet_title = models.CharField(max_length=32, blank=True, null=True)
    page2_sidebullet_text = models.CharField(max_length=256, blank=True, null=True)
    

    page3_title = models.CharField(max_length=128, blank=True, null=True, help_text='Keep this blank to remove section 3 entirely')
    page3_subtitle = models.CharField(max_length=128, blank=True, null=True)
    page3_service1_title = models.CharField(max_length=128, blank=True, null=True)
    page3_service1_text = models.CharField(max_length=128, blank=True, null=True)
    page3_service2_title = models.CharField(max_length=128, blank=True, null=True)
    page3_service2_text = models.CharField(max_length=128, blank=True, null=True)
    page3_service3_title = models.CharField(max_length=128, blank=True, null=True)
    page3_service3_text = models.CharField(max_length=128, blank=True, null=True)
    page3_service4_title = models.CharField(max_length=128, blank=True, null=True)
    page3_service4_text = models.CharField(max_length=128, blank=True, null=True)

    page4_title = models.CharField(max_length=128, blank=True, null=True)
    page4_subtitle = models.CharField(max_length=128, blank=True, null=True)
    page4_address = models.CharField(max_length=32, blank=True, null=True)
    page4_phone = models.CharField(max_length=32, blank=True, null=True)
    page4_email = models.EmailField(blank=True, null=True)

