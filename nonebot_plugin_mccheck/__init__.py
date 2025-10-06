import itertools

from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters
from .config import Config
from .configs import lang, lang_data
from .utils import (
    change_language_to,
    get_message_list,
    handle_exception,
    is_qbot,
    is_validity_address,
    parse_host,
)

require("nonebot_plugin_alconna")
require("nonebot_plugin_uninfo")
from arclet.alconna import Alconna, Args, CommandMeta
from nonebot_plugin_alconna import Match, Text, UniMessage, on_alconna
from nonebot_plugin_uninfo import Uninfo

__plugin_meta__ = PluginMetadata(
    name="Minecraft查服",
    description="Minecraft服务器状态查询，支持IPv6",
    type="application",
    homepage="https://github.com/molanp/nonebot_plugin_mccheck",
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_alconna", "nonebot_plugin_uninfo"
    ),
    config=Config,
    usage="""
    Minecraft服务器状态查询，支持IPv6
    用法：
        查服 [ip]:[端口] / 查服 [ip]
        设置语言 zh-cn
        当前语言
        语言列表
    eg:
        mcheck ip:port / mcheck ip
        set_lang en
        lang_now
        lang_list
    """.strip(),
    extra={"author": "molanp <luotian233@foxmail.com>"},
)

check = on_alconna(
    Alconna("mcheck", Args["host?", str], meta=CommandMeta(compact=True)),
    aliases={"查服"},
    priority=5,
    block=True,
)


lang_change = on_alconna(
    Alconna("set_lang", Args["language", str], meta=CommandMeta(compact=True)),
    aliases={"设置语言"},
    priority=5,
    block=True,
)

lang_now = on_alconna(
    Alconna("lang_now", meta=CommandMeta(compact=True)),
    aliases={"当前语言"},
    priority=5,
    block=True,
)

lang_list = on_alconna(
    Alconna("lang_list", meta=CommandMeta(compact=True)),
    aliases={"语言列表"},
    priority=5,
    block=True,
)


@check.handle()
async def _(host: Match[str], session: Uninfo):
    if not host.available:
        await check.finish(Text(f"{lang_data[lang]['where_ip']}"), reply_to=True)
    address, port = await parse_host(host.result)

    if not str(port).isdigit() or not (0 <= int(port) <= 65535):
        await check.finish(Text(f"{lang_data[lang]['where_port']}"), reply_to=True)

    if is_validity_address(address):
        await get_info(address, port, session)
        return


async def get_info(ip, port, session):
    global ms

    try:
        message_list = await get_message_list(ip, port, 3)
        if is_qbot(session):
            for m in message_list:
                await check.send(UniMessage(m), reply_to=True)
        else:
            message_list = list(itertools.chain.from_iterable(message_list))
            await check.send(UniMessage(message_list), reply_to=True)
    except BaseException as e:
        await check.send(handle_exception(e), reply_to=True)


@lang_change.handle()
async def _(language: str):
    if language:
        await lang_change.send(Text(change_language_to(language)), reply_to=True)
    else:
        await lang_change.send(Text("Language?"), reply_to=True)


@lang_now.handle()
async def _():
    await lang_now.send(Text(f"Language: {lang}."), reply_to=True)


@lang_list.handle()
async def _():
    i = "\n".join(list(lang_data.keys()))
    await lang_list.send(Text(f"Language List:\n{i}"), reply_to=True)
