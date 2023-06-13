
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse



import jinja2

app = FastAPI()

app.mount("/static",StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/")

@app.get("/")
async def homepage(request:Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.get("/technicalskills")
async def technicalskills(request: Request):
    return templates.TemplateResponse("technicalskills.html", {"request": request})

@app.get("/education")
async def education(request:Request):
    return templates.TemplateResponse("education.html", {"request": request})

@app.get("/github")
def redirect_to_github():
    github_link= "https://github.com/PrathaGautam"
    return RedirectResponse(url=github_link)

@app.get("/linkedin")
def redirect_to_linkedin():
    linkedin_link = "https://www.linkedin.com/in/pratha-gautam-2a048b191/"
    return RedirectResponse(url=linkedin_link)

@app.get("/gmail")
def redirect_to_gmail():
    email = "prathagautam40@gmail.com"
    mailto_link = f'mailto:{email}'
    return RedirectResponse(url=mailto_link)

@app.get("/projects")
async def projects(request:Request):
    return templates.TemplateResponse("projects.html", {"request": request})

@app.get("/demo_ecommerce")
def redirect_to_linkedin():
    youtube_link = "https://www.youtube.com/watch?v=XHXHyNK1syc"
    return RedirectResponse(url=youtube_link)

@app.get("/banking_OOP")
def redirect_to_linkedin():
    github_link = "https://github.com/PrathaGautam/BankingSystemOOP"
    return RedirectResponse(url=github_link)

@app.get("/RPS")
def redirect_to_linkedin():
    github_link = "https://github.com/PrathaGautam/RockPaperScissors"
    return RedirectResponse(url=github_link)

@app.get("/contact")
def contact_page(request:Request):
    return templates.TemplateResponse("contact.html",  {"request": request})

@app.get("/softskills")
async def softskills(request: Request):
    return templates.TemplateResponse("softskills.html", {"request": request})

@app.get("/portfolio")
def redirect_to_portfolio():
    github_link = "https://github.com/PrathaGautam/My_Portfolio"
    return RedirectResponse(url=github_link)

@app.get("/calculator")
def redirect_to_calcu():
    github_link = "https://github.com/PrathaGautam/Unusual_Calculator"
    return RedirectResponse(url=github_link)