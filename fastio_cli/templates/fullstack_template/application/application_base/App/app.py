from typing import List
from fastapi import Depends, FastAPI, Header, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

from App.Config.app import settings
from App.Models import User
from App.Http.Requests import UserCreateRequest
from App.Http.middleware import ROUTES_MIDDLEWARE

from App.Api.admin import admin_api_router
from App.Api.v1 import api_router

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(title=settings.APP_NAME, openapi_url="{0}/openapi.json".format(settings.API_ADMIN_PREFIX), middleware=ROUTES_MIDDLEWARE)

# Register client API: /*
app.include_router(api_router)

# Register Admin API: /admin/* 
app.include_router(admin_api_router, prefix=settings.API_ADMIN_PREFIX)


# origins = [
#     "http://localhost:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# config static files & Themes
# app.mount("/static", StaticFiles(directory="App/public/static"), name="static")
# app.mount("/js", StaticFiles(directory="App/Themes/admin/dist/js"), name="js")
# app.mount("/css", StaticFiles(directory="App/Themes/admin/dist/css"), name="css")
# AppVue = Jinja2Templates(directory="App/Themes/admin/dist")

# Authenication

@app.on_event("startup")
def startup_event():
    # print(settings)
    pass


@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    app_data = {
        "request": request,
        "app": {
            "name": "App"
        },
    }
    return 'It works!'