import feedparser
import urllib
import urllib2
import json
from time import mktime
from datetime import datetime

from django.http.response import HttpResponseBadRequest, HttpResponse
import storage.models as sm

YAHOO_RSS = lambda symbol:"http://feeds.finance.yahoo.com/rss/2.0/headline?s=%s&region=US&lang=en-US" % symbol
RETWEETS_API = "http://urls.api.twitter.com/1/urls/count.json"

def get_news(request):
	stock_symbol = request.GET.get('stock_symbol')
	if not stock_symbol:
		return HttpResponseBadRequest("provide stock_symbol parameter")

	parsed = feedparser.parse(YAHOO_RSS(stock_symbol))
	if parsed.feed.title ==  u'Yahoo! Finance: RSS feed not found':
		return HttpResponseBadRequest("Unknown stock symbol.")

	sourcefeed, created = sm.SourceFeed.objects.get_or_create(stock_symbol=stock_symbol)
	if created:
		sourcefeed.url = YAHOO_RSS(stock_symbol)
		sourcefeed.save()

	news_saved = 0
	for item in parsed.entries:
		title = item['title']
		url = item['link'].split("/*")[1]
		published_datetime = datetime.fromtimestamp(mktime(item['published_parsed']))
		news, created = sm.News.objects.get_or_create(sourcefeed=sourcefeed, title=title, url=url, published_datetime=published_datetime)
		if created:
			news.retweets = get_retweets(url)
			news.save()
			news_saved += 1
	
	return HttpResponse(news_saved)


def get_retweets(url):
	params_encoded = urllib.urlencode({"url": url})
	data = json.loads(urllib2.urlopen(RETWEETS_API + '?' + params_encoded).read())
	return data['count']
	
