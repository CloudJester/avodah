from fastapi import FastAPI
import sqlite3
from routers import jobs

app = FastAPI()
app.include_router(jobs.router)
