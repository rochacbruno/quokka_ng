from .content.models import make_model, Category
from .content.utils import url_for_content


def configure(app):

    # add context processors
    @app.context_processor
    def app_theme_context():
        context = {**app.theme_context}
        if app.theme_context.get('DISPLAY_RECENT_POSTS_ON_SIDEBAR'):
            context['articles'] = [
                make_model(item)
                for item in app.db.article_set({'published': True})
            ]

        context['pages'] = [
            make_model(item) for item in app.db.page_set({'published': True})
        ]
        # app.theme_context['PAGES']
        # app.theme_context['tags']

        # TODO: Split categories by `/` to get roots
        context['categories'] = [
            (Category(cat), [])
            for cat in app.db.value_set(
                'index', 'category',
                filter={'published': True},
                sort=True
            )
        ]
        # context['tag_cloud']

        menu = build_menu(app)
        if menu:
            context['MENUITEMS'] = menu

        return context


def build_menu(app):
    menu = app.db.get(
        'index',
        {'content_type': 'collection', 'title': 'MENUITEMS', 'published': True}
    )
    if menu and menu.get('collection_items'):
        return [
            build_menu_item(app, item) for item in menu['collection_items']
        ]


def build_menu_item(app, item):
    """Return a name for menu item based on its destination"""
    name = item.get('name')

    if item.get('index_id'):
        content = app.db.get('index', {'_id': item['index_id']})
        return (name or content['title'], url_for_content(content))

    for ref in ['author', 'category', 'tag']:
        data = item.get(f"{ref}_id")
        if not data:
            continue
        return (name or data, make_model(data, ref).url)

    return (name, item['item'])
