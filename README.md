# THE ​BOOKSTORE

### The​ ​Brogrammers

- Saiteja​ ​Talluri​ ​-​ ​​ ​ 160050098 
- Saiteja​ ​Nangunoori​ ​​ ​-​ ​ 160050089 
- Sathvik​ ​Kollu​ ​Reddy​ ​-​ ​ 160050077 

## ABSTRACT

We​ ​built​ ​an​ ​online​ ​website​ ​which​ ​serves​ ​as​ ​a​ ​bookstore​ ​for​ ​reading​ ​and​ ​lending​ ​manuals, journals​ ​and​ ​books.

```
● Every​ ​user​ ​can​ ​read, rate​ ​and​ ​review​ ​the​ ​books.
● User​s ​can​ ​not​ ​only​ ​read​ ​but​ ​can​ ​also​ ​upload/advertise​ ​his​ ​own​ ​books​ ​or​ ​materials.
● Users​ ​can​ ​follow​ ​uploaders​ ​and​ ​also​ ​chat​ ​with​ ​them​ ​via​ ​a​ ​simple​ ​chat​ ​box.
● Group​ ​of​ ​users​ ​can​ ​also​ ​form​ ​a​ ​community​ ​depending​ ​on​ ​their​ ​interests.​ ​The​ ​materials shared​ ​in​ ​the​
  community​ ​are​ ​accessible​ ​to​ ​everyone​ ​in​ ​it.
```

## MOTIVATION

```
● Many​ ​of​ ​us​ ​would​ ​have​ ​faced​ ​the​ ​problem​ ​at​ ​some​ ​point​ ​or​ ​the​ ​other​ ​to​ ​find​ ​whether someone​ ​in​ ​our​ ​
  friends​ ​or​ ​classmates​ ​had​ ​a​ ​hard​ ​copy​ ​of​ ​our​ ​favourite​ ​novel/comic​ ​and are​ ​willing​ ​to​ ​lend​ ​the​ ​book.
● So​ ​we​ ​thought​ ​of​ ​creating​ ​a​ ​website​ ​that​ ​enables​ ​the​ ​users​ ​to​ ​​ ​know​ ​the​ ​owner​ ​of​ ​​ ​a​ ​hard copy​ ​for​ ​
  the​ ​book​ ​they​ ​are​ ​searching​ ​for​ ​and​ ​can​ ​also​ ​chat​ ​with​ ​the​ ​owner​ ​through​ ​a simple​ ​chat​ ​interface​ ​and​ ​
  borrow​ ​the​ ​book​ ​from​ ​him​ ​for​ ​a​ ​week/month.
● We​ ​also​ ​face​ ​many​ ​problems​ ​while​ ​collecting​ ​the​ ​reference​ ​materials​ ​or​ ​​ ​class​ ​notes related​ ​to​ ​the​ ​
  courses​ ​at​ ​the​ ​start​ ​or​ ​at​ ​the​ ​time​ ​of​ ​exams,​ ​so​ ​we​ ​wanted​ ​to​ ​create​ ​a website​ ​​ ​that​ ​can​ ​help​ ​peers​ ​
  by​ ​preserving​ ​​ ​the​ ​material​ ​which​ ​was​ ​uploaded​ ​by​ ​the seniors​ ​or​ ​professors​ ​over​ ​years​ ​in​ ​a​ ​
  community​ ​and​ ​accessible​ ​to​ ​only​ ​members​ ​of​ ​that community.
```

## PROBLEM ​STATEMENT


```
● Creating​ ​a​ ​web​ ​application​ ​where​ ​you​ ​can​ ​read/rate/review/upload books/materials/journals.
● Implementing​ ​database​ ​searches​ ​so​ ​that​ ​users​ ​can​ ​search​ ​books​ ​by​ ​genre/authors.
● The​ ​website​ ​should​ ​also​ ​notify/suggest​ ​the​ ​user​ ​whenever​ ​a​ ​new​ ​material​ ​of​ ​his​ ​interest​ ​is uploaded 
  in​ the​ ​site.
● It​ ​should​ ​have​ ​the​ ​feature​ ​of​ ​forming​ ​groups/communities​ ​such​ ​that​ ​the​ ​materials uploaded​ ​in​ ​the​ ​
  group​ ​are​ ​accessible​ ​only​ ​to​ ​the​ ​members​ ​of​ ​the​ ​group.
● Creating​ ​chat​ ​boxes​ ​so​ ​that​ ​users​ ​can​ ​communicate​ ​with​ ​uploaders​ ​and​ ​borrow​ ​books from​ ​them.
```

## SOFTWARE ​REQUIREMENTS

```
- Front end ​- ​Basic web ​designing
     1. HTML
     2. CSS
     3. BOOTSTRAP
     4. JAVASCRIPT
- Backend
​ ​​ ​​ ​​ ​​ ​​5.​ ​​ ​Django
- Documentation
​ ​​ ​​ ​​ ​​ ​​6.​ ​​ ​Latex
​ ​​ ​​ ​​ ​​ ​7.​ ​​ ​Doxygen
- For version ​ control
​ ​​ ​​ ​​ ​​ ​8.​ ​​ ​Git
```

## IMPLEMENTATION

```
● Used​ ​Django​ ​Models​ ​to​ ​make​ ​suitable​ ​classes​ ​to​ ​represent​ ​objects​ ​such​ ​as​ ​Profile, Document, 
  Community,​ ​Advertise,​ ​Join​ ​etc.
● Used​ ​Django​ ​ModelForms​ ​to​ ​generate​ ​forms​ ​to​ ​edit​ ​models.
● Used​ ​Django​ ​Authentication​ ​System​ ​to​ ​authenticate​ ​users​ ​in​ ​the​ ​login​ ​page.
● Used​ ​Django-Filters​ ​to​ ​implement​ ​searching​ ​of​ ​Documents​ ​​ ​and​ ​Ads
● Used​ ​Django-private-chat​ ​to​ ​implement​ ​chat​ ​feature
● Used​ ​SQLite3​ ​to​ ​manage​ ​the​ ​database
● Used​ ​HTML,​ ​CSS​ ​and​ ​Bootstrap​ ​to​ ​create​ ​the​ ​front​ ​end​ ​of​ ​the​ ​website.
```

## FEATURES (Promised) ​​ ​​ :

```
1. Login
2. Register
3. Search​ ​by​ ​genre,​ ​author,​ ​title
4. Rate/Review
5. Upload
6. Chat​ ​with​ ​uploader
7. Community
8. Follow​ ​people
9. Checking​ ​copyrights
```

**LOGIN** ​​ ​ **:**
Users​ ​can​ ​login​ ​through​ ​their​ ​username​ ​and​ ​password.
**REGISTER** ​ ​ **:**
Users​ ​can​ ​​ ​register​ ​by​ ​providing​ ​their​ ​personal​ ​details​ ​which​ ​include​ ​their
favourite​ ​authors​ ​and​ ​their​ ​interests.
**SEARCH** ​ ​ **BY** ​ ​ **GENRE** ​ ​ **,** ​ ​ **AUTHOR,** ​ ​ **TITLE** ​ ​ **:**
Users​ ​can​ ​search​ ​by​ ​genre,​ ​author,​ ​title.
**RATE** ​ ​ **/** ​ ​ **REVIEW** ​ ​ **:**
Users​ ​can​ ​rate​ ​and​ ​review​ ​the​ ​books/materials​ ​that​ ​are​ ​up​ ​on​ ​​ ​the
website.
**UPLOAD** ​ ​ **:**
a. Users​ ​can​ ​upload​ ​books​ ​(provided​ ​there​ ​is​ ​no​ ​problem​ ​with​ ​copyrights​ ​of
the​ ​book)​ ​and​ ​materials​ ​related​ ​to​ ​a​ ​particular​ ​community
b. Users​ ​can​ ​upload​ ​the​ ​preview​ ​of​ ​the​ ​hardcopy​ ​they​ ​have​ ​with​ ​them​ ​(which
they​ ​are​ ​willing​ ​to​ ​lend)
c. we​ ​check​ ​the​ ​page​ ​next​ ​to​ ​title​ ​page​ ​whether​ ​it​ ​has​ ​copyright​ ​issues​ ​or
not​ ​by​ ​scanning​ ​it.


#### CHAT ​ ​ WITH ​ ​ UPLOADER ​ ​ :

```
Users​ ​can​ ​personally​ ​chat​ ​with​ ​the​ ​uploaders​ ​about​ ​a​ ​book​ ​and​ ​discuss​ ​their​ ​views
or​ ​make​ ​a​ ​deal​ ​to​ ​borrow​ ​the​ ​book​ ​(provided​ ​uploader​ ​have​ ​a​ ​hard​ ​copy)
COMMUNITY ​ ​ :
● Users​ ​can​ ​form​ ​a​ ​community​ ​based​ ​on​ ​interests​ ​,courses​ ​they​ ​have​ ​taken,​ ​institute
they​ ​belong​ ​to,etc.
● Users​ ​can​ ​upload​ ​materials​ ​related​ ​to​ ​the​ ​members​ ​of​ ​the​ ​community.
● Content​ ​can​ ​be​ ​accessed​ ​only​ ​by​ ​members​ ​of​ ​community.
FOLLOW ​ ​ PEOPLE ​ ​ :
Users​ ​can​ ​follow​ ​an​ ​individual​ ​so​ ​that​ ​when​ ​he​ ​or​ ​she​ ​uploads​ ​and
book​ ​they​ ​​ ​get​ ​a​ ​notification.
```
## FEATURES (Completed) ​​ ​​ :

1. Login
2. Register
3. Search​ ​by​ ​genre,​ ​author,​ ​title
4. Rate/Review
5. Upload
6. Chat​ ​with​ ​uploader
7. Community
8. Follow​ ​people
    We​ ​had​ ​successfully​​ ​​implemented​ ​almost​ ​all​ ​the​ ​features​ ​except​ ​that​ ​we​ ​are​ ​not​ ​able​ ​to
    scan​ ​the​ ​document​ ​for​ ​checking​ ​copyrights​ ​as​ ​we​ ​didn’t​ ​get​ ​any​ ​tool​ ​to​ ​scan​ ​a​ ​document


#### LOGIN ​​ ​ :

Users​ ​can​ ​login​ ​through​ ​their​ ​username​ ​and​ ​password.
**REGISTER** ​ ​ **:**
Users​ ​can​ ​​ ​register​ ​by​ ​providing​ ​their​ ​personal​ ​details​ ​and​ ​select​ ​their​ ​interests​ ​in
​ ​settings.
**SEARCH** ​ ​ **BY** ​ ​ **GENRE** ​ ​ **,** ​ ​ **AUTHOR,** ​ ​ **TITLE** ​ ​ **:**
Users​ ​can​ ​search​ ​by​ ​genre,​ ​author,​ ​title.
**RATE** ​ ​ **/** ​ ​ **REVIEW** ​ ​ **:**
Users​ ​can​ ​rate​ ​and​ ​review​ ​the​ ​books/materials​ ​that​ ​are​ ​up​ ​on​ ​​ ​the
Website.
**UPLOAD** ​ ​ **:**
d. Users​ ​can​ ​upload​ ​books​ ​and​ ​materials​ ​related​ ​to​ ​a​ ​particular​ ​community
e. Users​ ​can​ ​upload​ ​the​ ​preview​ ​of​ ​the​ ​hardcopy​ ​they​ ​have​ ​with​ ​them​ ​(which
they​ ​are​ ​willing​ ​to​ ​lend)
**CHAT** ​ ​ **WITH** ​ ​ **UPLOADER** ​ ​ **:**
Users​ ​can​ ​personally​ ​chat​ ​with​ ​the​ ​uploaders​ ​about​ ​a​ ​book​ ​and​ ​discuss​ ​their​ ​views
or​ ​make​ ​a​ ​deal​ ​to​ ​borrow​ ​the​ ​book​ ​(provided​ ​uploader​ ​have​ ​a​ ​hard​ ​copy)
**COMMUNITY** ​ ​ **:**
● Users​ ​can​ ​form​ ​a​ ​community​ ​based​ ​on​ ​interests​ ​,courses​ ​they​ ​have​ ​taken,​ ​institute
they​ ​belong​ ​to,etc.
● Users​ ​can​ ​upload​ ​materials​ ​related​ ​to​ ​the​ ​members​ ​of​ ​the​ ​community.
● Content​ ​can​ ​be​ ​accessed​ ​only​ ​by​ ​members​ ​of​ ​community.
**FOLLOW** ​ ​ **PEOPLE** ​ ​ **:**
Users​ ​can​ ​follow​ ​an​ ​individual​ ​so​ ​that​ ​when​ ​he​ ​or​ ​she​ ​uploads​ ​and
book​ ​they​ ​​ ​get​ ​a​ ​notification.


## CITATIONS

 1. Used​ ​for​ ​implementing​ ​Chat​ ​feature

    https://github.com/Bearle/django-private-chat/tree/dev/example

 2. Used​ ​for​ ​implementing​ ​Search​ ​feature

    https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html

 3. Used​ ​for​ ​understanding​ ​Inbuilt​ ​authentication​ ​System

   https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html

 4. Used​ ​for​ ​understanding​ ​how​ ​django​ ​works​ ​.​ ​Learned​ ​Basic​ ​Django from​ ​this​ ​site

   https://tutorial.djangogirls.org/en/

 5. Used​ ​for​ ​learning​ ​the​ ​way​ ​to​ ​extend​ ​a​ ​model​ ​to​ ​another​ ​model

  https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html

 6. Used​ ​for​ ​learning​ ​about​ ​Many​ ​to​ ​Many​ ​relationships​ ​in​ ​django

   https://www.youtube.com/watch?v=nwpLCa79DUw

 7. Used​ ​for​ ​implemeting​ ​Forgot​ ​Password

   https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html
