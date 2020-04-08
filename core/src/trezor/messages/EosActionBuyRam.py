# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .EosAsset import EosAsset

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosActionBuyRam(p.MessageType):

    def __init__(
        self,
        *,
        payer: int = None,
        receiver: int = None,
        quantity: EosAsset = None,
    ) -> None:
        self.payer = payer
        self.receiver = receiver
        self.quantity = quantity

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('payer', p.UVarintType, 0),
            2: ('receiver', p.UVarintType, 0),
            3: ('quantity', EosAsset, 0),
        }
