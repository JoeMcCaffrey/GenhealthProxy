
# Submisison for Joe McCaffrey

## Running
`docker-compose up`

or locally

`python server.py`

Then you can navigate to 

`localhost:8000` 
and use the swagger doc 

The predict and embeddings endpoints require a bearer token, which is the same as given from the Genhealth Auth0 site.

In the swagger doc in the upper right hand corner of the request you can click the lock icon and add the token.

## Design

A few pillars of my design:
- Deployment (docker, docker compose instead of k8s for simplicity)
- Security (using fast api built in auth)
- Error Handling
- Unit Testing

I believe that deployment/security is pretty important for startups, as they need to get their capabilities to market quickly 

When Engineers have designs that are working on their laptops, which have some break through capability or reduce a painpoint. 
There is an abyss to get it deployed and working in the cloud. 
