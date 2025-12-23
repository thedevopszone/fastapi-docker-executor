from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.post("/start-container")
def start_container():
    try:
        result = subprocess.run(
            ["docker", "run", "-d", "--name", "nginx_test", "nginx:latest"],
            check=True,
            capture_output=True,
            text=True
        )
        return {"container_id": result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=e.stderr)
