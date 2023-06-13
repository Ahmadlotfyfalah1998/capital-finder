from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    url_path=self.path
    print(1111,url_path)
    url_component=parse.urlsplit(url_path)
    print('2222',url_component)
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    welcom="welcom to deployed page"
    self.wfile.write(welcom.encode())
    return