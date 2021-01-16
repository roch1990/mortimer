from config import Config
from aiopg.sa import create_engine


class Postgres:

    def __init__(self):
        self.user = Config.db_user
        self.database = Config.db_name
        self.host = Config.db_host
        self.port = Config.db_port
        self.password = Config.db_pass

    async def connect(self):
        return await create_engine(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )

    async def wait_close(self):
        pass
