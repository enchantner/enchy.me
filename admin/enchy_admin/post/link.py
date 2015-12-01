
import os
import os.path

from datetime import datetime

from enchy_admin.config import config


class Link(object):

    def __init__(self, title, link, description, thumbnail, template):
        self.template = template
        self.title = title

        links_path = os.path.join(config.CONTENT_PATH, "links")
        last_link_id = sorted([
            int(lf.split("-")[0]) for lf in os.listdir(links_path)
        ])[-1]
        self.link_id = last_link_id + 1
        self.fullpath = os.path.join(
            links_path,
            "-".join([
                str(self.link_id),
                "_".join(self.title.lower().split(" "))
            ]) + ".rst"
        )
        with open(self.fullpath, "w") as link_file:
            link_file.write(
                self.template.render(
                    title=self.title,
                    datetime=datetime.utcnow().isoformat(' '),
                    description=description,
                    link=link,
                    thumbnail=thumbnail
                )
            )
