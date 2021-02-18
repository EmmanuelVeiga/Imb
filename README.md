## Este projeto foi feito com:

* [Python 3.8.2](https://www.python.org/)
* [Django 3.1.6](https://www.djangoproject.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/EmmanuelVeiga/imb.git
cd imb
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py shell_plus
```

Leia o [passo-a-passo](passo.md)

## Criar usuário

```
python manage.py criar_usuario --email "admin@email.com" --password "1234" --is_super_user

python manage.py criar_usuario --email "joao@email.com" \
--password "1234" \
--first_name="João" \
--last_name="Silva" \
--corretor
```

## Como criar uma nova branch a partir da master

```
git checkout master  # caso não esteja na master
git checkout -b nova_branch
```


## Links

[Django: Save username equal email - salvar username igual email](https://gist.github.com/rg3915/0b97308cf0123ac73b58a8bd1b584c59)

[How to Extend Django User Model - Option 2: Using One-To-One Link With a User Model (Profile)](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)

Usamos [How to Add User Profile To Django Admin](https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html)

[django-widget-tweaks](https://pypi.org/project/django-widget-tweaks/)

[sweetalert2](https://sweetalert2.github.io/)

[Adiciona mensagem de sucesso no template do Django](https://gist.github.com/rg3915/407577c42bcee93dd8d58a64bd2ba3b0)

[django-orm](https://github.com/rg3915/django-orm)
