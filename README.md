# thumbnailer

Generates on-demand thumbnails of images from the zoo static S3 bucket

E.g.
http://zooniverse-static.s3-website-us-east-1.amazonaws.com/www.zooniverse.org/291a76c92e4335f7e3a0bed53af6a7bf.jpg
https://thumbnails.zooniverse.org/400x200/www.zooniverse.org/291a76c92e4335f7e3a0bed53af6a7bf.jpg

## Testing

1. `docker-compose build`
2. `docker-compose up`

``` bash
# media hosted in zooniverse-static bucket
curl -vv localhost:8080/400x200/www.zooniverse.org/291a76c92e4335f7e3a0bed53af6a7bf.jpg

# media hosted in www.galaxyzoo.org bucket
curl -vv  localhost:8080/150x150/www.galaxyzoo.org.s3.amazonaws.com/subjects/standard/1237646586100384096.jpg
```
