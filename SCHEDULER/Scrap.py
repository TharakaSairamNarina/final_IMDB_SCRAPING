import os
from DATASCRAP.models import Movie_Data,TimeSpan
from flask import Flask, flash, redirect, render_template, request, url_for
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import re

def sort_code(sort):
    algo=""
    if(sort=='Rating Decending'):
        algo='&sort=user_rating,desc'
    elif(sort=='Popularity Decending'):
        algo='&sort=moviemeter,desc'
    elif(sort=='Votes Decending'):
        algo='&sort=num_votes,desc'
    elif(sort=='Rating Ascending'):
        algo='&sort=user_rating,asc'
    elif(sort=='Votes Ascending'):
        algo='&sort=num_votes,asc'
    return algo

def language_code(language):
    lang=""
    if(language == 'Telugu'):
        lang='te'
    elif(language == 'Hindi'):
        lang='hi'
    elif(language == 'Malayalam'):
        lang='ml'
    elif(language == 'Kannada'):
        lang='kn'
    elif(language == 'Tamil'):
        lang='ta'
    elif(language == "English"):
        lang='en'
    return lang


def update_date(languages,gener,sorting):
    language=language_code(languages)
    sort=sort_code(sorting)
    key=languages+gener+sorting
    Movie_Data.objects.filter(key=key).delete()
    my_url='https://www.imdb.com/search/title/?num_votes=200,&genres='+gener+'&languages='+language+'&country=in'+sort+'&count=250'
    print(my_url)
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    c=0
    #grabs each product
    containers = page_soup.findAll("div",{"class":"lister-item mode-advanced"})
    # print(containers)
    for container in containers:

        # movie name
        movie=""
        if(container.a.img["alt"]):
            movie = container.a.img["alt"]

        #img_url
        url=""
        if(container.a.img["loadlate"]):
            url=container.a.img["loadlate"]
        else:
            url="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB466725069_.png"

        #rating
        rating=""
        if(container.strong):
            rating = container.strong.text

        #votes
        votes=''
        if(container.findAll("span",{"name":"nv"})):
            votes=container.findAll("span",{"name":"nv"})[0]
            votes=votes.text.split('>')[0]

        #release date
        Date_rel= container.findAll("span",{"class":"lister-item-year text-muted unbold"})
        date=""
        if(Date_rel[0].text):
            date = Date_rel[0].text.strip()

        # Run times
        Run_time= container.findAll("span",{"class":"runtime"})
        duration=""
        if(Run_time):
            duration = Run_time[0].text.strip()

        # Director and actors
        act = container.findAll("p",{"class":""})
        actt = act[0].text
        act1 = actt.replace("\n","")
        act2 = act1.replace('|',"\n")
        act3 = act2.replace(' ','')
        actors=act3.split(":")
        character=""
        director=""
        if(actors):
            if(len(actors)==3):
                character=actors[2]
                director=(actors[1].split('\n'))[0]
            else:
                if(actors[0]=="Director" or actors[0]=="Directors"):
                    director=actors[1]
                elif(actors[0]=='Star' or actors[0]=='Stars'):
                    # print(actors[1])
                    character=actors[1]
        character=character.split(",")
        director=director.split(",")
        characters=""
        directors=""
        for char in character:
            characters+=char+" "
        for dirs in director:
            directors+=dirs+" "
        # print(character)
        # # Introduction to movuie
        intr = container.findAll("p",{"class":"text-muted"})
        intro = intr[1].text.replace('   ','')
        introduction = intro.replace("\n","")
        if(introduction.endswith("»")):
            introduction=introduction[0:len(introduction)-22]
            introduction+='.'
        if(movie!='' or rating!='' or votes!='' or date!='' or duration!='' or characters!='' or director!='' or len(introduction)>15):
            c=c+1
            # print(movie+" "+language+" "+gener+" "+sort)
            save_data=Movie_Data(
                key=key,
                language=languages,
                gener=gener,
                sort=sorting,
                img_url=url,
                movie=movie,
                rating=rating,
                votes=votes,
                date=date,
                duration=duration,
                character=characters,
                director=directors,
                introduction=introduction
            )
            save_data.save()
            if(c==10):
                break