from aiogram.dispatcher import Dispatcher

from .menu import register_menu_handlers
from .up_privilege import register_up_privilege_handler
from .down_privilege import register_down_privilege_handler
from .add_event import register_add_event_handler
from .delete_event import register_delete_event_handler
from .add_service import register_add_service_handler


def register_admin(dp: Dispatcher) -> None:
    register_menu_handlers(dp)
    register_up_privilege_handler(dp)
    register_down_privilege_handler(dp)
    register_add_event_handler(dp)
    register_delete_event_handler(dp)
    register_add_service_handler(dp)
