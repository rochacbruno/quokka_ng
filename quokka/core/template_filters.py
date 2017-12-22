# coding: utf-8


# class Menu(list):
#     def __init__(self, items=None):
#         # to use custom append
#         if items:
#             for item in items:
#                 self.append(item)

#     @property
#     def names(self):
#         return (item[0] for item in self)

#     def append(self, item):
#         if item[0] not in self.names:
#             super().append(item)


def configure(app):
    """Configure Jinja filters and globals"""
    # app.jinja_env.filters['isinstance'] = is_instance
    # app.add_template_global(get_content)
    # app.add_template_global(get_contents)

    # populate and add MENUITEMS
    # app.add_template_global(Menu)
