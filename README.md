# Django3 dockerized and orchestrated

This project is a basic django 3 project thought to help starting up a new django project
dockerized and orchestrated.

Creates 3 docker images: **django with gunicorn, postgres and nginx**.

## Requirements
- docker
- docker-compose

## Run the project

Run the project:
```
docker-compose up
```

Go to:
```
http://localhost/admin
```
User `admin` and password `admin`. You can change them in the environment variables: `.envs/.django`

Stop the project:
```
docker-compose down
```

If you want to deploy it to a Kubernetes cluster (you need the kubectl pointing to a cluster):
```
kubectl apply -f k8s/
```

**TIP**: You can try the kubernetes using `minikube` in your local machine and assigning kubectl to the "minikube cluster".

## Contains
### Django
- Made with django-cookiecutter.
- DRF API with 2 example endpoints.
- Creates a django superuser.
- Dumb data for the endpoints.
- Two apps, main and api. Main is the app where you can find the basic files.
- src structure. I prefer to have a src directory containing all the apps.
- Use WSGI, you can change to ASGI in `compose/django/start`
- Use Gunicorn to start the server and create 4 workers by default.
- Use environment variables.

### Docker
- Everything can be find inside the directory `compose`.
- Creates a django image based on the project code.
- User is root.
- Nginx publish the statics.
- docker-compose to develop.
- Persistent volumes for postgres and the statics.
- Use environment variables.

# Kubernetes
- All the manifests can be find inside the directory `k8s`.
- Three deployments.
- Three services.
- Persistent volumes for postgres and the statics.
- Use environment variables from the configmaps.
- Ingress to expose the nginx service.
- By default use a public image stored in my account of DockerHub.