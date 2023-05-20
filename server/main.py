from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    '*',
    'http://localhost:5173/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

imgs = [
        {  "url": "https://t3.ftcdn.net/jpg/05/48/56/38/360_F_548563894_s5tGFJjPhc7lp5uG4iJkR77QbgvrKr9e.webp",  "title": "Mountain",},
        {  "url": "https://t3.ftcdn.net/jpg/05/68/49/90/240_F_568499083_q9QfafI1PkGJA8QQMIpiTT557xUUJ4Qq.jpg",  "title": "Forest",},
        {  "url": "https://t4.ftcdn.net/jpg/05/55/71/83/240_F_555718315_XAi4cgO4s2uBRshlJZ8wXjAWkptX8023.jpg",  "title": "Moon",}
        ]

@app.get("/")
async def root():
    return { "data": imgs}
    

@app.get("/add")
async def add_item(img_url,title):
    img =  {"url": img_url, 'title': title}
    imgs.append(img)
    return imgs