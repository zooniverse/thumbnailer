# thumbnailer

Generates on-demand thumbnails of images from the zoo
owned Azure blob storage and (currently) specific S3 buckets. These buckets are allowed:

1. panoptesuploads (Azure storage account, `public` container)
2. All other paths will be proxied to Azure `zooniversestatic` storage account in the `$web` container (e.g. www.sciencegossip.org, www.galaxyzoo.org)
    + https://thumbnails.zooniverse.org/100x100/www.sciencegossip.org/subjects/thumb/54f43a24efc50104c30007d9.jpg
    + https://thumbnails.zooniverse.org/100x100/www.galaxyzoo.org/subjects/thumbnail/56f3dff05925d90043004e21.jpeg

E.g. the following URL

https://thumbnails.zooniverse.org/400x200/panoptes-uploads.zooniverse.org/tutorial_attached_image/00029b92-9b79-4838-8aa0-983b2965a691.png

proxies to the upstream URL -->

https://panoptesuploads.blob.core.windows.net/public/tutorial_attached_image/00029b92-9b79-4838-8aa0-983b2965a691.png

## Testing

1. `docker-compose build`
2. `docker-compose up`

``` bash
# media hosted in azure zooniversestatic storage account $web container
curl -vv localhost:8080/400x200/www.zooniverse.org/291a76c92e4335f7e3a0bed53af6a7bf.jpg

# media hosted in the azure panoptes-uploads storage account public container
curl -vv localhost:8080/400x200/panoptes-uploads.zooniverse.org/tutorial_attached_image/00029b92-9b79-4838-8aa0-983b2965a691.png
curl -vv localhost:8080/400x200/tutorial_attached_image/00029b92-9b79-4838-8aa0-983b2965a691.png
```
