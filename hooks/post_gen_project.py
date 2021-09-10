import requests
from cookiecutter.main import cookiecutter
from datetime import date
import subprocess

# aut-generate LICENSE content
license = '{{ cookiecutter.license }}'.lower()
body = requests.get(f"https://api.github.com/licenses/{license}").json()['body']
year = f"{date.today().year}"
fullname = "{{ cookiecutter.author_name }}"
body = body.replace("[year]", year).replace("[fullname]",fullname)
f = open("../{{ cookiecutter.directory_name }}/LICENSE", "w")
f.write(body)
f.close()
