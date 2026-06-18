"""ByteReaper Shared State Definition"""
from typing import TypedDict, Optional

class ReaperState(TypedDict):
    binary_path: str
    platform: str
    file_format: str
    arch: Optional[str]
    asm_output: Optional[str]
    pseudo_c_output: Optional[str]
    cfg_path: Optional[str]
    crypto_findings: list
    c2_findings: list
    evasion_findings: list
    strings_output: list
    imports_output: list
    report_path: Optional[str]
    error: Optional[str]
