import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://s224740132_sit772_part1_user:9mdgsfRF4HkWd24MUOs8MMcDbGIL1dQZ@dpg-cqs2hu8gph6c73a6n5rg-a.oregon-postgres.render.com/s224740132_sit772_part1")

settings = Settings()
