from django.core.management.base import BaseCommand
from modelapp.models import Client
class Command(BaseCommand):
    help = "Create client."
    def handle(self, *args, **kwargs):
        client = Client(first_name='Ivan',  last_name='Fedorov', patronymic='Semenovich', phone = "89112352142",
                  client_account=0.00)
        client.save()
        self.stdout.write(f'{client}')