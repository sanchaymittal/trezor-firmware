# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TxRequestSerializedType(p.MessageType):

    def __init__(
        self,
        *,
        signature_index: int = None,
        signature: bytes = None,
        serialized_tx: bytes = None,
    ) -> None:
        self.signature_index = signature_index
        self.signature = signature
        self.serialized_tx = serialized_tx

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('signature_index', p.UVarintType, 0),
            2: ('signature', p.BytesType, 0),
            3: ('serialized_tx', p.BytesType, 0),
        }
