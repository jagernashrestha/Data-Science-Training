#ctrl+c = break server
# cls = clear
# uv add fastapi
# uv add "fastapi[standard]"


from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
async def get_items():
    return[
        {
            "name" : "item1"
        },
        {
           "name":"item2"
        }
    ]
