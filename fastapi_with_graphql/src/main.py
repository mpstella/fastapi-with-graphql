import strawberry
 
from typing import Union
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Role:
    id: int
    name: str
    description: str

@strawberry.type
class Person:
    id: int
    name: str
    age: int
    role: Role

lead_singer = Role(id=1, name="Lead", description="Lead Singer of a band")

people = { 
    1 : Person(id=1, name="Bob Marley", age="36", role=lead_singer),
    2 : Person(id=1, name="Jimmy Hendrix", age="27", role=lead_singer)
}


@strawberry.type
class Query:
    
    @strawberry.field
    def person(self, id: int) -> Union[Person,None]:
        return people.get(id, None)

    @strawberry.field
    def role(self, id: int) -> Union[Role, None]:
        return lead_singer if id ==1 else None


schema = strawberry.Schema(Query)
 
graphql_app = GraphQLRouter(schema)
 
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")