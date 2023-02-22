from .admin import AdminFilter


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)
