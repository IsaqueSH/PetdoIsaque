from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Produto

class CadastroForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(CadastroForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	





# Create Add Record Form
class AddProdutoForm(forms.ModelForm):
	criado_em = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Criado em", "class":"form-control"}), label="")
	nome_produto = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nome", "class":"form-control"}), label="")
	marca_produto = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Marca", "class":"form-control"}), label="")
	pet_produto = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Indicado para qual pet?", "class":"form-control"}), label="")
	tipo_produto = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Tipo", "class":"form-control"}), label="")
	preco_produto = forms.FloatField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Preço", "class":"form-control"}), label="")
	apresentacao_produto = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Apresentação", "class":"form-control"}), label="")

	class Meta:
		model = Produto
		exclude = ("user",)