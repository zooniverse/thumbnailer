# thumbnailer

Generates on-demand thumbnails of images from the zoo
owned Azure blob storage and (currently) specific S3 buckets. These buckets are allowed:

1. panoptesuploads (Azure storage account, `public` container)
2. www.galaxyzoo.org (S3 bucket, legacy)
3. Anything else will be proxied to S3, for other cases that aren't in panoptesuploads (e.g. sciencegossip)

E.g.

https://panoptesuploads.blob.core.windows.net/public/tutorial_attached_image/00029b92-9b79-4838-8aa0-983b2965a691.png

-->

https://thumbnails.zooniverse.org/400x200/tutorial_attached_image/00029b92-9b79-4838-8aa0-983b2965a691.png

## Testing

1. `docker-compose build`
2. `docker-compose up`

``` bash
# media hosted in zooniverse-static bucket
curl -vv localhost:8080/400x200/tutorial_attached_image/00029b92-9b79-4838-8aa0-983b2965a691.png

# media hosted in www.galaxyzoo.org bucket
curl -vv  localhost:8080/150x150/www.galaxyzoo.org.s3.amazonaws.com/subjects/standard/1237646586100384096.jpg
```
