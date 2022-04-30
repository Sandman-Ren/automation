from dataclasses import dataclass
from json import JSONDecoder, JSONEncoder
from typing import TypeVar

NotionObjectJSONEncoder = TypeVar("NotionObjectJSONEncoder", bound=JSONEncoder)
NotionObjectJSONDecoder = TypeVar("NotionObjectJSONDecoder", bound=JSONDecoder)


@dataclass
class NotionObject:
    encoder_type: NotionObjectJSONEncoder
    decoder_type: NotionObjectJSONDecoder

    object: str
    id: str
