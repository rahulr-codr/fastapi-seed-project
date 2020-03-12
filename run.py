import dotenv
import uvicorn

from sql_app.main import app

if __name__ == "__main__":
    dotenv.load_dotenv(".env")
    uvicorn.run(app, host="0.0.0.0", port=8000)
