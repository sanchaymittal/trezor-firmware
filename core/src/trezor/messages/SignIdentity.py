# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .IdentityType import IdentityType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class SignIdentity(p.MessageType):
    MESSAGE_WIRE_TYPE = 53

    def __init__(
        self,
        *,
        identity: IdentityType = None,
        challenge_hidden: bytes = None,
        challenge_visual: str = None,
        ecdsa_curve_name: str = None,
    ) -> None:
        self.identity = identity
        self.challenge_hidden = challenge_hidden
        self.challenge_visual = challenge_visual
        self.ecdsa_curve_name = ecdsa_curve_name

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('identity', IdentityType, 0),
            2: ('challenge_hidden', p.BytesType, 0),
            3: ('challenge_visual', p.UnicodeType, 0),
            4: ('ecdsa_curve_name', p.UnicodeType, 0),
        }
