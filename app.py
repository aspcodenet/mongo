import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["hockey"]

class Player:
    namn:str = ""
    jersey:int  =0

    @classmethod
    def create(cls,in_dict:dict):
        a = cls()
        a.__dict__ = in_dict
        return a    


playersCollection = mydb["players"]

while True:
    print("1. Insert")
    print("2. Update")
    print("3. List all")
    print("4. Sök på nummer")
    print("5. Sök på namn")
    sel = input("Action:")
    if sel == "1":
        p = Player()
        p.namn = input("Namn")
        p.jersey=int(input("jersey"))
        ny = playersCollection.insert_one(p.__dict__)
        # Auto ID ??
        print(f"Nya spelaren fick id:{ny.inserted_id}")
    if sel == "3":
        for x in playersCollection.find():
            player = Player.create(x)    
            print(f"{player.namn} {player.jersey}")

    if sel == "5":
        worda = input("Ange text söka efter")
        query = {"namn": {"$regex": worda + ".*","$options" :'i' }}
        for x in playersCollection.find(query):
            player = Player.create(x)    
            print(f"{player.namn} {player.jersey}")
    if sel == "4":
        num = int(input("Ange nummer att söka efter"))
        query = {"jersey": num}
        for x in playersCollection.find(query):
            player = Player.create(x)    
            print(f"{player.namn} {player.jersey}")
