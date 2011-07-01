from django.http import HttpResponse

from django.views.generic.list_detail import object_list

from models import News

def news_list(request):
	return object_list(
        request,
		queryset=News.objects.all(),
        template_name= 'news/list.html',
		template_object_name='news'
    )
	
def news_main(request):
	# For now just return empty set
	return object_list(
        request,    
		queryset=News.objects.none(),
        template_name= 'news/main.html'
    )

def hello(request):
    return HttpResponse("These are not the droids you're looking for.")