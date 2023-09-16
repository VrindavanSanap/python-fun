from wsgiref.simple_server import make_server

def application(environ, start_response):
    # Check if the URL path matches our expected format
    headers = [('Content-type', 'text/plain')]
    if environ['PATH_INFO'] == '/square':
        try:
            query_string = environ['QUERY_STRING']
            params = dict(p.split('=') for p in query_string.split('&'))
            number = float(params.get('number', 0))
            result = number * number
            status = '200 OK'
            headers = [('Content-type', 'text/plain')]
            response = f"The square of {number} is {result}"

        except Exception as e:
            status = '400 Bad Request'
            response = f"Bad Request: {str(e)}"
    else:
        status = '404 Not Found'
        response = 'Not Found'

    start_response(status, headers)
    return [response.encode('utf-8')]

if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    with make_server(host, port, application) as httpd:
        httpd.serve_forever()

