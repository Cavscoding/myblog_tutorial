from django.db import models

class Article(models.Model):
	title = models.CharField(max_length = 100) #博客标题
	category = models.CharField(max_length = 50, blank = True) #博客标签
	date_time = models.DateTimeField(auto_now_add = True) #博客日期
	content = models.TextField(blank = True, null = True) #文章正文

	def __unicode__(self):
		return self.title

	#def __str__(self):
	#	return self.title.encode('utf-8')

	class Meta:  #按时间下降排序
		ordering = ['-date_time']
