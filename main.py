from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.mawaqitController import router as mawaqitRouter

def create_app() -> FastAPI:
    app = FastAPI(title='Mawaqit Api', debug=False, read_root="/")

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins, change to specific domains if needed
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods, change to specific methods if needed
        allow_headers=["*"],  # Allows all headers, change to specific headers if needed
    )
    
    return app

app = create_app()
app.include_router(router=mawaqitRouter)
