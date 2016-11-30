from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Topics


def index(request):
    all_topics = Topics.objects.all()
    context = {
        'all_topics' : all_topics,
    }
    return render(request, 'maps/index.html', context)



def details(request, topic_id):
    apnd = Topics.objects.get(pk = topic_id)
    awslink = ''
    full = awslink + apnd.topic

    tweet = requests.get(full)
    results = json.loads(tweet.text)
    round1 = results["hits"]["hits"]
    list1 = []
    count = 0
    for i in range(len(round1)):
        try:
            if str(round1[i]['_source']['sentiment'])[1]== "p":
                list1.append({'latitude': round1[i]['_source']['latitude'], 'longitude': round1[i]['_source']['longitude'], 'sentiment': 1})
            elif str(round1[i]['_source']['sentiment'])[3]== "u":
                list1.append({'latitude': round1[i]['_source']['latitude'], 'longitude': round1[i]['_source']['longitude'], 'sentiment': 0})
            elif str(round1[i]['_source']['sentiment'])[3]== "g":
                list1.append({'latitude': round1[i]['_source']['latitude'], 'longitude': round1[i]['_source']['longitude'], 'sentiment': -1})
        except KeyError:
            pass



    #
    for i in range(len(round1)):
        if round1[i]['_source']['flag'] == 1:
            count += 1
            round1[i]['_source']['flag'] = 0
            #es_client.update(index='twittersen', type = 'twittersen', id=es["_id"] body = {"doc":{"flag":0}})
        else:
            count = 0



    #print (list1[0]['sentiment'][1] == "p")
    #print (round1[2]['_source']['flag'] == 1)
    context = {'list1': list1, 'count' : count}
    return render(request, 'maps/details.html', context)

