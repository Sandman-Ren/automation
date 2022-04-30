from dataclasses import dataclass
from typing import List, TypeVar

from notion.models.base import NotionObject
from notion.models.common import RichText
from notion.models.user import PartialUser

BlockType = TypeVar("BlockType", bound="Block")


class Block(NotionObject):
    created_time: str
    created_by: PartialUser
    last_edited_time: str
    last_edited_by: PartialUser
    has_children: bool
    type: str
    archived: bool


class Paragraph(Block):
    @dataclass
    class ParagraphContent:
        rich_text: List[RichText]
        color: str
        children: List[Block]

    type: str = 'paragraph'
    paragraph: ParagraphContent

@dataclass
class HeadingContent:
    rich_text: List[RichText]


class HeadingOneBlock(Block):
    type: str = 'heading_1'
    # heading_1: