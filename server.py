from livereload import Server

server = Server()
server.watch('*.html')
server.serve(root='docs/_build/html')