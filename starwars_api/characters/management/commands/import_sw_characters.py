from django.core.management.base import BaseCommand
from characters.services import import_characters

class Command(BaseCommand):
  
  help = "Import Star Wars characters"
  
  def handle(self, *args, **kwargs):

        import_characters()

        self.stdout.write(self.style.SUCCESS("Characters imported"))