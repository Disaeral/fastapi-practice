from src.core.config import config

if __name__ == '__main__':
    import uvicorn
    print("uvicorn run port", config.PORT, "host", config.HOST)
    uvicorn.run(
        app='src:infrastructure.app',
        host=config.HOST,
        port=config.PORT,
        reload=True
    )