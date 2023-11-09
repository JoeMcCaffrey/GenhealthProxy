# This is a sample Python script.
from fastapi.security import HTTPBearer

from models.request.embeddings_request import EmbeddingsRequest
from models.request.inference_request import InferenceRequest
from services.genhealth_service import GenhealthService
from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import RedirectResponse
from errors.errors import GenHealthPostException, GenHealthAuthException
def create_app() -> FastAPI:

    app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True})

    # add oauth 2 security. simple way to ask for a token for each response
    # instead of parsing it in each endpoint
    oauth2_scheme = HTTPBearer()

    @app.get('/healthz')
    def healthz():
        return "ok"

    @app.post('/predict')
    async def predict(request: InferenceRequest, token = Depends(oauth2_scheme)):
        health = GenhealthService(url="https://api.genhealth.ai/predict") #move this so its not hardcoded in the future
        health.post_to_genhealth(json_data=request.model_dump_json(), token=token.credentials)

    @app.post('/embeddings')
    async def embeddings(request: EmbeddingsRequest, token=Depends(oauth2_scheme)):
        health = GenhealthService(
            url="https://api.genhealth.ai/predict")  # move this so its not hardcoded in the future
        health.post_to_genhealth(json_data=request.model_dump_json(), token=token.credentials)

    # catch some of these exceptions thrown by post to gen health
    @app.exception_handler(GenHealthAuthException)
    async def auth_failure(request: Request, exc: GenHealthAuthException):
        return Response(status_code=401, content=exc.__str__())

    # add a server error endpoint
    @app.exception_handler(GenHealthPostException)
    async def duplicate_appt(request: Request, exc: GenHealthPostException):
        return Response(status_code=500, content=exc.__str__())

    @app.get('/', include_in_schema=False)
    def root():
        return RedirectResponse('/docs')

    return app

app = create_app()
