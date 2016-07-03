from django.db import models
from django.core.urlresolvers import reverse

class Article(models.Model):
	title = models.CharField(max_length = 100) #博客标题
	category = models.CharField(max_length = 50, blank = True) #博客标签
	date_time = models.DateTimeField(auto_now_add = True) #博客日期
	content = models.TextField(blank = True, null = True) #文章正文

	def __unicode__(self):
		return self.title

	#获取URL并转换成url的表示格式
	def get_absolute_url(self):
		path = reverse('detail', kwargs={'id': self.id})
		return "http://127.0.0.1:8000%s" % path
	
	#def __str__(self):
	#	return self.title

	class Meta:  #按时间下降排序
		ordering = ['-date_time']
