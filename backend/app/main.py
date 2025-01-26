from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.User import api as user
from app.core.Auth import api as auth

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/user", tags=["user"])


@app.get("/", tags=["healthcheck"])
async def root():
    return {"message": "Hello World"}


# global exception handler
@app.exception_handler(Exception)
async def exception_handler(request, exc: Exception):
    return JSONResponse(status_code=500, content={"message": str(exc)})
