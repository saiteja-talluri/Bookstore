## @brief Models for the Blog app.


from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver

## @brief This class represents the Profile of Users enrolled in the website.
class Profile(models.Model):
    ## The user associated with the Profile
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    ## The Profile picture of the user
    picture=models.ImageField(upload_to='images/',default = 'pic_folder/None/no-img.jpg')
    ## The firstname picture of the user
    first_name = models.CharField(max_length=30)
    ## The lastname picture of the user
    last_name = models.CharField(max_length=30)
    ## The email-id picture of the user
    email = models.EmailField(max_length=254)
    
    
## @brief This class represents the Genre Interests of Users enrolled in the website.
class Interest(models.Model):
    ## The user associated with the Interest
    user=models.OneToOneField('auth.User',default=1, on_delete=models.CASCADE)
    ## A multiple choice field which represents the selected interests of user
    my_field = MultiSelectField(choices=
        (('Fiction','Fiction'),('LoveandRomance','LoveandRomance'),("Mystery","Mystery"),("Thriller","Thriller"),("ScienceandFiction","ScienceandFiction"),("Fantasy","Fantasy"),("Horror","Horror"),("ActionandAdventure","ActionandAdventure"),("Comedy","Comedy"),("Poetry","Poetry"),("Study","Study"),))
    
    
## @brief This class represents the Documents uploaded in the website
class Document(models.Model):
    ## A variable which represents genre choices available
    genre_choices=(('Fiction','Fiction'),('LoveandRomance','LoveandRomance'),("Mystery","Mystery"),("Thriller","Thriller"),("ScienceandFiction","ScienceandFiction"),("Fantasy","Fantasy"),("Horror","Horror"),("ActionandAdventure","ActionandAdventure"),("Comedy","Comedy"),("Poetry","Poetry"),("Study","Study"),)
    ## A variable which represents rating of a document
    rating = models.FloatField(null=True, blank=True, default=0.0)
    ## A variable which represents no of ratings given to a documnet/book
    no_ratings = models.IntegerField(default=0)
    user=models.ForeignKey('auth.User',default=1, on_delete=models.CASCADE)
    ## A variable which represents uploader of the document
    uploader = models.CharField(max_length=200,default='')
    ## A variable which represents title of the document
    title = models.CharField(max_length=200,default='')
    ## A variable which represents author of the document
    author = models.CharField(max_length=200,default='')
    ## A variable which represents genre of the document
    genre = models.CharField(
        max_length=20,
        choices=genre_choices,
        default='fiction',)
    ## A variable which represents description of the document
    description = models.CharField(max_length=255, blank=True)
    ## A file field which contains the uploaded document
    document = models.FileField(upload_to='documents/')
    ## A image field which contains the cover pic of uploaded document
    image = models.ImageField(upload_to='images/',default = 'pic_folder/None/no-img.jpg')
    ## A variable which describes whether the documents is readable by all users or not 
    public = models.BooleanField(default=True)
    ## A variable which represent list of users who can read the book if it is not public
    rmembers=models.ManyToManyField('auth.User',related_name='rmembers')
    ## A variable represents the published date of the book
    published_date = models.DateTimeField(auto_now_add=True)
    ## A boolean variable which tells whether the document should be during search or not
    searchshow = models.BooleanField(default=True)
    
## @brief This class represents the Rating of the uploaded document given by a user    
class Rate(models.Model):
    ## The user associated with the Rate 
    user=models.ForeignKey('auth.User',default=1, on_delete=models.CASCADE)
    ## The document associated with the Rate
    doc=models.ForeignKey(Document, on_delete=models.CASCADE)
    ## A variable which represents the rating of the document
    rating = models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5)),default=1)


## @brief This class represents the list of users followed by a user    
class Follow(models.Model):
    ## The user associated with the Rate 
    user=models.OneToOneField('auth.User',default=1, on_delete=models.CASCADE)
    ## A variable which contains the list of users followed by the user 
    flist=models.ManyToManyField('auth.User',related_name='owner1')

## @brief This class represents the Communties in the website
class Community(models.Model):
    ## Represents The user who is admin of this community
    admin=models.ForeignKey('auth.User',default=1, on_delete=models.CASCADE)
    ## Contains the list of users who are members of this community
    members=models.ManyToManyField('auth.User',related_name='members')
    ## A variable which represents the name of Community
    name = models.CharField(max_length=200,default='')
    ## A variable which represents description/purpose of community
    description = models.CharField(max_length=255, blank=True)
    ## A variable which contains the list of documents uploaded/belong to this community
    documents=models.ManyToManyField('Document',related_name='docs')
    ## A variable which contains the list of users who sent join request ti this community
    jrequests=models.ManyToManyField('auth.User',related_name='jrequests')

## @brief This class represents the communities in which user is joined 
class Join(models.Model):
    ## The user associated with the Join 
    user=models.ForeignKey('auth.User',default=1, on_delete=models.CASCADE)
    ## A variable which contains the list of communities in which user is a member
    jlist=models.ManyToManyField('Community',related_name='jlist')

## @brief This class represents the Advertisements uploaded in the website
class Advertise(models.Model):
    ## A variable which represents genre choices available
    genre_choices=(('Fiction','Fiction'),('LoveandRomance','LoveandRomance'),("Mystery","Mystery"),("Thriller","Thriller"),("ScienceandFiction","ScienceandFiction"),("Fantasy","Fantasy"),("Horror","Horror"),("ActionandAdventure","ActionandAdventure"),("Comedy","Comedy"),("Poetry","Poetry"),("Study","Study"),)
    user=models.ForeignKey('auth.User',default=1, on_delete=models.CASCADE)
    ## A variable which represents uploader of the document
    uploader = models.CharField(max_length=200,default='')
    ## A variable which represents title of the document
    title = models.CharField(max_length=200,default='')
    ## A variable which represents author of the document
    author = models.CharField(max_length=200,default='')
    ## A variable which represents genre of the document
    genre = models.CharField(
        max_length=20,
        choices=genre_choices,
        default='fiction',)
    ## A variable which represents description of the document
    description = models.CharField(max_length=255, blank=True)
    ## A image field which contains the cover pic of uploaded document
    image = models.ImageField(upload_to='images/',default = 'pic_folder/None/no-img.jpg')
    ## A variable represents the published date of the book
    published_date = models.DateTimeField(auto_now_add=True)


## @brief This class represents the list users who want to read a document if book is private
class Readpending(models.Model):
    ## The user associated with the Readpending
    user=models.ForeignKey('auth.User',default=1, on_delete=models.CASCADE)
    ## The document associated with the ReadPending
    doc=models.ForeignKey(Document, on_delete=models.CASCADE)
    ## A variable which contains the list of users in who want to read this private document
    rplist=models.ManyToManyField('auth.User',related_name='rplist')


    
