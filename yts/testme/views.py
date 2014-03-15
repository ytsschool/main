# coding: utf-8
import mimetypes
from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from testme.models import File, Bug
from testme.forms import FileUploadForm, ReportBugForm


def file_manager(request):
    # Check if file is very BIG
    if request.method == 'POST':
        form = FileUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            messages.success(request, u'Файл сохранен')
            return redirect(request.path)
    else:
        form = FileUploadForm()

    return render(request, 'testme/file_manager.html', {
        'files': File.objects.all(),
        'form': form,
    })


def delete_file(request, pk):
    file = get_object_or_404(File, pk=pk)

    if request.method == 'POST':
        file.delete()
        messages.success(request, u'Файл удален')
        return redirect('testme:file_manager')
    else:
        return render(request, 'testme/confirm_file_deletion.html', {'file': file})


def download_file(request, pk):
    file = get_object_or_404(File, pk=pk)
    response = StreamingHttpResponse(file.file, content_type=mimetypes.guess_type(file.file.name))
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(str(file))
    return response


def bugs(request):
    return render(request, 'testme/bugs.html', {
        'bugs': Bug.objects.all(),
    })


def report_bug(request):
    if request.method == 'POST':
        form = ReportBugForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, u'Баг сохранен')
            return redirect("testme:file_manager")

    else:
        form = ReportBugForm()

    return render(request, 'testme/report_bug.html', {
        'form': form,
    })


def main(request):
    return redirect('testme:file_manager')
