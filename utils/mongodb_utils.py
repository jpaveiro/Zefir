from pymongo import MongoClient

class MongoDB_Utils:
    def __init__(self) -> None:
        self.connection_string = "mongodb://localhost:27017/"
        self.client = MongoClient(self.connection_string)
        self.db_connection = self.client["zefir"]
        self.collection_users = self.db_connection.get_collection("users")

    async def insert_user(self, user_id: int) -> None:
        usuario = {
            "user_id": user_id,
            "level": 1,
            "level_xp": 0,
            "money": 0.00,
            "medals": [],
        }

        self.collection_users.insert_one(usuario)
    
    def fetch_user_by_id(self, user_id: int) -> dict:
        return self.collection_users.find_one({"user_id": user_id})
    
    async def register_if_not_exists(self, user_id: int) -> None:
        if (self.fetch_user_by_id(user_id) == None):
            print(f"[REGISTRO] {user_id} não encontrado, registrando...")
            try:
                await self.insert_user(user_id)
            except Exception as e:
                print(f"[REGISTRO] Erro ao registrar usuário com ID {user_id}: {e}")