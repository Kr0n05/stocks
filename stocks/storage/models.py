from django.db import models


class SourceFeed(models.Model):
	id = models.AutoField(primary_key=True)
	stock_symbol = models.CharField(max_length=20, db_index=True, verbose_name="Stock Symbol", null=False)
	url = models.CharField(max_length=200, db_index=True, verbose_name="SourceFeed URL", null=False)

	def __unicode__(self):
		return  self.stock_symbol


class News(models.Model):

	id = models.AutoField(primary_key=True)
	sourcefeed = models.ForeignKey(SourceFeed)
	title = models.CharField(max_length=255, verbose_name = "News Title")
	url = models.CharField(max_length=500, verbose_name="News URL", null=False)
	published_datetime = models.DateTimeField()

	retweets = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title + " " + "(%s)" % self.retweets

	class Meta:
		verbose_name = "News"
		verbose_name_plural = "News"
