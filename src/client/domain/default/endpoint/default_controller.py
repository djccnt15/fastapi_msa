from fastapi import APIRouter
from starlette.responses import PlainTextResponse, RedirectResponse

router = APIRouter()


@router.get("/robots.txt", response_class=PlainTextResponse)
async def robots():
    return "User-agent: *\nDisallow: /"


@router.get("/", response_class=RedirectResponse)
async def index_redirect():  # temporal index page redirect to swagger
    return "/docs"


@router.get("/health")
async def helath():
    return 1


@router.get("/ping", response_class=PlainTextResponse)
async def ping():
    return "pong"
