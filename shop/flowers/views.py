from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Catalog, Order
from .forms import LoginForm, RegisterForm, OrderForm, ProductForm

def home(request):
    params = {
        'phrase': 'Самый лучший магазин цветов'
    }
    return render(request, 'home.html', context=params)


def catalog(request):
    datal = Catalog.objects.all()
    paginator = Paginator(datal, 3)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'catalog.html', {'catalog': data, 'form': form, 'errors': ''})
        form.save()
        cr = Catalog.objects.get(product=form.cleaned_data['product'])
        return redirect('/catalog/%s' % str(cr.id))
    else:
        form = ProductForm

    return render(request, 'catalog.html', {'catalog': data, 'form': form})


class Product(View):
    def get(self, request, id):
        data = Catalog.objects.get(id=id)
        form = OrderForm()
        Ord = Order.objects.filter(idproduct=id)
        uuser = []
        for el in Ord:
            if el.iduser not in uuser:
                uuser.append(el.iduser)
        return render(request, 'product.html', {'catalog': data, 'user': uuser, 'errors': '', 'form': form})

    def post(self, request, id):
        data = Catalog.objects.get(id=id)
        form = OrderForm(request.POST)
        Ord = Order.objects.filter(idproduct=id)
        uuser = []
        for el in Ord:
            if el.iduser not in uuser:
                uuser.append(el.iduser)
        if not form.is_valid():
            return render(request, 'product.html', {'catalog': data, 'user': uuser, 'errors': '', 'form': form})

        if request.user.is_authenticated():
            u = Order(quantity=form.cleaned_data['quantity'], iduser_id=request.user.id, idproduct_id=data.id,
                      summ=form.cleaned_data['quantity']*data.price)
            u.save()
            data.quantity = F('quantity') - form.cleaned_data['quantity']
            data.save()
            return redirect('/order')
        else:
            return render(request, 'product.html', {'catalog': data, 'user': uuser,
                                                    'errors': 'Авторизуйтесь', 'form': form})


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'errors': '', 'form': form.as_p()})

    def post(self, request):
        form = RegisterForm(request.POST)

        if not form.is_valid():
            return render(request, 'register.html', {'errors': '', 'form': form.as_p()})

        u = User(username=form.cleaned_data['login'], email=form.cleaned_data['email'],
                 last_name=form.cleaned_data['lastname'], first_name=form.cleaned_data['firstname'])
        u.set_password(form.cleaned_data['password'])
        u.save()
        return redirect('/catalog')


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form.as_p()})

    def post(self, request):
        log = request.POST['login']
        password = request.POST['password']
        errors = []

        user = authenticate(username=log, password=password)

        if user is not None:
            login(request, user)
            return redirect('/catalog')
        errors.append('Логин или пароль неверны')
        return render(request, 'login.html', {'errors': mark_safe('<br>'.join(errors)), 'login': login})


@login_required(login_url='/login')
def authOrder(request):
    a = 'Ваши заказы'
    return render(request, 'authOrder.html', {'auth': a})


class BaseView(View):
    success_url = '/'


class Logout(BaseView):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class Newproduct(View):
    def get(self, request):
        form = ProductForm
        return render(request, 'newproduct.html', {'errors': '', 'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, 'newproduct.html', {'errors': '', 'form': form})
        form.save()
        cr = Catalog.objects.get(product=form.cleaned_data['product'])
        return redirect('/catalog/%s' % str(cr.id))
