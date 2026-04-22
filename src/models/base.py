from sqlalchemy.orm import DeclarativeBase
from advanced_alchemy.mixins import AuditColumns


class Base(DeclarativeBase, AuditColumns):
    pass
