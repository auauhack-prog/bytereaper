"""ByteReaper Tools — Disassembler/Decompiler Clients & Utilities"""
import subprocess
import json
from pathlib import Path
from typing import Optional

def run_radare2(binary: str, cmd: str = "aaaa") -> str:
    """Run radare2 analysis on a binary."""
    try:
        result = subprocess.run(
            ["r2", "-q", "-c", cmd, binary],
            capture_output=True, text=True, timeout=60
        )
        return result.stdout
    except FileNotFoundError:
        return "[radare2 not installed]"
    except Exception as e:
        return f"[radare2 error: {e}]"

def run_capstone_disasm(hex_bytes: str, arch: str = "x64") -> str:
    """Disassemble raw hex bytes using Capstone."""
    try:
        from capstone import Cs, CS_ARCH_X86, CS_MODE_64
        md = Cs(CS_ARCH_X86, CS_MODE_64)
        code = bytes.fromhex(hex_bytes)
        lines = [f"{i.address:#x}: {i.mnemonic} {i.op_str}" 
                 for i in md.disasm(code, 0x1000)]
        return "\n".join(lines)
    except ImportError:
        return "[capstone not installed]"

def extract_apk(apk_path: str, output_dir: str):
    """Extract APK contents (dex, resources, lib)."""
    import zipfile
    with zipfile.ZipFile(apk_path, 'r') as zf:
        zf.extractall(output_dir)

def scan_memory_pattern(pid: int, pattern: bytes) -> list:
    """Memory pattern scan using Frida (placeholder)."""
    return [{"address": "0x7f000000+offset", "matches": "N/A"}]
