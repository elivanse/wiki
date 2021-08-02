from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from encyclopedia import util
from encyclopedia.forms import PaginaForm
from encyclopedia.forms import EditarForm
from django import forms
import markdown
import random



def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})



def entry(request, entry):
    if util.get_entry(entry) is None:
        return render(request, "encyclopedia/errorhandler.html", { "errorMsg": "REASON : Page not found!, We cant reach your requested page, try another one :)", "errorTitle": "ERROR"})
    else:
        entryPagina=markdown.markdown(util.get_entry(entry))
        return render(request, "encyclopedia/entry.html", {"entryTitulo": entry,'entryPagina':entryPagina})



def search(request):
    entries = util.list_entries()
    q = request.GET.get('q')
    arr = []
    if q:
        for look in entries:
            if q in entries:
                entryPagina=markdown.markdown(util.get_entry(q))
                return render(request, "encyclopedia/entry.html", {"entryTitulo": q,'entryPagina':entryPagina})
            else:
                if q.lower() in look.lower():
                    arr.append(look)
        if len(arr) == 1:
            entryPagina=markdown.markdown(util.get_entry(arr[0]))
            return render(request, "encyclopedia/entry.html", {"entryTitulo": arr[0],'entryPagina':entryPagina})
        else:
            if len(arr) == 0:
                q = "Empty Search"
                return render(request, "encyclopedia/index.html", {"entry": q, "search": True})
            else:
                varcant = str(len(arr))+" records found"
                return render(request, "encyclopedia/index.html", {"entries": arr, "cantidad": varcant})
    else:
        q = "Empty Search"
        return render(request, "encyclopedia/index.html", {"entry": q, "search": True})



def create(request):
    form = PaginaForm(request.POST or None)
    if request.method == 'POST':
        form = PaginaForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["Title"]
            textarea = form.cleaned_data["Markdown"]
            entries = util.list_entries()
            if title in entries:
                return render(request, "encyclopedia/errorhandler.html", { "errorMsg": "Error : Cannot create requested Page, already exist!", "errorTitle": "ERROR"})
            else:
                util.save_entry(title,markdown.markdown(textarea))
                entryPagina=markdown.markdown(util.get_entry(title))
                return render(request, "encyclopedia/entry.html", {"entryTitulo": title,'entryPagina':entryPagina})
        else:
            form = PaginaForm()
    return render(request, "encyclopedia/create.html", {'form': form})



def edit(request,title):
    content=util.get_entry(title)
    if request.method == 'GET':
        form=EditarForm(initial={"title":title,"txarea":content})
        return render(request,"encyclopedia/edit.html",{"title":title,"edit":form})
        pagename = edit_form.cleaned_data["pagename"]
    if request.method=="POST":
        form=EditarForm(request.POST)
        if form.is_valid():
            tx = form.cleaned_data["txarea"]
            util.save_entry(title,tx)
            page_converted = markdown.markdown(content)
            entryPagina=markdown.markdown(util.get_entry(title))
            return render(request, "encyclopedia/entry.html", {"entryTitulo": title,'entryPagina':entryPagina})
        else:
            page = util.get_entry(title)
            return render(request, "encyclopedia/errorhandler.html", { "errorMsg": "Error : Cannot edit requested Page, try again!", "errorTitle": "ERROR"})



def rnd(request):
    if request.method == 'GET':
        entries=util.list_entries()
        rnd_page=random.choice(entries)
        entry=util.get_entry(rnd_page)
        entryPagina=markdown.markdown(entry)
        return render(request, "encyclopedia/entry.html", {"entryTitulo": rnd_page,'entryPagina':entryPagina})