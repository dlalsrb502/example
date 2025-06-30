from fastapi import FastAPI
import socket
import os

app = FastAPI()

@app.get("/")
async def get_host():
    try:
        hostname = socket.gethostname()

        db_info = {
            "user": os.getenv("DB_USER", "not set"),
            "password": os.getenv("DB_PASSWORD", "not set"),
            "host": os.getenv("DB_HOST", "not set"),
            "port": os.getenv("DB_PORT", "not set"),
        }

        return {
            "hostname": hostname,
            "db_info": db_info
        }
    except Exception as e:
        return {"message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
