# request_headers
Simple web server that echos the headers of requests made to it.

It's really basic, but is helpful when trying to quickly see what headers are being passed back to an application.

e.g.
```
$ curl 127.0.0.1:5000
## Generated by headers.py ##
Accept: */*
Content-Length: 
Content-Type: 
Host: 127.0.0.1:5000
User-Agent: curl/7.54.0
```

## Docker
To build the docker image
`docker built -t local/request_headers .`

To run the docker image as daemon
`docker run -d --rm -p5000:5000 local/request_headers`

To run the docker image in foreground
`docker run -it --rm -p5000:5000 local/request_headers`
