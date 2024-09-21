from fastapi.templating import Jinja2Templates
import jinja_partials


templates = Jinja2Templates(directory='src/templates')

jinja_partials.register_starlette_extensions(templates)
