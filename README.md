## Running this thing
```sh
$> cd fastapi_with_graphql/src
$> poetry run uvicorn main:app --reload
```

## Sample Query

```json
{
  person(id: 2) {
    name,
    role {
      description
    }
  }
}
```
