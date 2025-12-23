from fastapi import FastAPI, HTTPException
import docker

app = FastAPI()
client = docker.from_env()

@app.post("/start-container")
def start_container(image: str = "nginx:latest"):
    try:
        container = client.containers.run(
            image=image,
            detach=True,
            name="nginx_test",
            ports={"80/tcp": 8080}
        )
        return {"container_id": container.id}
    except docker.errors.APIError as e:
        raise HTTPException(status_code=500, detail=str(e))
