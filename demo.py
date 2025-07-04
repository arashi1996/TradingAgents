#!/usr/bin/env python3
"""
TradingAgents 演示脚本
展示如何使用多代理LLM金融交易框架
"""

import os
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

def check_api_keys():
    """检查API密钥是否设置"""
    finnhub_key = os.getenv("FINNHUB_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    
    print("🔑 API密钥检查:")
    print(f"   FinnHub API: {'✅ 已设置' if finnhub_key else '❌ 未设置'}")
    print(f"   OpenAI API: {'✅ 已设置' if openai_key else '❌ 未设置'}")
    
    if not finnhub_key or not openai_key:
        print("\n⚠️  请先设置API密钥:")
        print("   1. 运行: ./setup_env.sh")
        print("   2. 或者手动设置环境变量")
        return False
    return True

def demo_basic_usage():
    """演示基本用法"""
    print("\n🚀 演示基本用法")
    print("=" * 50)
    
    # 创建配置
    config = DEFAULT_CONFIG.copy()
    config["deep_think_llm"] = "gpt-4o-mini"
    config["quick_think_llm"] = "gpt-4o-mini"
    config["max_debate_rounds"] = 1
    config["online_tools"] = True
    
    print("📊 配置信息:")
    print(f"   深度思考模型: {config['deep_think_llm']}")
    print(f"   快速思考模型: {config['quick_think_llm']}")
    print(f"   辩论轮数: {config['max_debate_rounds']}")
    print(f"   在线工具: {config['online_tools']}")
    
    try:
        # 初始化TradingAgents
        print("\n🔧 初始化TradingAgents...")
        ta = TradingAgentsGraph(debug=True, config=config)
        
        # 运行分析
        print("\n📈 开始分析 NVDA 股票 (2024-05-10)...")
        print("⏳ 这可能需要几分钟时间，请耐心等待...")
        
        _, decision = ta.propagate("NVDA", "2024-05-10")
        
        print("\n🎯 分析结果:")
        print("=" * 50)
        print(decision)
        
    except Exception as e:
        print(f"\n❌ 运行出错: {e}")
        print("请检查API密钥是否正确设置")

def demo_cli_usage():
    """演示CLI用法"""
    print("\n💻 演示CLI界面")
    print("=" * 50)
    print("要启动CLI界面，请运行:")
    print("   python -m cli.main")
    print("\nCLI界面功能:")
    print("   ✅ 交互式股票选择")
    print("   ✅ 日期选择")
    print("   ✅ 模型配置")
    print("   ✅ 实时进度显示")
    print("   ✅ 详细分析报告")

def demo_custom_config():
    """演示自定义配置"""
    print("\n⚙️  演示自定义配置")
    print("=" * 50)
    
    # 创建自定义配置
    custom_config = DEFAULT_CONFIG.copy()
    custom_config.update({
        "deep_think_llm": "gpt-4o",  # 使用更强大的模型
        "quick_think_llm": "gpt-4o",
        "max_debate_rounds": 2,  # 增加辩论轮数
        "max_risk_discuss_rounds": 2,
        "online_tools": True,
    })
    
    print("🔧 自定义配置示例:")
    for key, value in custom_config.items():
        if key in ["deep_think_llm", "quick_think_llm", "max_debate_rounds", "max_risk_discuss_rounds", "online_tools"]:
            print(f"   {key}: {value}")
    
    print("\n💡 配置建议:")
    print("   • 使用 gpt-4o-mini 节省成本")
    print("   • 使用 gpt-4o 获得更好结果")
    print("   • 增加辩论轮数获得更深入分析")
    print("   • 启用在线工具获取实时数据")

def main():
    """主函数"""
    print("🎉 TradingAgents 演示")
    print("=" * 60)
    print("多代理LLM金融交易框架")
    print("基于 LangGraph 构建")
    print("=" * 60)
    
    # 检查API密钥
    if not check_api_keys():
        return
    
    # 演示各种用法
    demo_basic_usage()
    demo_cli_usage()
    demo_custom_config()
    
    print("\n🎯 总结")
    print("=" * 60)
    print("✅ 框架已成功安装")
    print("✅ 依赖包已安装")
    print("✅ 可以开始使用")
    print("\n📚 更多信息:")
    print("   • 查看使用指南.md")
    print("   • 访问 GitHub: https://github.com/TauricResearch/TradingAgents")
    print("   • 阅读论文: https://arxiv.org/abs/2412.20138")

if __name__ == "__main__":
    main() 