# Passo a passo

* Recriar o projeto

```
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```


* Criar o projeto

```
django-admin.py startproject rimov .
```



* Criar app core

```
cd rimov
python ../manage.py startapp core
```


* Criar app usuario

```
python ../manage.py startapp usuario
```



* OK * Rever o settings


* Usuario: Refazer a autenticação com email

```
usuario/forms.py
```



* Testar criando um usuario pelo shell_plus

```
mkdir -p core/management/commands
touch core/management/__init__.py
touch core/management/commands/__init__.py
touch core/management/commands/criar_usuario.py
```

