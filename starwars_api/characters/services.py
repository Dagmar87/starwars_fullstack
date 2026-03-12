import requests
from .models import Character

def import_characters():
  
  url = "https://swapi.dev/api/people/"
  
  respnse = requests.get(url)
  data = respnse.json()
  
  for person in data['results']:
    
    Character.objects.create(
			  name=person['name'],
    		height=person['height'] if person['height'].isdigit() else None,
    		mass=person['mass'] if person['mass'].isdigit() else None,
    		gender=person['gender'],
				birth_year=person['birth_year']
		)