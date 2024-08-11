from django.db import models

class HeroSection(models.Model):
    # Image for the hero portrait
    portrait_image = models.ImageField(upload_to='Media/', help_text='Upload a portrait image for the hero section.')

    # Content for the hero section
    greeting = models.CharField(max_length=255, help_text='Greeting message, e.g., "Namasté, I\'m"')
    name = models.CharField(max_length=255, help_text='Name to display in the hero section.')
    profession = models.CharField(max_length=255, help_text='Profession or title, e.g., "Frontend Developer"')
    tagline = models.TextField(help_text='Tagline or description for the hero section.')

    # Social media links
    github_link = models.URLField(blank=True, null=True, help_text='Link to GitHub profile.')
    twitter_link = models.URLField(blank=True, null=True, help_text='Link to Twitter profile.')
    instagram_link = models.URLField(blank=True, null=True, help_text='Link to Instagram profile.')
    youtube_link = models.URLField(blank=True, null=True, help_text='Link to YouTube channel.')
    linkedin_link = models.URLField(blank=True, null=True, help_text='Link to LinkedIn profile.')
    discord_link = models.URLField(blank=True, null=True, help_text='Link to Discord server.')

    # Contact and portfolio section
    contact_link = models.URLField(help_text='Link to the contact section.')
    portfolio_link = models.URLField(help_text='Link to the portfolio section.')

    def __str__(self):
        return f'Hero Section - {self.name}'


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    icon = models.ImageField(upload_to='Media/projects/icons/')
    banner = models.ImageField(upload_to='Media/projects/banners/')
    stacks = models.CharField(max_length=255, blank=True, null=True)  # Technology stacks used

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300,null=True)
    url = models.URLField()
    image = models.ImageField(upload_to='Media/certificates/')
    tag = models.CharField(max_length=50, blank=True, null=True)  # e.g., Gaming, Symposium

    def __str__(self):
        return self.title
    
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='Media/courses/')
    url = models.URLField()
    tag = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    portrait = models.ImageField(upload_to='Media/about_me/', help_text='Upload a portrait image')
    bio = models.TextField(help_text='Write your biography here')

    def __str__(self):
        return "About Me Section"

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

class Skill(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the skill')
    image = models.ImageField(upload_to='skills/', help_text='Upload the skill icon')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"