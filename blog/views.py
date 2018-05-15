## @brief Views for the blog app.

from django.utils import timezone
from .models import Interest,Document,Rate,Follow,Community,Join,Advertise,Readpending,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignUpForm,InterestForm,DocumentForm,RatingForm,CommunityForm,AdvertiseForm,DocumentCForm,ProfileForm
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .filters import DocumentFilter,AdvertiseFilter
from django.contrib import messages

## @brief view for the home page of the user.
#
# This view is called by home url.\n
# It returns to home.html 
@login_required
def home(request):
    documents = Document.objects.order_by('published_date').filter(user=request.user,searchshow=True)
    ads = Advertise.objects.order_by('published_date').filter(user=request.user)
    interest = Interest.objects.get(user=request.user)
    choices=['Fiction','LoveandRomance',"Mystery","Thriller","ScienceandFiction","Fantasy","Horror","ActionandAdventure","Comedy","Poetry","Study"]
    doc=Document.objects.order_by('published_date').filter(genre__in=interest.my_field,searchshow=True).exclude(user=request.user)
    Communities=Community.objects.all().exclude(admin=request.user)
    communities=[c for c in Communities]
    jpclist=map(lambda x:[x,x.jrequests.all()],communities)
    oCom=Community.objects.filter(admin=request.user)
    ocom=[c for c in oCom]
    opclist=map(lambda x:[x,x.jrequests.all().count()],ocom)
    jcom=Join.objects.get(user=request.user).jlist.all()
    readreq=Readpending.objects.filter(user=request.user)
    rplist=map(lambda x:[x.doc,x.rplist.all()],readreq)
    return render(request, 'home.html',{'documents': documents,'ads':ads,'interest':interest,'doc':doc,'jpclist':jpclist,'jcom':jcom,'opclist':opclist,'rplist':rplist,'choices':choices})

## @brief view for the signup page for a new user.
#
# This view is called by signup url.\n
# It returns to signup.html 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            Interest.objects.create(user=user,my_field=['Fiction','Study','Comedy','Thriller','ScienceandFiction'])
            Follow.objects.create(user=user)
            Profile.objects.create(user=user)
            Join.objects.create(user=user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

## @brief view to edit profile of a user.
#
# This view is called by editprofile url.\n
# It returns to editprofile.html 
def editprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            request.user.email=form.cleaned_data.get('email',None)
            request.user.first_name=form.cleaned_data.get('first_name',None)
            request.user.last_name=form.cleaned_data.get('last_name',None)
            request.user.save()
            return redirect('settings')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'editprofile.html', {'form': form})

## @brief view to edit interets of a user.
#
# This view is called by interests url.\n
# It returns to interests.html 
def interests(request):
    if request.method == "POST":
        form = InterestForm(request.POST,instance=request.user.interest)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = InterestForm(instance=request.user.interest)
    return render(request, 'interests.html', {'form': form})

## @brief view to upload document.
#
# This view is called by upfile url.\n
# It returns to model_form_upload.html 
def upfile(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=request.user
            post.uploader = request.user.username.encode('ascii','ignore')
            post.published_date = timezone.now()
            post.save()
            Readpending.objects.create(user=request.user,doc=post)
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {'form': form})

## @brief view to advertise a book
#
# This view is called by advertise url.\n
# It returns to model_form_upload.html
def advertise(request):
    if request.method == 'POST':
        form = AdvertiseForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=request.user
            post.uploader = request.user.username.encode('ascii','ignore')
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = AdvertiseForm()
    return render(request, 'model_form_upload.html', {'form': form})

## @brief view for settings page
#
# This view is called by settings url.\n
# It returns to settings.html
def settings(request):
    return render(request,'settings.html')

## @brief view for notifications page
#
# This view is called by notes url.\n
# It returns to notes.html
def notes(request):
    f=Follow.objects.get(user=request.user)
    fl=f.flist.all()
    d=Document.objects.filter(user__in=fl).order_by('-published_date')
    readreq=Readpending.objects.filter(user=request.user)
    rplist=map(lambda x:[x.doc,x.rplist.all()],readreq)
    
    return render(request,'notes.html',{'fl':fl,'d':d,'rplist':rplist})

## @brief view for search page
#
# This view is called by search url.\n
# It returns to search.html
def search(request):
    Document_list = Document.objects.all()
    Document_filter = DocumentFilter(request.POST, queryset=Document_list)   
    if request.method == 'POST':
        le=Document_list.count()
        return render(request, 'search.html', {'filter': Document_filter,'le':le})
    else:
        return render(request, 'search.html',{'filter': Document_filter,'le':0})

def searchad(request):
    ad_list = Advertise.objects.all()
    ad_filter = AdvertiseFilter(request.POST, queryset=ad_list)   
    if request.method == 'POST':
        le=ad_list.count()
        return render(request, 'searchad.html', {'filter': ad_filter,'le':le})
    else:
        return render(request, 'searchad.html',{'filter': ad_filter,'le':0})

## @brief view to delete a book
#
# This view is called by delete url.\n
# It returns to home.html
def delete1(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    doc.delete()
    return redirect('home')

## @brief view to delete a advertise
#
# This view is called by delete1ad url.\n
# It returns to home.html
def delete1ad(request, pk):
    ad = get_object_or_404(Advertise, pk=pk)
    ad.delete()
    return redirect('home')

## @brief view for book page
#
# This view is called by bookpage url.\n
# It returns to bookpage.html
def bookpage(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    mlist=doc.rmembers.all()
    if(doc.searchshow):
        rplist=Readpending.objects.get(doc=doc).rplist.all()
    else:
        rplist=[]
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            r = Rate.objects.filter(doc=doc,user=request.user)
            if not r:
                r=Rate.objects.create(user=request.user, doc=doc, rating=form.cleaned_data.get('rating',None))
            r=Rate.objects.get(doc=doc,user=request.user)
            r.rating=form.cleaned_data.get('rating',None)
            r.save()
            tr=list(Rate.objects.filter(doc=doc).values_list('rating',flat=True))
            #print(r.rating)
            #print(Rate.objects.get(doc=doc,user=request.user).rating)
            if tr!=[]:
                r1=float(sum(tr))/float(len(tr))
                t=len(tr)
                d1=Document.objects.get(document=doc.document)
                d1.rating=r1
                d1.no_ratings=t
                d1.save()
            else:
                r1=0
                t=0
                doc.rating=r1
                doc.no_ratings=t
                doc.save()
            return render(request,'bookpage.html',{'doc':doc,'form':form,'r':r,'r1':round(r1,2),'t':t,'user':request.user,'mlist':mlist,'rplist':rplist})
    else:
        form = RatingForm()
        tr=list(Rate.objects.filter(doc=doc).values_list('rating',flat=True))
        if tr!=[]:
            r1=float(sum(tr))/float(len(tr))
            t=len(tr)
            doc.rating=r1
            doc.no_ratings=t
            doc.save()
        else:
            r1=0
            t=0
            doc.rating=r1
            doc.no_ratings=t 
            doc.save() 
    return render(request,'bookpage.html',{'doc':doc,'form':form,'r1':round(r1,2),'t':t,'mlist':mlist,'rplist':rplist})

## @brief view for ad page
#
# This view is called by adpage url.\n
# It returns to adpage.html
def adpage(request, pk):
    ad = get_object_or_404(Advertise, pk=pk)
    return render(request,'adpage.html',{'ad':ad,})

## @brief view for joined communities page of a user
#
# This view is called by jcommunities url.\n
# It returns to joinedcommunity.html
def jcommunities(request):
    jcom=Join.objects.get(user=request.user).jlist.all()
    return render(request,'joinedcommunity.html',{'jcom':jcom,})

## @brief view for other communities page of a user
#
# This view is called by ocommunities url.\n
# It returns to othercommunity.html
def ocommunities(request):
    Communities=Community.objects.all().exclude(admin=request.user)
    communities=[c for c in Communities]
    jpclist=map(lambda x:[x,x.jrequests.all()],communities)
    jcom=Join.objects.get(user=request.user).jlist.all()
    return render(request,'othercommunity.html',{'jpclist':jpclist,'jcom':jcom})

## @brief view to edit profile of a user.
#
# This view is called by reset url.\n
# It returns to change_password.html 
def reset(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

## @brief view for genre page
#
# This view is called by genre url.\n
# It returns to genre.html
def genre(request,pk):
    documents=Document.objects.filter(genre=pk,searchshow=True)
    return render(request,'genre.html',{'docs':documents})

## @brief view for author page
#
# This view is called by author url.\n
# It returns to author.html
def author(request,pk):
    documents=Document.objects.filter(author=pk,searchshow=True)
    return render(request,'author.html',{'docs':documents})

## @brief view for uploader page
#
# This view is called by uploader url.\n
# It returns to uploader.html
def uploader(request,pk):
    documents=Document.objects.filter(uploader=pk,searchshow=True)
    u=documents.first().user
    f=Follow.objects.get(user=request.user).flist.all()
    if u in f:
        s=1
    else:
        s=0
    return render(request,'uploader.html',{'docs':documents,'s':s,'pk':pk})


## @brief view to make one user follow another user
#
# This view is called by follow url.\n
# It returns to uploader.html
def follow(request,pk):
    print(pk)
    documents=Document.objects.filter(uploader=pk)
    u=documents.first().user
    f=Follow.objects.get(user=request.user)
    f.flist.add(u)
    f.save()
    return render(request,'uploader.html',{'docs':documents,'s':1,'pk':pk})


## @brief view to make one user follow another user
#
# This view is called by unfollow url.\n
# It returns to uploader.html
def unfollow(request,pk):
    documents=Document.objects.filter(uploader=pk)
    u=documents.first().user
    f=Follow.objects.get(user=request.user)
    f.flist.remove(u)
    f.save()
    return render(request,'uploader.html',{'docs':documents,'s':0,'pk':pk})


## @brief view to change privacy of a document
#
# This view is called by change url.\n
# It returns to bookpage.html
def change(request,pk):
    doc = get_object_or_404(Document, pk=pk)
    doc.public=not(doc.public)
    doc.save()
    form = RatingForm()
    tr=list(Rate.objects.filter(doc=doc).values_list('rating',flat=True))
    if tr!=[]:
        r1=float(sum(tr))/float(len(tr))
        t=len(tr)
        doc.rating=r1
        doc.no_ratings=t
        doc.save()
    else:
        r1=0
        t=0
        doc.rate=r1
        doc.no_ratings=t 
        doc.save() 
    return render(request,'bookpage.html',{'doc':doc,'form':form,'r1':round(r1,2),'t':t})

## @brief view to create a community
#
# This view is called by community url.\n
# It returns to createcommunity.html
def community(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.admin=request.user
            post.save()
            return redirect('home')
    else:
        form = CommunityForm()
    return render(request, 'createcommunity.html', {'form': form})
    
## @brief view for community page
#
# This view is called by cpage url.\n
# It returns to cpage.html
def cpage(request, pk):
    com = get_object_or_404(Community, pk=pk)
    mlist=com.members.all()
    jplist=com.jrequests.all()
    docs=com.documents.all()
    return render(request,'cpage.html',{'com':com,'mlist':mlist,'jplist':jplist,'docs':docs})

## @brief view to sendrequest to join a community by a user
#
# This view is called by srequest url.\n
# It returns to othercommunity.html
def srequest(request, pk):
    com = get_object_or_404(Community, pk=pk)
    com.jrequests.add(request.user)
    return redirect('ocommunities')

## @brief view to cancelrequest to join a community by a user
#
# This view is called by crequest url.\n
# It returns to othercommunity.html
def crequest(request, pk):
    com = get_object_or_404(Community, pk=pk)
    com.jrequests.remove(request.user)
    return redirect('ocommunities')

## @brief view to acceptrequest of a user by admin of a community 
#
# This view is called by accept url.\n
# It returns to cpage.html
def accept(request, pk,name):
    u = User.objects.get(pk=pk)
    com=Community.objects.get(admin=request.user,name=name)
    com.members.add(u)
    com.jrequests.remove(u)
    Join.objects.get(user=u).jlist.add(com)
    return redirect('cpage',pk=com.pk)

## @brief view for a user to leave a community
#
# This view is called by leave url.\n
# It returns to home.html
def leave(request, pk):
    com = get_object_or_404(Community, pk=pk)
    com.members.remove(request.user)
    Join.objects.get(user=request.user).jlist.remove(com)
    return redirect('home')

## @brief view for a user to send a request to read a private book
#
# This view is called by prequest url.\n
# It returns to bookpage.html
def prequest(request,pk):
    doc=Document.objects.get(pk=pk)
    u=doc.user
    rp=Readpending.objects.get(user=u,doc=doc).rplist.add(request.user)
    return redirect('bookpage',pk=doc.pk)

## @brief view for a user to cancel a request sent by him to read a private book
#
# This view is called by cprequest url.\n
# It returns to bookpage.html
def cprequest(request,pk):
    doc=Document.objects.get(pk=pk)
    u=doc.user
    rp=Readpending.objects.get(user=u,doc=doc).rplist.remove(request.user)
    return redirect('bookpage',pk=doc.pk)

## @brief view to acceptreadrequest of a user by uploader of book 
#
# This view is called by acceptread url.\n
# It returns to notes.html
def acceptread(request, pk,pk1):
    u = User.objects.get(pk=pk)
    doc=Document.objects.get(pk=pk1)
    doc.rmembers.add(u)
    doc.save()
    Readpending.objects.get(user=request.user,doc=doc).rplist.remove(u)
    return redirect('notes')

## @brief view to upload document in a community
#
# This view is called by upfilec url.\n
# It returns to model_form_upload.html 
def upfileinc(request,pk):
    com=Community.objects.get(pk=pk)
    if request.method == 'POST':
        form = DocumentCForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=request.user
            post.uploader = request.user.username.encode('ascii','ignore')
            post.published_date = timezone.now()
            post.searchshow=False
            post.save()
            com.documents.add(post)
            com.save()
            return redirect('cpage',pk=com.pk)
    else:
        form = DocumentCForm()
    return render(request, 'model_form_upload.html', {'form': form})
