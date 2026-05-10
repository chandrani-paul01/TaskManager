from fastapi import FastAPI
from Routes import task_routes,user_routes
from Authentication import auth
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_routes.router)
app.include_router(user_routes.router)
app.include_router(auth.router)
