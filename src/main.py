'''Entry Point'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from src.routes import users, resumes, profiles, challenges

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
# app.include_router(resumes.router)
# app.include_router(profiles.router)
# app.include_router(challenges.router)


@app.get('/')
async def root():
    '''
    Root endpoint.

    Returns:
        dict: A welcome message.
    '''
    return {'message': 'Wellcome again!'}
