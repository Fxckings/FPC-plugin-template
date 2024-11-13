from __future__ import annotations

import logging
from locales.localizer import Localizer
from cardinal import Cardinal
from FunPayAPI.updater.events import NewOrderEvent, NewMessageEvent

logger = logging.getLogger(__name__)
"""Создаем логгер."""

localizer = Localizer()
_ = localizer.translate
"""Локализ."""

NAME = "Template Plug-In"
"""Название вашего плагина (будет отображаться только в тг)."""

VERSION = "0.0.1"
"""Версия, совершенно любая (будет отображаться только в тг)."""

DESCRIPTION = "Тест плаген."
"""Описание плагина, будет отображаться при нажатии на плагин в списке плагинов (будет отображаться только в тг)."""

CREDITS = "@cloudecode | https://funpay.com/users/10231791/ | @tinkovof"
"""Кредиты, ваш юз/ссылка/все что угодно (будет отображаться только в тг)."""

UUID = "b14ecdd8-bc59-4831-944a-4ad76590ff52"
"""Ююайди плагина, нужно брать с: https://www.uuidgenerator.net/"""

SETTINGS_PAGE = False
"""Будет ли кнопка "настройки" у плагина (будет отображаться только в тг)"""

logger.info(f"[{NAME}] (Плагееен загружееен!!)")
"""Опционально можно сделать лог при загрузке плагина."""

def new_message_handler(cardinal: Cardinal, event: NewMessageEvent) -> None:
    """Хендлер нового сообщения."""
    logger.info(f"Написал новый пользователь: {e.message.chat_name}")

    """
    Основное:
    e.message.chat_name - название чата

    дальше сами
    """

def new_order_handler(cardinal: Cardinal, event: NewOrderEvent) -> None:
    """Хендлер нового заказа."""
    logger.info(f"Новый заказ: {e.order.id}")
    """
    Основное:
    e.order.id - айди заказа
    e.order.amount - сумма заказа

    дальше сами
    """

def init_cardinal(cardinal: Cardinal) -> None:
    """Что будет при инициализации плагина."""
    pass

BIND_TO_PRE_INIT = [init_cardinal]
BIND_TO_NEW_ORDER = [new_order_handler]
BIND_TO_NEW_MESSAGE = [new_message_handler]
BIND_TO_DELETE = None