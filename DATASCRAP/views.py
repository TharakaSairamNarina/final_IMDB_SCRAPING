from django.shortcuts import render
from .models import Movie_Data,TimeSpan
from datetime import datetime, timedelta
from SCHEDULER import Scrap
import pytz
# Create your views here.

def home(request):
    data={
        'languages':['Telugu','Hindi','English','Tamil','Malayalam','Kannada'],
        'geners':['Action','Comedy','Romance','Sci-Fi','Horror','Family'],
        'sort':['Rating Decending','Rating Ascending','Votes Decending','Votes Ascending','Popularity Decending','Popularity Ascending']
    }
    return render(
        request,
        'Html/home.html',
        data
    )

def search(request):
    languages=request.POST.get('language')
    gener=request.POST.get('gener')
    sort=request.POST.get('sort')
    key=languages+gener+sort
    minute = datetime.now(tz=pytz.utc) - timedelta(days=7)
    time=None
    if(TimeSpan.objects.filter(key=key)):
        time=TimeSpan.objects.filter(key=key)[0]
    if(time is None or time.time<minute):
        Scrap.update_date(languages,gener,sort)
        if(time is not None):
            TimeSpan.objects.filter(key=key).delete()
        update_time=TimeSpan(
            key=key,
            time=datetime.now(tz=pytz.utc)
        )
        update_time.save()
    # print(sort)
    data=Movie_Data.objects.filter(gener=gener,language=languages,sort=sort)
    # print(data)
    details={
        'data':data,
        'languages':['Telugu','Hindi','English','Tamil','Malayalam','Kannada'],
        'geners':['Action','Comedy','Romance','Sci-Fi','Horror','Family'],
        'sort':['Rating Decending','Rating Ascending','Votes Decending','Votes Ascending','Popularity Decending','Popularity Ascending'],
        'language':languages,
        'gener':gener,
        'sorting':sort
    }
    return render(
        request,
        'Html/search.html',
        details
    )
