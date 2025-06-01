# Project example using Chancy (postgre queue) for python

Application using [Chancy](https://tkte.ch/chancy/) that is a Task queue in Python that support Schedule tasks for future, recurrency tasks and even workflow with dependency using postgres as a storage.

This repo contains a simple example structure with Chancy for demonstrate usage coming configured with the dashboard, for this project we will use [uv package manager](https://docs.astral.sh/uv/) to install the dependencies and [DBngin](https://dbngin.com/) to create a postgresql.


Configure the postgres URI for your application
```sh
export CHANCY_DB_URL="postgresql://postgres:postgres@localhost:5430/postgres"
```

Then you can initialize the database with the migrations and create the queues:
```sh
uv run 00-init.py
```

For the migrations that are the tables that will be created.

![alt text](image-1.png)


Then we can initialize our first jobs.

```sh
uv run 01-create-jobs.py
```

And now we can initialize our worker to process the jobs and view our dashboard.
```sh
uv run 02-worker.py
```

We can see the logs of our jobs and access dashboard [Chancy dashboard](http://localhost:8000/jobs/succeeded) with the credentials (admin/admin).

![alt text](image.png)


And we can look into details for each job.

![alt text](image-2.png)


Or into details for specific queues about the number of jobs already processed.

![alt text](image-3.png)