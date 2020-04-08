# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EthereumTxAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 60

    def __init__(
        self,
        *,
        data_chunk: bytes = None,
    ) -> None:
        self.data_chunk = data_chunk

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('data_chunk', p.BytesType, 0),
        }
