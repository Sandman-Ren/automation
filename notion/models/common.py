from dataclasses import dataclass


@dataclass
class RichText:
    @dataclass
    class Annotations:
        bold: bool
        italic: bool
        strikethrough: bool
        underline: bool
        code: bool
        color: str
    plain_text: str
    href: str
    annotations: Annotations
    type: str   # one of text, mention, equation
