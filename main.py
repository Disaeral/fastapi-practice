from src.core.config import config

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        app='src:app',
        host=config.HOST,
        port=config.PORT,
        reload=True
    )