import requests

data = {
   "name": "Victor Durán",
   "mail": "victor.duran@ug.uchile.cl",
   "github_url": "https://github.com/COLOSOUS/latam-challenge.git"
}
response = requests.post('https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer', json=data)
print(response.status_code, response.text)

