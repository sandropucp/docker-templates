# docker-templates

This repo is a introduction of using Docker as a platform for development. with 4 difference scenarios. You can find more details in this [medium blog](https://medium.com/@sandropucp/introduction-to-docker-for-developers-93265abeac66).

1. Add docker to local project.
2. Add docker to Asp.Net Core project.
3. Add docker to Python project.
4. Add docker to Data Science project.

<details>
  <summary>1. Local Project</summary>

```docker
# Linux, Mac, and WSL
docker run -d -p 8080:5063 -v $(pwd):/var/www -w "/var/www" mcr.microsoft.com/dotnet/sdk bash -c "dotnet watch run"

# PowerShell
docker run -d -p 8080:5063 -v ${PWD}:/var/www -w "/var/www" mcr.microsoft.com/dotnet/sdk bash -c "dotnet watch run"
```

</details>

<details>
  <summary>2. Asp.Net Core Project</summary>

```docker
# Build the image using:
docker build -t aspnetcore-sdk .

# Run the image using:
docker run -d -p 5199:5199 -v ${PWD}:/app aspnetcore-sdk
````

</details>

<details>
  <summary>3.Python Project</summary>

```docker
# Go to local folder
cd..

# Build the image:
docker build . -t python_flask

# Get the IMAGEID:
docker images

# Create Container
docker run -d -p 5000:5000 [IMAGEID]

# Stop Container
docker stop [IMAGEID]
````

</details>

<details>
  <summary>4. Data Science Docker</summary>

```docker
# Build the image:
$ docker build . -t datascience

# Get the IMAGEID:
docker images

# Create Container
docker run -it -v ${PWD}:/home/jupyter -p 8888:8888 [IMAGEID]

# Stop Container
docker stop [IMAGEID]
```

</details>
