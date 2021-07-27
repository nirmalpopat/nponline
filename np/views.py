from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import SellsForm, Select
from .models import Sells,Stock
from django.urls import reverse_lazy
import datetime
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

def updatestock(request):
    items = ['earphone','neckband','charger','otg','datacable']
    sells = {}
    for i in Sells.objects.filter(date = datetime.date.today()):
        if i.item_name in items:
            try:
                sells[i.item_name] += 1
            except:
                sells[i.item_name] = 1
    remaining_sells = {}
    for i in Stock.objects.all():
        try:
            remaining_sells[i.item_name] = i.item_qty - sells[i.item_name]
        except:
            remaining_sells[i.item_name] = i.item_qty
    if request.method == 'POST':
        for i in Stock.objects.all():
            Stock.objects.filter(pk = i.pk).update(item_qty=remaining_sells[i.item_name])
        return redirect('addstock')
    return render(request, 'stock_update.html', {'sells': remaining_sells})
            

class StockCreateView(CreateView):
    model = Stock
    fields = ['item_name', 'item_qty']
    template_name = 'stock_create.html'
    success_url = reverse_lazy("addstock")
    def get_context_data(self, **kwargs):
        return dict(
            super(StockCreateView, self).get_context_data(**kwargs),
            stocks=Stock.objects.all()
        )

def index(request):
    try:
        x_forward = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forward:
            ip = x_forward.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip = ''
    print(ip)
    if request.method == 'POST':
        fm = SellsForm(request.POST)
        if fm.is_valid():
            #request.POST['ip'] = get_client_ip(request)
            fm.save()
            #last_data = Sells.objects.order_by('-id')[0]
            
            #print(last_data, '  hererr')
        else:
            return HttpResponse('<h1>Enter vailid data</h1>')

    fm = SellsForm()
    md = Sells.objects.all()
    #print(get_client_ip(request)[0])
    
    return render(request, 'index.html',{'form' : fm,'model' : md, 'ip' : ip})

def view_list(request):
    
    context = {}
    context['form'] = Select()
    context['date'] = datetime.date.today()
    f_date = t_date = datetime.date.today()
    data = Sells.objects.filter(date__range=[f_date, t_date])
    if request.method == 'POST':
        f_date = request.POST['f_date']
        t_date = request.POST['t_date']
        if f_date and t_date:
            pass
        elif f_date and not t_date:
            t_date = datetime.date.today()
        else:
            f_date = t_date = datetime.date.today()
        #if request.POST['agent_name']:
         #   data = Sells.objects.filter(agent_name = request.POST['agent_name'],date__range=[f_date, t_date])
        #else:
            #data = Sells.objects.all()
        data = Sells.objects.filter(date__range=[f_date, t_date])
    return render(request, 'list.html', {'data':data, 'f_date': f_date, 't_date': t_date})
    return render(request, 'select.html', context)