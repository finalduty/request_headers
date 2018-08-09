##!virtenv/bin/python
## Provides API for CMK Collector Service

#from flask import Flask, jsonify, abort, make_response, request, url_for
#from time import time

from flask import Flask, request, Response

app = Flask(__name__)

@app.route( '/' )
def index():    
    resp = []
    user_agent = request.headers.get('User-Agent')
    
    for k,v in request.headers:
        if user_agent == "" or user_agent.startswith('curl'):
            resp.append( k + ': ' + v + '\n' )
        else:
            resp.append( k + ': ' + v + '</br>\n' )
    
    return( Response(sorted(resp)) )


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
