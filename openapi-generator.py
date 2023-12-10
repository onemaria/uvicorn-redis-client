import json
from main import app
from fastapi.openapi.utils import get_openapi


with open('openapi.json', 'w') as f:
    json.dump(get_openapi(
        title="uvicorn-redis-client",
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
    ), f)
