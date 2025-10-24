from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = "mysql+pymysql://root:Soumya@localhost:3306/fastapi_db"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        result = connection.execute("SELECT 1")
        print("✅ Connection successful:", result.scalar())
except SQLAlchemyError as e:
    print("❌ Connection failed:", e)
