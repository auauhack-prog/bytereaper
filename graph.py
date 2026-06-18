"""
ByteReaper - Binary Reverse Engineering Platform
LangGraph StateGraph: 9节点反编译+恶意软件分析流水线
"""
from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END

class ReaperState(TypedDict):
    binary_path: str
    platform: str  # pc / mobile
    file_format: str  # PE / ELF / Mach-O / APK / IPA
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

from nodes import (
    identify_binary, disassemble_binary, decompile_binary,
    generate_cfg, analyze_crypto, analyze_c2,
    detect_evasion, extract_strings_imports, generate_report
)

def build_graph():
    workflow = StateGraph(ReaperState)
    
    workflow.add_node("identify", identify_binary)
    workflow.add_node("disassemble", disassemble_binary)
    workflow.add_node("decompile", decompile_binary)
    workflow.add_node("cfg", generate_cfg)
    workflow.add_node("crypto", analyze_crypto)
    workflow.add_node("c2", analyze_c2)
    workflow.add_node("evasion", detect_evasion)
    workflow.add_node("strings_imports", extract_strings_imports)
    workflow.add_node("report", generate_report)
    
    workflow.set_entry_point("identify")
    workflow.add_conditional_edges("identify", lambda s: "error" if s.get("error") else "disassemble",
                                    {"disassemble": "disassemble", "error": "report"})
    workflow.add_edge("disassemble", "decompile")
    workflow.add_edge("decompile", "cfg")
    workflow.add_edge("cfg", "crypto")
    workflow.add_edge("crypto", "c2")
    workflow.add_edge("c2", "evasion")
    workflow.add_edge("evasion", "strings_imports")
    workflow.add_edge("strings_imports", "report")
    workflow.add_edge("report", END)
    
    return workflow.compile()

if __name__ == "__main__":
    graph = build_graph()
    result = graph.invoke({"binary_path": "/path/to/malware.exe", "platform": "pc"})
    print(result)
