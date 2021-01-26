## Este projeto foi feito com:

* [Python 3.8.2](https://www.python.org/)
* [Django 3.1.1](https://www.djangoproject.com/)

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
python manage.py migrate
```