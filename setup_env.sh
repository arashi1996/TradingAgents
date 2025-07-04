#!/bin/bash

echo "🚀 TradingAgents 环境设置"
echo "=========================="

# 检查是否已有API密钥
if [ -n "$FINNHUB_API_KEY" ]; then
    echo "✅ FINNHUB_API_KEY 已设置"
else
    echo "❌ FINNHUB_API_KEY 未设置"
    echo "请访问 https://finnhub.io/ 注册免费账户获取API密钥"
    read -p "请输入您的 FinnHub API 密钥: " finnhub_key
    if [ -n "$finnhub_key" ]; then
        export FINNHUB_API_KEY="$finnhub_key"
        echo "export FINNHUB_API_KEY=\"$finnhub_key\"" >> ~/.zshrc
        echo "✅ FINNHUB_API_KEY 已设置并保存到 ~/.zshrc"
    fi
fi

if [ -n "$OPENAI_API_KEY" ]; then
    echo "✅ OPENAI_API_KEY 已设置"
else
    echo "❌ OPENAI_API_KEY 未设置"
    echo "请访问 https://platform.openai.com/ 注册账户获取API密钥"
    read -p "请输入您的 OpenAI API 密钥: " openai_key
    if [ -n "$openai_key" ]; then
        export OPENAI_API_KEY="$openai_key"
        echo "export OPENAI_API_KEY=\"$openai_key\"" >> ~/.zshrc
        echo "✅ OPENAI_API_KEY 已设置并保存到 ~/.zshrc"
    fi
fi

echo ""
echo "🎉 环境设置完成！"
echo "现在您可以运行以下命令："
echo "1. CLI 界面: python -m cli.main"
echo "2. 直接运行: python main.py"
echo "3. 重新加载环境: source ~/.zshrc" 