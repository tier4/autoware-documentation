import os
import re
import urllib


def define_env(env):

    @env.filter
    def drawio(image_path):
        image_url = urllib.parse.quote(f"{env.conf['site_url']}{image_path}", "")
        return f"https://app.diagrams.net/?lightbox=1#U{image_url}"

    @env.macro
    def adapi(name):
        match = re.match(r"/api/v\d+/", name)
        if not match:
            return name
        link = name[match.end():].replace("/", "-") + ".md"
        base = "design/autoware-interfaces/ad-api/list/"
        path = os.path.dirname(env.page.file.src_path)
        path = os.path.relpath(base, path)
        path = os.path.join(path, link)
        return f"[{name}]({path})"
