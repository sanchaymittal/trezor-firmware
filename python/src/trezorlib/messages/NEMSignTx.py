# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .NEMAggregateModification import NEMAggregateModification
from .NEMImportanceTransfer import NEMImportanceTransfer
from .NEMMosaicCreation import NEMMosaicCreation
from .NEMMosaicSupplyChange import NEMMosaicSupplyChange
from .NEMProvisionNamespace import NEMProvisionNamespace
from .NEMTransactionCommon import NEMTransactionCommon
from .NEMTransfer import NEMTransfer

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEMSignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 69

    def __init__(
        self,
        *,
        transaction: NEMTransactionCommon = None,
        multisig: NEMTransactionCommon = None,
        transfer: NEMTransfer = None,
        cosigning: bool = None,
        provision_namespace: NEMProvisionNamespace = None,
        mosaic_creation: NEMMosaicCreation = None,
        supply_change: NEMMosaicSupplyChange = None,
        aggregate_modification: NEMAggregateModification = None,
        importance_transfer: NEMImportanceTransfer = None,
    ) -> None:
        self.transaction = transaction
        self.multisig = multisig
        self.transfer = transfer
        self.cosigning = cosigning
        self.provision_namespace = provision_namespace
        self.mosaic_creation = mosaic_creation
        self.supply_change = supply_change
        self.aggregate_modification = aggregate_modification
        self.importance_transfer = importance_transfer

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('transaction', NEMTransactionCommon, 0),
            2: ('multisig', NEMTransactionCommon, 0),
            3: ('transfer', NEMTransfer, 0),
            4: ('cosigning', p.BoolType, 0),
            5: ('provision_namespace', NEMProvisionNamespace, 0),
            6: ('mosaic_creation', NEMMosaicCreation, 0),
            7: ('supply_change', NEMMosaicSupplyChange, 0),
            8: ('aggregate_modification', NEMAggregateModification, 0),
            9: ('importance_transfer', NEMImportanceTransfer, 0),
        }
