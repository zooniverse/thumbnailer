# thumbnailer

Generates on-demand thumbnails of images from the zoo
owned Azure blob storage and (currently) specific S3 buckets. These buckets are allowed:

1. panoptesuploads (Azure storage account, `public` container)
2. Anything else will be proxied to S3, for other cases that aren't in panoptesuploads (e.g. www.sciencegossip.org, www.galaxyzoo.org)
    + https://thumbnails.zooniverse.org/100x100/www.sciencegossip.org/subjects/thumb/54f43a24efc50104c30007d9.jpg
    + https://thumbnails.zooniverse.org/100x100/www.galaxyzoo.org/subjects/thumbnail/56f3dff05925d90043004e21.jpeg

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
```
