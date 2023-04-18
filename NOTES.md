This project adds a Django app called content which should have all the logic for the assignment within.

I tested this using Docker.

I used the Django Rest Framework's Serializers to enforce the schema of the input.

The main url for interacting with the application is `localhost:8000/data`.
I feel that I should have done some optimizations here like adding pagination, as it's a bit slow when rendering all data.

To search by `key` or `value`, just pass it in as a query parameter on `localhost:8000/data`.
(i.e. `localhost:8000/data?key=color`)

**Side Note**: I did have to change the script to run `docker compose` instead of `docker-compose` as I could not figure out how to use `docker-compose` locally.
I also added the whole project folder to docker through the volume. 