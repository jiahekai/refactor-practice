# refactor-practice

一个从「50 行乱脚本」重构为「多模块工程」的练习项目。同一个功能，两种写法，用来体会模块拆分、日志和异常处理的价值。

## 功能

批量读取指定文件夹下的 `.txt` 文件，做文本清洗、分句、词频统计，输出：

- `result.csv` — 全部文件的词频汇总表
- `report.md` — 每个文件的句数/词数统计 + TOP10 词频报告

## 项目结构

```
refactor-practice/
├── main.py        # 入口：配置、流程编排、日志、异常处理
├── text_ops.py    # 文本处理：读文件、清洗、分句、分词、计数
├── report.py      # 输出：写 CSV、写 Markdown 报告
└── data/          # 输入文本
```

**职责边界**：`text_ops.py` 和 `report.py` 都是纯函数，只依赖入参、只通过返回值输出，不读写全局状态；`main.py` 负责决定"处理哪个目录、结果存哪里"。

## 运行

```bash
uv venv
uv run python main.py
```

## 设计要点

**模块拆分**

每个文件只负责一件事。改清洗逻辑只动 `text_ops.py`，改输出格式只动 `report.py`，互不影响。

**日志**

统一使用 `logging`，格式为 `时间 [级别] logger名: 消息`。日志配置只写在入口 `main.py`，其他模块通过 `getLogger("docstats")` 复用同一个 logger 实例（同名 logger 是单例，不会重复配置）。

**异常处理**

- `data/` 目录不存在：记录 ERROR 并正常退出，不抛堆栈
- 单个文件编码错误：记录 ERROR，跳过该文件，继续处理其余文件
- 一个坏文件不会拖垮整批任务

**编码**

读写文件统一显式指定 `encoding="utf-8"`，避免 Windows 默认 GBK 导致的乱码和 `UnicodeDecodeError`。

## 已知限制

中文分词目前用正则 `[a-zA-Z\u4e00-\u9fa5]+` 实现。由于中文没有空格分隔，整句中文会被当成一个"词"。真实场景需要用 jieba 等分词工具，或在 RAG 场景中改用向量化 + 分块策略。
