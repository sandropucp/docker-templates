FROM        mcr.microsoft.com/dotnet/sdk

LABEL       author="Sandro Sanchez"

ENV         DOTNET_URLS=http://+:5199
ENV         ASPNETCORE_URLS=http://+:5199
ENV         DOTNET_USE_POLLING_FILE_WATCHER=1
ENV         ASPNETCORE_ENVIRONMENT=development

WORKDIR     /app

EXPOSE      5199

#ENTRYPOINT ["/bin/bash", "-c","dotnet restore && dotnet watch run"]
ENTRYPOINT ["dotnet", "run"]

# Build the image using:
# docker build -t aspnetcore-sdk .

# Run the image using:
# docker run -d -p 5199:5199 -v ${PWD}:/app aspnetcore-sdk
# docker run -d -p 8080:5199 -v ${PWD}:/app aspnetcore-sdk