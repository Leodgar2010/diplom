from django.shortcuts import render, get_object_or_404
from .forms import ClientForm
from .models import Client
def client_ifexist(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'modelapp/client.html', {'client':client})
def add_client (request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            patronymic = form.cleaned_data['patronymic']
            phone = form.cleaned_data['phone']
            client_account = form.cleaned_data['client_account']
            client = Client(first_name=first_name, last_name=last_name,
                            patronymic=patronymic, phone=phone, client_account=client_account)
            client.save()
            message = 'Пользователь сохранён'
    else:
         form = ClientForm()
         message = 'Заполните форму'
    return render(request, 'modelapp/client_form.html', {'form': form, 'message': message})

