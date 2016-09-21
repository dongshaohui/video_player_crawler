#coding=utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from bs4 import BeautifulSoup
import sys,os,urllib2,threading,re
from VideoCrawler.models import *

# Create your views here.
def video_crawler(request):
	response = {}
	jizzdr_url_tag = "http://www.jizzdr.com/porn-video?p="
	for i in range(1,10):
		jizzdr_url = jizzdr_url_tag + str(i)
		r = urllib2.Request(jizzdr_url)
		f = None
		soup = None
		try:
			f = urllib2.urlopen(r, data=None, timeout=30)
			soup = BeautifulSoup(f.read(),"html.parser")
		except:
			continue
		video_thumb_list = soup.findAll('a',{'class','thumb'})
		video_title_list = soup.findAll('a',{'class','title'})
		for index in range(0,len(video_thumb_list)):
			video_thumb_tag = video_thumb_list[index]
			video_title_tag = video_title_list[index]
			href = "http://www.jizzdr.com" + video_thumb_tag['href']
			img_link = video_thumb_tag.find('img')['src']
			video_title = video_title_tag['title']
			digit_mode = re.compile(r'\d+')
			video_number = int(digit_mode.findall(href)[0])
			if len(porn_video_info.objects.filter(number=video_number)) == 0:
				porn_video_info.objects.create(number=video_number,desc=video_title,link=href,thumb=img_link)

	return HttpResponse(json.dumps(response,ensure_ascii=False,indent=2))