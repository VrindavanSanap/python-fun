import requests

class APIClient:
	def __init__(self, base_url):
		self.base_url = base_url

	def __call__(self, endpoint, **params):
		response = requests.get(f"{self.base_url}/{endpoint}", params=params)
		self.log_request(endpoint, params, response.status_code)
		return response.json()
	
	def log_request(self, endpoint, params, status_code):
		print(f"Requested {endpoint} with {params} - Status code {status_code}")
	
client = APIClient("https://api.artic.edu/api/v1")
resp = client("artworks", page=2, limit=10)
print(resp, type(resp))