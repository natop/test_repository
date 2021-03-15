def makeqr(environ, start_response):
    # import qrcode
    #
    # img = qrcode.make(url)
    # with open(path, 'wb') as f:
    #     img.save(f)

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>How Are!</h1>']
from wsgiref.simple_server import make_server
a = 8001
httpd = make_server('', a, makeqr)

httpd.serve_forever()