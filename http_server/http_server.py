
#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        #print(self.path)
        # my_json = {'nombre':'iphone', 'precio':'3000000'}
        # json_codificado = json.dumps(my_json, ensure_ascii=False).encode()
        # self.wfile.write(json_codificado)
        file = open('info.json').read().encode()
        dic = json.loads(file)
        if self.path[1:].isdigit():
            numero = self.path[1:]
            item = dic.get(numero)
            json_item = json.dumps(item).encode()
            self.wfile.write(json_item)
        else:
            self.wfile.write(file)

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        print(post_data)
        #convertimos la data a diccionario con json.loads
        diccionario = json.loads(post_data.decode('utf8'))
        #leemos el archivo
        file = open('info.json').read().encode()
        #convertimos a diccionario el json del archivo
        dict_de_archivo = json.loads(file)
        #metemos en el diccionario el dic de la data y con len(dict_de_archivo)+1 le ponemos el id que sigue
        dict_de_archivo[3] = diccionario
        #enviamos el nuevo json
        a = json.dumps(diccionario).encode()
        self.wfile.write(a)
        #self.wfile.write("<html><body><h1>POST!</h1></body></html>")


# def run(server_class=HTTPServer, handler_class=S, port=80):
#     server_address = ('', port)
#     httpd = server_class(server_address, handler_class)
#     print
#     'Starting httpd...'
#     httpd.serve_forever()


if __name__ == "__main__":
    #run()
    url=''
    port=80
    server_address=(url,port)
    httpd=HTTPServer(server_address,S)
    print('iniciando')
    httpd.serve_forever()