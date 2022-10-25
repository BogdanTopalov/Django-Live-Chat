# Django-Live-Chat
 
## Set up DB:
You need to have Docker installed!

Execute:
1. `docker pull postgres`
2. ```
   docker run
   --name (your container name)
   -e POSTGRES_USER=(your DB username)
   -e POSTGRES_PASSWORD=(your DB password)
   -e POSTGRES_DB=(your DB name) 
   -p (host port):(docker container port)
   -v /data:/var/lib/postgresql/data 
   -d 
   postgres
   ```
   Example:
   ```
   docker run 
   --name mycontainername 
   -e POSTGRES_USER=myusername 
   -e POSTGRES_PASSWORD=mypassword 
   -e POSTGRES_DB=mydbname
   -p 5432:5432 
   -v /data:/var/lib/postgresql/data 
   -d 
   postgres
   ```
3. `docker start/stop (your container name)` to start/stop your container

