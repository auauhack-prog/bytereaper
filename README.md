# ByteReaper — 二进制逆向工程平台

# ByteReaper — Binary Reverse Engineering Platform

反汇编 / 反编译 / 恶意软件分析 / 游戏逆向 / 小程序反编译 / APK提取 | PC + App + 小程序全能逆向

Disassemble / Decompile / Malware Analysis / Game Reverse / Mini-Program Reverse / APK Extract | Universal Binary Analysis

---

## 设计原型 / Design Prototypes

### PC 桌面客户端 / PC Desktop Client
![PC Software Design](pc_software_design.png)

### Web 管理后台 / Web Admin Backend
![Web Admin Design](web_admin_design.png)

### 系统架构 / System Architecture
![System Architecture](system_architecture.png)

### App 5屏操作流程 / App 5-Screen Flow
![App Flow Design](app_flow_design.png)

---

## 项目简介

ByteReaper 是一个全能的二进制逆向工程平台，致力于为安全研究人员、逆向工程师、CTF 选手、游戏安全爱好者和移动应用开发者提供一站式的反汇编、反编译和二进制分析解决方案。无论你是需要分析恶意软件的内部逻辑、理解勒索软件的加密例程、逆向 C2 通信协议、检测规避技术，还是想要反编译一个 APK 应用、提取游戏素材资源、分析 Android 小程序的源码结构，甚至是对 PC 端软件进行深度逆向并生成伪 C 代码——ByteReaper 都能在统一的流水线中高效完成。

本项目的核心理念是在汇编和伪 C 代码层面理解二进制文件的内部逻辑、密码学例程、C2 协议和规避技术。ByteReaper 集成了 Ghidra、IDA Pro、radare2、Capstone、Binary Ninja、angr、Frida 等业界顶尖的逆向工程工具，通过 LangGraph 9 节点流水线实现从二进制识别到综合报告生成的全自动化分析。平台支持 Windows PE、Linux ELF、macOS Mach-O、Android APK/AAB、iOS IPA 等全平台二进制格式，覆盖 x86、x64、ARM、ARM64、MIPS、RISC-V 等多种处理器架构。

ByteReaper 的设计初衷是服务于学习与研究目的。我们相信，深入理解软件的内部运行机制是培养下一代安全工程师和逆向分析师的最佳途径。平台的每一项功能都配有详细的分析说明和伪代码输出，让初学者能够循序渐进地从汇编指令理解到高级语言逻辑还原，同时为资深分析师提供多引擎交叉验证和批量自动化分析能力。

---

## 功能模块一览

### 核心逆向引擎

| 模块 | 说明 |
|---|---|
| **多引擎反汇编** | Ghidra / IDA Pro / radare2 / Capstone / Binary Ninja / objdump 多引擎并行反汇编，自动对比分析 |
| **伪C代码反编译** | 反编译为可读伪C/伪Python代码，支持类型恢复、结构体识别、函数签名推断 |
| **控制流图生成** | 自动生成函数级 CFG 可视化，标注基本块、跳转关系和循环结构 |
| **十六进制查看器** | 集成十六进制编辑器，支持结构体映射、交叉引用跳转和模式搜索 |
| **熵值分析** | 自动检测加壳/加密/压缩段，识别 UPX/ASPack/Themida 等常见壳 |
| **PE/ELF/Mach-O 解析** | 完整解析文件头、节表、导入表、导出表、重定位表、资源段等 |

### 恶意软件分析

| 模块 | 说明 |
|---|---|
| **密码学例程识别** | 自动检测 RC4 / AES / DES / XOR / Base64 / CRC32 / MD5 / SHA256 等算法 |
| **C2 协议分析** | 提取 C2 服务器地址、通信协议 (HTTP/HTTPS/DNS/TCP)、beacon 间隔、加密方式 |
| **规避技术检测** | 反调试 (IsDebuggerPresent/NtQueryInformationProcess)、反虚拟机 (CPUID/VBOX/VMware)、混淆 (XOR/Base64 编码)、时序规避 (Sleep/GetTickCount) |
| **字符串分析** | 提取 ASCII/Unicode 字符串，自动标记 IP/URL/文件路径/注册表键 |
| **导入表分析** | 危险 API 调用识别与分类，映射到 MITRE ATT&CK 技术 |
| **YARA 规则匹配** | 内置 200+ 恶意软件 YARA 规则，自动匹配已知恶意软件家族 |
| **行为分析** | 沙箱行为报告分析，进程树/文件操作/网络连接/注册表修改 |
| **IOC 提取** | 自动提取 IP/域名/URL/文件哈希/注册表键/Mutex 等失陷指标 |

### 游戏与小程序逆向

| 模块 | 说明 |
|---|---|
| **Unity 游戏逆向** | 提取 Assembly-CSharp.dll，反编译 IL2CPP，还原 C# 源码逻辑 |
| **Unreal 游戏分析** | UE4/UE5 打包文件解析，提取 .pak/.ucas/.utoc 资源 |
| **微信小程序反编译** | 提取 .wxapkg 包，反编译 WXML/WXSS/JS 代码，还原项目结构 |
| **Android 游戏修改器** | 内存扫描与修改，DLL 注入分析，反作弊绕过分析 |
| **iOS 游戏分析** | IPA 脱壳、Mach-O 分析、越狱检测绕过 |
| **游戏存档分析** | 加解密存档文件，修改游戏数值 |
| **Anti-Cheat 研究** | EAC/BattlEye/Vanguard 等反作弊系统原理分析与绕过思路 |

### 应用与软件反编译

| 模块 | 说明 |
|---|---|
| **APK 反编译提取** | dex2jar/jadx/apktool 全流程，提取 Java/Kotlin 源码、资源文件、AndroidManifest |
| **IPA 分析** | Mach-O 反汇编、class-dump、Swift 符号恢复 |
| **PC 软件反编译** | .NET/Java 反编译 (ILSpy/dnSpy/JD-GUI)、Native 二进制逆向 |
| **固件分析** | 固件解包、文件系统提取、硬编码密钥搜索 |
| **浏览器扩展分析** | Chrome/Firefox 扩展逆向，JavaScript 代码审计 |
| **DLL/驱动分析** | Windows 内核驱动逆向，SSDT Hook 检测 |

### AI 辅助与自动化

| 模块 | 说明 |
|---|---|
| **AI 代码分析** | 集成 Codex / Claude Code / GPT / DeepSeek V4 Pro 等 LLM 辅助理解反编译代码并生成注释 |
| **智能重命名** | 基于语义分析自动重命名函数和变量，提升伪代码可读性 |
| **批量分析** | 批量上传样本，并发分析，统一报告输出 |
| **增量分析** | 同一二进制多次上传只分析变更部分，支持 diff 对比 |
| **报告导出** | Markdown / PDF / JSON / HTML / MITRE ATT&CK Navigator 多格式导出 |
| **API 接口** | RESTful API，支持 CI/CD 集成和自动化安全流水线 |

### 平台与格式兼容

| 平台 | 支持格式 | 架构 |
|---|---|---|
| Windows | .exe / .dll / .sys / .ocx / .msi | x86, x64 |
| Linux | ELF (.so / .o / .ko) | x86, x64, ARM, ARM64, MIPS, RISC-V |
| macOS | Mach-O / .dylib / .app | x64, ARM64 (Apple Silicon) |
| Android | .apk / .aab / .dex / .so | ARM, ARM64, x86 |
| iOS | .ipa / .app | ARM64 |
| 微信小程序 | .wxapkg | N/A |
| 固件 | .bin / .img / .rom | ARM, MIPS |
| .NET | .exe / .dll (CIL) | x86, x64 |
| Web | .js / .wasm (WebAssembly) | N/A |

---

## 9节点 LangGraph 流水线

ByteReaper 采用 LangGraph StateGraph 构建 9 节点自动化分析流水线：

```
identify → disassemble → decompile → cfg → crypto → c2 → evasion → strings_imports → report
```

| 节点 | 功能 | 输出 |
|---|---|---|
| **identify** | 识别二进制格式/平台/架构/编译器/壳/熵值 | file_format, platform, arch |
| **disassemble** | 多引擎反汇编，提取函数列表、基本块、交叉引用 | asm_output, function_list |
| **decompile** | 反编译为伪C代码，类型恢复，结构体和函数签名推断 | pseudo_c_output |
| **cfg** | 生成控制流图 (DOT/PNG)，标注循环和条件分支 | cfg_path |
| **crypto** | 检测密码学例程 (RC4/AES/XOR/Base64/CRC/SHA)，提取密钥常量 | crypto_findings |
| **c2** | 提取 C2 URL/IP/域名、通信协议、加密方式、beacon 间隔 | c2_findings |
| **evasion** | 检测反调试/反VM/混淆/时序规避/进程注入，映射 MITRE ATT&CK | evasion_findings |
| **strings_imports** | 提取 ASCII/Unicode 字符串和导入 API，标记危险调用 | strings_output, imports_output |
| **report** | 汇总所有发现，生成结构化 Markdown/JSON 报告 | report_path |

流水线支持条件路由：当 identify 阶段发现异常（如文件不存在或格式不支持）时直接跳转到 report 节点生成错误报告，避免后续节点空转。

---

## 技术栈

| 层级 | 技术 |
|---|---|
| 编排引擎 | LangGraph + LangChain |
| 反汇编引擎 | Ghidra / IDA Pro / radare2 / Capstone / Binary Ninja |
| 反编译引擎 | Ghidra Decompiler / Hex-Rays / angr decompiler / RetDec |
| 调试框架 | Frida / x64dbg / lldb / gdb |
| AI 辅助 | Codex / Claude Code / GPT-4o / DeepSeek V4 Pro |
| 数据存储 | PostgreSQL / Redis / MinIO |
| 前端 | React / Tailwind CSS / Monaco Editor |
| API | FastAPI / WebSocket |
| 部署 | Docker / Kubernetes |

---

## 外部工具集成

| 工具 | 用途 | 状态 |
|---|---|---|
| [Ghidra](https://ghidra-sre.org/) | NSA 开源逆向框架，含反汇编器和反编译器 | 深度集成 |
| [radare2](https://rada.re/) | UNIX 风格命令行逆向框架 | 深度集成 |
| [IDA Pro](https://hex-rays.com/ida-pro/) | 商业反汇编器和 Hex-Rays 反编译器 | 可选集成 |
| [Capstone](http://www.capstone-engine.org/) | 轻量级多架构反汇编框架 | 内置 |
| [Binary Ninja](https://binary.ninja/) | 现代化商业逆向平台 | 可选集成 |
| [Frida](https://frida.re/) | 跨平台动态插桩工具 | 深度集成 |
| [x64dbg](https://x64dbg.com/) | Windows 开源调试器 | 可选集成 |
| [angr](https://angr.io/) | Python 二进制分析框架 | 内置 |
| [Unicorn](https://www.unicorn-engine.org/) | 轻量级 CPU 模拟器 | 内置 |
| [YARA](https://virustotal.github.io/yara/) | 恶意软件模式匹配 | 内置 |
| [jadx](https://github.com/skylot/jadx) | Android DEX 反编译器 | 内置 |
| [apktool](https://apktool.org/) | APK 反编译工具 | 内置 |

---

## 快速开始

```bash
# 克隆仓库
git clone git@github.com:auauhack-prog/bytereaper.git
cd bytereaper

# 一键启动
chmod +x 启动.command && ./启动.command

# 或手动启动
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python3 graph.py
```

### 配置外部引擎

```bash
# 编辑 .env 文件配置引擎路径
cp .env.example .env
nano .env
```

---

## 项目结构

```
ByteReaper/
├── graph.py                          # LangGraph 9节点流水线入口
├── nodes.py                          # 9个分析节点完整实现
├── tools.py                          # 反汇编/反编译工具客户端
├── state.py                          # 共享状态定义
├── config.json                       # 项目配置 (10+ 功能模块)
├── langgraph.json                    # LangGraph 依赖声明
├── requirements.txt                  # Python 依赖
├── .env.example                      # 环境变量模板
├── .gitignore
├── README.md                         # 项目文档 (中英双语)
├── SKILL.md                          # AI 技能提示词模板
├── 启动.command                       # macOS 一键启动脚本
├── pc_software_design.png            # PC 桌面客户端设计图
├── web_admin_design.png              # Web 管理后台设计图
├── system_architecture.png           # 系统架构设计图
└── app_flow_design.png               # App 5屏操作流程图
```

---

## 应用场景

### 学习研究
- 逆向工程入门教学，从汇编基础到高级反编译
- CTF (Capture The Flag) 竞赛逆向解题辅助
- 二进制漏洞挖掘与利用分析
- 密码学算法逆向学习

### 恶意软件分析
- APT 样本深度逆向与溯源分析
- 勒索软件加密算法逆向与解密工具开发
- 银行木马 C2 协议分析与情报提取
- 供应链攻击样本批量分析与 IOC 提取

### 游戏安全
- 游戏外挂/作弊器原理分析与检测
- Unity/Unreal 游戏资源提取与修改
- 反作弊系统研究与绕过分析
- 游戏协议逆向与封包分析

### 移动安全
- Android/iOS 应用安全审计
- 微信小程序源码反编译与漏洞挖掘
- APK 恶意代码检测与脱壳
- iOS 越狱检测绕过分析

### 软件开发
- 遗留软件逆向重构（无源码维护）
- 第三方 SDK 行为审计
- 竞品软件功能分析（仅限学习研究）
- 文件格式逆向与解析器开发

---

## 免责声明

ByteReaper 仅供学习、研究、安全审计和授权测试使用。使用者应遵守所在国家/地区的法律法规，不得将本工具用于任何非法目的。使用本工具分析非自有软件时，请确保已获得合法授权。作者不对任何滥用行为承担责任。

---

*Generated by Marvis | ByteReaper v1.0.0 — Reverse Engineering Platform*
