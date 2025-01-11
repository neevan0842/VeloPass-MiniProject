from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.routers import auth, user

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/user", tags=["user"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.exception_handler(Exception)
async def exception_handler(request, exc: Exception):
    return JSONResponse(status_code=500, content={"message": str(exc)})
