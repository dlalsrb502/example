from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
async def get_host():
    try:
        hostname = socket.gethostname()
        return {"hostname": hostname}
    except Exception as e:
        return {"message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)