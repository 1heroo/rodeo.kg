from fastapi import APIRouter
from source.gallery.routes import router as gallery_router
from source.news.routes import router as new_router
from source.tournament.routes import router as tournament_router
from source.champions.routes import router as champion_router


router = APIRouter(prefix='/api/v1')

router.include_router(router=new_router)
router.include_router(router=gallery_router)
router.include_router(router=tournament_router)
router.include_router(router=champion_router)
