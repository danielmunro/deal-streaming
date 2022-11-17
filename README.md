# deal-streaming

Deal streaming service is a service written in python using flask, with two HTTP endpoints. The root URL for both endpoints is `/product-price`. 

The first endpoint aggregates `ProductPrice` changes via POST requests. 

The second endpoint serves as a search on `ProductPrice` entities for the cheapest price matching the SKU. This request is a GET.  

## Local requirements

- Python 3.9
- openapi-generator (for generating python code from api spec)

## Running the code

```
$ python3 -m openapi_server
```

## Running the tests

```
$ python3 test.py
```

## Generate open API boilerplate

```
$ openapi-generator generate -i api.yaml -g python-flask -o build/
```

## Tagging a new release

```
$ git tag -a <version> -m "<tag message>"
$ git push origin <version>
```

GitHub will run the `build-and-publish.yaml` workflow, resulting in a docker image being pushed to GitHub Container Registry if CI/CD completes successfully.

## Postman integration

`api.postman_collection.json` can be imported into Postman for easier api testing.
