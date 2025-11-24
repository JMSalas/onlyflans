from django.shortcuts import render, redirect
from .utils import slice_list, calificacion_promedio
from .models import Flan, Favoritos, Review
from .forms import ContactFormModelForm, SignupForm, FavoritosForm, DeleteFavoritosForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Index View
def index(request):

    context = { 'flans' : Flan.objects.filter(is_private = False)}
    
    return render(request,'index.html', context)

# About View
def about(request):
    return render(request,'about.html')

# Welcome View
@login_required
def welcome(request):
    
    context = {'slides' : slice_list(Flan.objects.filter(is_private=True),3)}

    return render(request,'welcome.html', context)

# Contact View
def contact(request):
    
    initial_data = None
    user = request.user

    if  request.method == 'POST':
        # Construir instancia del formulario con parametros en el cuerpo de la request
        form = ContactFormModelForm(request.POST)
        # Validar formulario
        if form.is_valid():

            form.save()
            # Redireccionar a nueva url
            return redirect('success')
    else:
        if user.is_authenticated:
            initial_data = {'customer_email': user.email,'customer_name': user.first_name + ' ' + user.last_name}
        
        form = ContactFormModelForm(initial = initial_data)

    return render(request,'contact.html', {'form' : form})

# Sign_up View
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('signed_up')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

# Successs View
def success(request):
    return render(request,'success.html')

# Signed Up View
def signed_up(request):
    return render(request,'signedup.html')

# Detalle Flan View
def detalle_flan(request, flan_slug):
    
    flan = Flan.objects.get(slug = flan_slug)
    user = request.user

    favorito = Favoritos.objects.filter(id_flan=flan, id_user=user).first() if user.is_authenticated else None

    if request.method == 'POST':

        if 'add_favorito' in request.POST:
            
            add_form = FavoritosForm(request.POST)
            
            if add_form.is_valid():
                add_form.save()
                return redirect('detalle_flan', flan_slug = flan_slug)
        
        elif 'delete_favorito' in request.POST:
            
            delete_form = DeleteFavoritosForm(request.POST)
            
            if delete_form.is_valid():
                favorito.delete()
                return redirect('detalle_flan', flan_slug = flan_slug)
    else:
        initial_data = {'id_flan': flan.flan_uuid,'id_user': request.user.id}

        add_form = FavoritosForm(initial=initial_data)
        delete_form = DeleteFavoritosForm()
    
    is_favorito = True if favorito else False

    # reviews = flan.review_set.all()
    reviews = Review.objects.filter(id_flan=flan)
    
    # Reviews
    if reviews:
        calificacion_flan = f'{calificacion_promedio([review.calificacion for review in reviews]):.1f}'
    else:
        calificacion_flan = None
        reviews = None
        
    return render(request, 'detalle_flan.html', {'flan' : flan, 'form' : add_form, 'delete_form': delete_form, 'is_favorito': is_favorito, 'reviews' : reviews, 'calificacion' : calificacion_flan})

# Favoritos View
@login_required
def favoritos(request):
    # Join Favoritos y Flan por id_flan para el usuario con sesion activa
    favoritos = Favoritos.objects.filter(id_user=request.user).select_related('id_flan')

    return render(request,'favoritos.html', {'favoritos': favoritos})

# Agregar Review View
@login_required
def review_flan(request, flan_slug):
    
    initial_data = None
    flan = Flan.objects.get(slug = flan_slug)
    user = request.user

    if  request.method == 'POST':

        form = ReviewForm(request.POST)
        # Validar formulario
        if form.is_valid():

            form.save()
            # Redireccionar a nueva url
            return redirect('detalle_flan', flan_slug = flan_slug)
    else:
        initial_data = { 'id_user': user,'id_flan': flan }
        
        form = ReviewForm(initial = initial_data)

    return render(request,'review_flan.html', {'form' : form})