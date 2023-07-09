from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware

# from source.champions.admin import ParticipantsAdmin, ChampionAdmin
from source.core.routes import router


from source.db.db import async_engine
from source.news.admin import NewAdmin, NewsTitleAdmin
from source.gallery.admin import GalleryImageAdmin, GalleryTitleAdmin
from source.tournament.admin import TournamentTitleAdmin, TournamentAdmin, TournamentEventAdmin


def create_app() -> FastAPI:
    current_app = FastAPI(title="RODEO KG")

    current_app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    current_app.include_router(router=router)
    return current_app


app = create_app()


admin = Admin(app=app, engine=async_engine)


admin.add_view(NewsTitleAdmin)
admin.add_view(NewAdmin)
admin.add_view(GalleryTitleAdmin)
admin.add_view(GalleryImageAdmin)
admin.add_view(TournamentTitleAdmin)
admin.add_view(TournamentAdmin)
admin.add_view(TournamentEventAdmin)
# admin.add_view(ParticipantsAdmin)
# admin.add_view(ChampionAdmin)

app.mount("/static", StaticFiles(directory="static"), name="static")



if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=12500,
        reload=True,
    )

