from django import forms
from .models import ContactForm, Favoritos, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo (forms.Form)', widget = forms.TextInput(attrs={'style': 'width: 95%;'}))
    customer_name = forms.CharField(max_length=64, label='Nombre (forms.Form)', widget = forms.TextInput(attrs={'style': 'width: 95%;'}))
    message = forms.CharField(label ='Mensaje (forms.Form)', widget = forms.Textarea(attrs = {'style': 'width: 95%; height: 150px;'}))

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = "__all__"
        #fields = ("customer_email", "customer_name", "message")
        
        widgets ={
            "customer_email" : forms.TextInput(attrs={'style': 'width: 95%;'}),
            "customer_name" : forms.TextInput(attrs={'style': 'width: 95%;'}),
            "message" : forms.Textarea(attrs = {'style': 'width: 95%; height: 150px;'})
        }
        labels = {
            'customer_email' : 'Correo',
            'customer_name' : 'Nombre',
            'message' : 'Mensaje' 
        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

        labels = {
            'first_name' : 'Nombre',
            'last_name' : 'Apellido',
            'email' : 'Correo Electrónico' 
        }

class FavoritosForm(forms.ModelForm):
    class Meta:
        model = Favoritos
        fields = ("id_flan", "id_user")

    # Esconder formulario modal con campos inputs generados de claves foraneas
    def __init__(self, *args, **kwargs):
        super(FavoritosForm, self).__init__(*args, **kwargs)
        self.fields['id_flan'].widget = forms.HiddenInput()
        self.fields['id_user'].widget = forms.HiddenInput()
    
    # widgets ={
    #         "id_flan" : forms.HiddenInput(),
    #         "id_user" : forms.HiddenInput(),
    # } 

class DeleteFavoritosForm(forms.Form):
    confirm = forms.BooleanField(widget=forms.HiddenInput(), initial=True)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('mensaje', 'calificacion', 'id_flan', 'id_user')
        #fields = ("customer_email", "customer_name", "message")
                
        widgets ={
            "mensaje" : forms.Textarea(attrs = {'style': 'width: 95%; height: 150px;'}),
            "calificacion" : forms.Select(choices=[(i, i) for i in range(1, 6)])
        }

        labels = {
            'mensaje' : 'Mensaje',
            'calificacion' : 'Nota', 
        }
    
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['id_flan'].widget = forms.HiddenInput()
        self.fields['id_user'].widget = forms.HiddenInput()