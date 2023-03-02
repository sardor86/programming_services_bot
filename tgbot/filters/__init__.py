from .admin import AdminFilter
from .programmer import ProgrammerFilter
from .operator import OperatorFilter
from .privileged_users import PrivilegedUsersFilter


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(ProgrammerFilter)
    dp.filters_factory.bind(OperatorFilter)
    dp.filters_factory.bind(PrivilegedUsersFilter)
