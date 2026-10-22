# AI 智能伴侣

基于 Streamlit + DeepSeek API 的 AI 对话应用。

## 功能

- 网页端与 AI 助手多轮对话
- 接入 DeepSeek 大模型（deepseek-flash）

## 本地运行

1. 安装依赖：

```bash
pip install streamlit openai
```

2. 配置 API Key（环境变量，不写入代码）：

```bash
# Windows CMD
set DEEPSEEK_API_KEY=你的Key
# Windows PowerShell
$env:DEEPSEEK_API_KEY="你的Key"
```

3. 启动应用：

```bash
streamlit run AI_partner.py
```

## 说明

- API Key 通过环境变量 `DEEPSEEK_API_KEY` 读取，仓库中不包含任何密钥。
- 运行前需自行申请 DeepSeek API Key：https://platform.deepseek.com
