#coding=utf-8
from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.template import loader,RequestContext
from django.http import HttpRequest,HttpResponse,HttpResponseBadRequest,HttpResponseForbidden
from models import CommitInfo,User,Project
from django.db.utils import IntegrityError
from django.conf import global_settings

from django.views.generic import ListView

# Create your views here.
class CommitsView(ListView):
    model = CommitInfo
    template_name = 'ContributionBlog/index.html'
    paginate_by = 10
    queryset = CommitInfo.objects.order_by('-commitDate')
    def get_queryset(self):
        queryset = self.queryset
        if 'user' in self.kwargs:
            queryset = queryset.filter(user__name=self.kwargs['user'])
        return queryset
    def get_context_data(self, **kwargs):
        context_data = super(ListView,self).get_context_data()
        if 'user' in self.kwargs:
            context_data['user_name'] = self.kwargs['user']
        return context_data
def postCommitMessage(request):
    assert isinstance(request, HttpRequest)
    required_fields = ['message',
                       'user',
                       'project',
                       'revision',
                       'auth']
    for i in required_fields:
        if not i in request.GET:
            return HttpResponseBadRequest('BAD parameters')
    projects = Project.objects.filter(name=request.GET['project'])
    if len(projects)==0:
        return HttpResponseBadRequest('No project %s' % request.GET['project'])
    else:
        project = projects[0]
        if request.GET['auth'] != project.project_auth:
            return HttpResponseForbidden()
    user = User.objects.filter(name=request.GET['user'])
    if len(user)==0:
        user = User()
        user.name = request.GET['user']
        user.save()
    else:
        user = user[0]
    newCommit = CommitInfo()
    newCommit.user = user
    newCommit.project = project
    try:
        newCommit.revision = int(request.GET['revision'])
        newCommit.commitMessage = request.GET['message']
    except ValueError:
        return HttpResponseBadRequest('BAD parameters')
    try:
        newCommit.save()
    except IntegrityError:
        return HttpResponseBadRequest('Duplicated rev & project')
    return HttpResponse('OK')