# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .EosAuthorization import EosAuthorization

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosActionUpdateAuth(p.MessageType):

    def __init__(
        self,
        *,
        account: int = None,
        permission: int = None,
        parent: int = None,
        auth: EosAuthorization = None,
    ) -> None:
        self.account = account
        self.permission = permission
        self.parent = parent
        self.auth = auth

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('account', p.UVarintType, 0),
            2: ('permission', p.UVarintType, 0),
            3: ('parent', p.UVarintType, 0),
            4: ('auth', EosAuthorization, 0),
        }
