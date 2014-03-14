#coding: utf-8 
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic

from polls.models import Poll

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.order_by('-pub_date')[:15]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def vote(request):
        i = IndexView()
        result={}
        summa=0
        for poll in i.get_queryset():
           # try:
                s=str(poll.id)
                if s in request.POST:
                    pk=int(request.POST[str(poll.id)])
                   # print 'poll.id:',poll.id,',pk=',pk
                    for choice in poll.choice_set.all():
                        if choice.votes != 0:
                            if pk==choice.id:
                                result[poll.id]=u'Верный ответ на '+str(poll.id)+u' вопрос.'
                                summa+=1
                            else:
                                result[poll.id]=u'НеВерный ответ на '+str(poll.id)+u' вопрос.'
                            break
                else:
                    result[poll.id]=u'Вы неответили  на '+str(poll.id)+u' вопрос.'

                    
            #except:
        # Redisplay the poll voting form.
             #   return render(request, 'polls/detail.html', {
             #   'poll': poll.id,
             #   'error_message': "You didn't select a choice.",
             #   })

        return render(request, 'polls/detail.html', {
                 'result_message': u'Вы ответили верно на '+str(summa)+u' вопроса(ов)',
                 'detail_message': result,
                })
    
       #return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
# Create your views here.
