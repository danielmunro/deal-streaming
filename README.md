# deal-streaming

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

GitHub will run the `build-and-publish.yaml` workflow, resulting in a docker image being pushed to GitHub Container 
Registry if CI/CD completes successfully.