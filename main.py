import urllib


def define_env(env):
    @env.filter
    def drawio(image_path):
        image_url = urllib.parse.quote(f"{env.conf['site_url']}{image_path}", "")
        return f"https://app.diagrams.net/?lightbox=1#U{image_url}"