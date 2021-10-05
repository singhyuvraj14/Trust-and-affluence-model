from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import json
import pickle
import requests
from .serializers import User_Serializer
from .models import User
import random
import tweepy

consumer_key = "OYXI4GtyLQqpjYJpqPz69SjpN"
consumer_secret = "ELX4TnsEvVS0LmCN4UvWMMOSs0mMzCOxX2ZcBx0R1CsR91iDUh"
access_token_key = "1333770912345165826-qkxMIIC49pPearnw2dNBIGlcCN2zNZ"
access_token_secret = "VT87zTfHXEpPQVd8pXuFkxXv9NeZJWRkNsHeLHEXDoZaa"

def sign(request):
	return render(request, "index.html")

def det(request):
	return render(request, "info.html")

def main(request):
	try:
		name=request.POST.get('name')
		loan=int(request.POST.get('loan'))/73
		term=int(request.POST.get('term'))
		income=int(request.POST.get('income'))
		status=request.POST.get('status')
		home=request.POST.get('home')
		access=int(request.POST.get('access'))
		username=request.POST.get('username')
		monthly=loan/term
		debt=loan/income

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token_key, access_token_secret)
		api = tweepy.API(auth)
		if(access==1):
			dict_user = api.get_user(screen_name = username)
			friends=dict_user.friends_count
			posts=dict_user.statuses_count
		else:
			friends=0
			posts=0
		data={'loanoriginalamount':loan, 'statedmonthlyincome':income, 'term':term, 'employmentstatus': status, 'monthlyloanpayment':monthly, 'debttoincomeratio':debt, 'isborrowerhomeowner':home, 'socialmediaaccess':access, 'friends':friends, 'postbyuser':posts}
		serializer = User_Serializer(data=data, many=False)
		if serializer.is_valid():
			serializer.save()
		df = pd.json_normalize(data)
		df = df[["loanoriginalamount", "statedmonthlyincome", "term", "employmentstatus", "debttoincomeratio", "monthlyloanpayment", "isborrowerhomeowner", "socialmediaaccess", "friends", "postbyuser"]]

		with open('C:/Users/91920/OneDrive/Desktop/trust/trust_app/model_pickle2' , 'rb') as f:
			model= pickle.load(f)
  
		y_pred=model.predict(df)[0]*100
		fins=int(y_pred)
		if(fins<=0):
			fins=random.randrange(0, 50)
		elif(fins>=1100):
			fins=random.randrange(1075,1100)
		return render(request, "final.html",{"mess":fins})
	except:
		alert="Enter valid Username"
		return render(request, "info.html",{"all":alert})