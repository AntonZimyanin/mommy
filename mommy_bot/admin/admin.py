from fastapi import FastAPI, Request, Form,\
    HTTPException
from fastapi.responses import HTMLResponse,\
    RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_303_SEE_OTHER
from sqlalchemy.orm import sessionmaker

from db.models import FactOrm
from db.database import engine


app = FastAPI(title="admin panel")

templates = Jinja2Templates(directory=r"admin\\templates")
app.mount("/static", StaticFiles(directory='admin\static'), name="static")
app.mount("/img", StaticFiles(directory='admin\img'), name="img")


@app.post("/add")
def add(content: str = Form(...)): 
    try: 
        SessionLocal = sessionmaker(autoflush=False, bind=engine)
        db = SessionLocal()
        new_fact = FactOrm(content=content)
        db.add(new_fact)
        db.commit()
        #url = app.url_path_for("/")
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    except:
        raise HTTPException(status_code=500)
        

@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request): 
    return templates.TemplateResponse('add.html', {"request": request})
