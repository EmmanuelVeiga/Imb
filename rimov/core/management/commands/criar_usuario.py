from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rimov.usuario.models import Funcionario


class Command(BaseCommand):
    help = 'Cria um usuário.'

    def add_arguments(self, parser):
        # Argumento nomeado
        parser.add_argument('--first_name', dest='first_name', default=None)
        parser.add_argument('--last_name', dest='last_name', default=None)
        parser.add_argument('--email', dest='email', )
        parser.add_argument('--password', dest='password', )
        parser.add_argument(
            '--is_super_user',
            dest='is_super_user',
            default=None,
            action='store_true',
            help='Booleano define se é super usuário ou não.',
        )
        parser.add_argument(
            '--corretor',
            dest='corretor',
            default=None,
            action='store_true',
            help='Booleano define se é corretor ou não.',
        )

    def handle(self, *args, **options):
        email = options['email']
        password = options['password']
        first_name = options['first_name']
        last_name = options['last_name']
        # Truquezinho
        username = email

        if options['is_super_user']:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )

        if options['corretor']:
            usuario = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
            Funcionario.objects.create(
                usuario=usuario,
                tipo='COR',
            )
