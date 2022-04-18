import os
import re
import urllib


def define_env(env):

    @env.filter
    def drawio(image_path):
        image_url = urllib.parse.quote(f"{env.conf['site_url']}{image_path}", "")
        return f"https://app.diagrams.net/?lightbox=1#U{image_url}"

    @env.filter
    def link_api_type(name):
        path = os.path.relpath("design/autoware-interfaces/ad-api/types", env.page.file.src_path)
        link =  name.split("/")
        link = "/".join([*link[:-1], camel_to_snake(link[-1])])
        link = os.path.join(path, link)
        return f"[{name}]({link})"

    @env.filter
    def link_api_root(path):
        base = os.path.relpath("design/autoware-interfaces/ad-api", env.page.file.src_path)
        return os.path.join(base, path)

def camel_to_snake(text):
    text = re.sub("(.)([A-Z][a-z]+)", R"\1_\2", text)
    text = re.sub("([a-z0-9])([A-Z])", R"\1_\2", text)
    return text.lower()
