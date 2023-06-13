from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    
    
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_list = parse.parse_qsl(url_components.query)
    my_dict = dict(query_list)
    
    # print(111,my_dict)
    if 'cantry_name' in my_dict:
      contry = my_dict.get('cantry_name')
      url= 'https://restcountries.com/v3.1/name/'
      res = requests.get(url+contry)
      data = res.json()
      # print(222,data)
    for cantry_name_data in data :
      capital = cantry_name_data['capital'][0]
      message = f'the capital of {contry} is {capital}'
      
    # print(3333,list_of_dif)




    self.wfile.write(message.encode())
    return