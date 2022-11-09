import uvicorn
from os import getenv
from fastapi import FastAPI, Request

"""
That's the entrypoint to run the project
"""


def get_application() -> FastAPI:

    app = FastAPI(debug=getenv("DEBUG", False))

    # TODO : middleware missing
    # TODO : CORS missing
    # TODO : Header missing

    return app


app = get_application()


@app.get("/")
async def read_root(request: Request):

    # TODO : optional authentication method
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
