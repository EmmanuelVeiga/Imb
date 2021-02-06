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


## Links

[Django: Save username equal email - salvar username igual email](https://gist.github.com/rg3915/0b97308cf0123ac73b58a8bd1b584c59)

