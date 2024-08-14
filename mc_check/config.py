from pydantic import Field, BaseModel
from nonebot.plugin import get_plugin_config


class ScopedConfig(BaseModel):

    mcc_language: str = Field(default="zh-cn")
    """插件渲染图片所使用的语言"""
    mcc_type: int = Field(default=0)
    """插件发送的消息类型"""


class Config(BaseModel):
    status: ScopedConfig = Field(default_factory=ScopedConfig)
    """MCCheck Config"""


config: ScopedConfig = get_plugin_config(Config).status