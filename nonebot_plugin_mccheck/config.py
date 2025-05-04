from nonebot.plugin import get_plugin_config
from pydantic import BaseModel, Field


class ScopedConfig(BaseModel):
    language: str = Field(default="zh-cn")
    """插件渲染图片所使用的语言"""
    type: int = Field(default=0)
    """插件发送的消息类型"""


class Config(BaseModel):
    mcc: ScopedConfig = Field(default_factory=ScopedConfig)
    """MCCheck Config"""


config: ScopedConfig = get_plugin_config(Config).mcc
