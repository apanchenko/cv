from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from prisma import Prisma

from cv.deps import get_db

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")

app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/")
async def home_page(
    request: Request,
    db: Prisma = Depends(get_db),
):
    author = await db.author.find_first(include={
        'address': True,
    })

    return templates.TemplateResponse('index.html', {
        'request': request,
        **author.model_dump(),
        'experience': [
            {
                'position': 'Python developer',
                'since': '2023-03',
                'till': 'present',
                'href': 'https://cs.money/market/',
                'link': 'CS.Money',
                'text': 'Back-end services on python.',
            },
            {
                'position': 'Back-end Developer',
                'since': '2019',
                'till': '2023-03',
                'href': 'https://latoken.com/',
                'link': 'LATOKEN',
                'text': (
                    'Growth team technical lead. Developer of referral program, '
                    'crowdsale, airdrops and trading competition products.'
                ),
                'tech': 'Java (Spring, WebFlux), Python, Js (React, MobX), kubernetes, gRPC, Kafka, Postgres, Redis',
            },
            {
                'position': 'Developer',
                'since': '2009',
                'till': '2019',
                'href': 'https://panzar.com/',
                'link': 'Panzar Studio',
                'text': (
                    'Developer of multiplayer AAA games: <a href="https://store.steampowered.com/app/240320/Panzar/">Panzar</a>, '
                    '<a href="https://store.steampowered.com/app/1121710/Total_Lockdown/">Total Lockdown</a>. '
                    'Created user interface framework. Responsible for game business logic, Steam integration, '
                    'Chinese and Arabic localization, Back-end services.'
                ),
                'tech': 'C++11, <a href="https://www.cryengine.com/">Cry Engine</a>, <a href="https://www.unrealengine.com/en-US/">Unreal Engine</a>',
            },
            {
                'position': 'Software engineer',
                'since': '2003',
                'till': '2019',
                'href': 'https://en.wikipedia.org/wiki/Reaxion',
                'link': 'Reaxion',
                'text': 'BREW and J2ME applications and games development and porting.',
                'tech': (
                    'Shipped projects: MMS Client, Evel Knievel, Rug Rats, The Longest Yard, Mahjong '
                    'Deluxe, Frame Games, Go Fish!, Aviga Mobile, America\'s Next Top Model, Bumper Stars.'
                ),
            },
            {
                'position': 'Software developer',
                'since': '2000',
                'till': '2002',
                'link': 'Saybervizhn',
                'text': (
                    'Participation in project of development Surveillance Manager system of fault management multi-vendor '
                    'telecommunications network. Design and developedment of fault and discovery adapter plug-ins for '
                    'Lucent AnyMedia and Cisco CWM.'
                ),
                'tech': 'Java, CORBA, XML',
            },
        ],
        'education': [
            {
                'text': 'Machine Learning. Coursera',
                'href': 'https://www.coursera.org/account/accomplishments/verify/C7QERZ8DRNJZ',
                'link': 'C7QERZ8DRNJZ',
            },
            {
                'text': 'Algorithms and Data Structures in Python. Udemy',
                'href': 'https://www.udemy.com/certificate/UC-4I10CZQO/',
                'link': 'UC-4I10CZQO',
            },
            {
                'text': 'MS, Applied Mathematics and Physics.',
                'href': 'https://mipt.ru/english/',
                'link': 'MIPT',
                'year': '2002',
            },
            {
                'href': 'https://en.wikipedia.org/wiki/Ukrainian_Physics_and_Mathematics_Lyceum',
                'link': 'Ukrainian Physical and Mathematical Lyceum.',
                'abbr': 'UPML',
                'year': '1996',
            },
            {
                'text': 'Regional olympiads in mathematics.',
            },
        ],
        'skills': ['Python', 'Java', 'C++', 'Game Development', 'User Interface', 'Scrum']
    })
