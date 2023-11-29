from fastapi import FastAPI
import openai 
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()


class LLM_MODEL_LOADER():

    def llmSearch(key_word: str):
        # gets API Key from environment variable OPENAI_API_KEY
        client = openai(api_key=os.getenv("OPENAI_API_KEY"))

        # Non-streaming:
        print("----- standard request -----")
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    'content': 'Count to 100, with a comma between each number and no newlines. E.g., 1, 2, 3, ...'
                },
            ],
        )
        return completion.choices[0].message.content

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/search/{search_keyword}")
async def read_item(search_keyword: str, q: str ):
    if q:
        return LLM_MODEL_LOADER().llmSearch(search_keyword)
    return {"item_id": search_keyword}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str ):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
