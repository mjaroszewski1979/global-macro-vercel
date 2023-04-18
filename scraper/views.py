from django.http import HttpResponse
from django.shortcuts import render
from .forms import MyForm
from .scraper import links, stats
import mimetypes
import os
from pathlib import Path

# Create your views here.

    

def home_view(response):
    if response.method == 'POST':
        form = MyForm(response.POST)
        if form.is_valid():
            website = form.cleaned_data['website']
            keyword = form.cleaned_data['keyword']
            pages = form.cleaned_data['pages']
            data = form.cleaned_data['csv']
            new_link = links.get_links(website, keyword, pages)
            new_stat = stats.get_stats(website, keyword)
            if data == True:
                links.get_csv_links(website, keyword, pages)
                return render(response, 'success.html', {'website':website, 'keyword':keyword, 'new_link':new_link, 'new_stat':new_stat, 'data': data})
            else:
                return render(response, 'success.html', {'website':website, 'keyword':keyword, 'new_link':new_link, 'new_stat':new_stat, 'data': data})
    else:
        form = MyForm()
        return render(response, 'home.html', {'form':form})

def csv_view(response):
    BASE_DIR = Path(__file__).resolve().parent.parent
    filename = 'links.csv'
    fl_path = os.path.join(BASE_DIR, filename)
    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def page_not_found(response, exception):
    return render(response, '404.html')

def server_error(response):
    return render(response, '500.html')

