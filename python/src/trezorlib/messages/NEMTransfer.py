# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .NEMMosaic import NEMMosaic

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEMTransfer(p.MessageType):

    def __init__(
        self,
        *,
        mosaics: List[NEMMosaic] = None,
        recipient: str = None,
        amount: int = None,
        payload: bytes = None,
        public_key: bytes = None,
    ) -> None:
        self.mosaics = mosaics if mosaics is not None else []
        self.recipient = recipient
        self.amount = amount
        self.payload = payload
        self.public_key = public_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('recipient', p.UnicodeType, 0),
            2: ('amount', p.UVarintType, 0),
            3: ('payload', p.BytesType, 0),
            4: ('public_key', p.BytesType, 0),
            5: ('mosaics', NEMMosaic, p.FLAG_REPEATED),
        }
