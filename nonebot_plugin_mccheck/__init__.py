from nonebot import require
from nonebot.log import logger  # type: ignore
from nonebot.plugin import PluginMetadata  # type: ignore
from nonebot.exception import FinishedException  # type: ignore
require("nonebot_plugin_alconna")
from nonebot_plugin_alconna import Alconna, Args, on_alconna, Match, UniMessage  # type: ignore
from nonebot_plugin_alconna.uniseg import Text, Image  # type: ignore
from .config import config as plugin_config
from .config import Config
from .untils import (
    is_invalid_address,
    ColoredTextImage,
    parse_motd,
    parse_motd_to_html,
    readInfo,
    get_mc,
    resolve_srv
)
import re
import os
import traceback
import sys
import base64


__version__ = "0.1.17"

__plugin_meta__ = PluginMetadata(
    name="Minecraft查服",
    description="Minecraft服务器状态查询，支持IPv6/Minecraft server status query, IPv6 supported",
    type="application",
    homepage="https://github.com/molanp/nonebot_plugin_mccheck",
    config=Config,
    usage=f"""
    Minecraft服务器状态查询，支持IPv6
    用法：
        查服 [ip]:[端口] / 查服 [ip]
        设置语言 zh-cn
        当前语言
        语言列表
    usage:
        mcheck ip:port / mcheck ip
        set_lang en
        lang_now
        lang_list
    """.strip(),
    extra={
        "unique_name": "MCCheck",
        "example": "mcheck",
        "author": "molanp <luotian233@foxmail.com>",
        "version": __version__,
    },
)


message_type = plugin_config.type
lang = plugin_config.language
lang_data = readInfo("language.json")

check = on_alconna(
    Alconna("mcheck", Args["host?", str]),
    aliases={"查服"},
    priority=5,
    block=True,
)


lang_change = on_alconna(
    Alconna("set_lang", Args["language", str]),
    aliases={"设置语言"},
    priority=5,
    block=True,
)

lang_now = on_alconna(
    Alconna("lang_now"),
    aliases={"当前语言"},
    priority=5,
    block=True,
)

lang_list = on_alconna(
    Alconna("lang_list"),
    aliases={"语言列表"},
    priority=5,
    block=True,
)


@check.handle()
async def _(host: Match[str]):
    if host.available:
        check.set_path_arg("host", host.result)


@check.got_path("host", prompt=lang_data[lang]["where_ip"])
async def handle_check(host: str):
    address, port = parse_host(host)

    if not str(port).isdigit() or not (0 <= int(port) <= 65535):
        await check.finish(Text(f' {lang_data[lang]["where_port"]}'), at_sender=True)

    if is_invalid_address(address):
        await check.finish(Text(f' {lang_data[lang]["where_ip"]}'), at_sender=True)

    await get_info(address, port)


async def get_info(ip, port):
    global ms

    try:
        srv = await resolve_srv(ip, port)
        ms = await get_mc(srv[0], int(srv[1]), timeout=1)
        if ms.online:
            result = build_result(ms, message_type)
            await send_message(message_type, result, ms.favicon, ms.favicon_b64)
        else:
            await check.finish(Text(f' {lang_data[lang][str(ms.connection_status)]}'), at_sender=True)
    except FinishedException:
        pass
    except BaseException as e:
        await handle_exception(e)


def parse_host(host_name):
    if '.' in host_name:
        parts = host_name.strip().split(':')
        address = parts[0]
        port = parts[1] if len(parts) > 1 else 0
    else:
        pattern = r'\[(.+)\](?::(\d+))?$'
        match = re.match(pattern, host_name)
        address = match.group(1)  # type: ignore
        port = match.group(2) if match.group(2) else 0  # type: ignore

    return address, port


def build_result(ms, type=0):
    status = f'{ms.connection_status}|{lang_data[lang][str(ms.connection_status)]}'
    if type == 0:
        return {
            "favicon": ms.favicon_b64 if ms.favicon is not None and ms.favicon != "" else "no_favicon.png",
            "version": parse_motd_to_html(ms.version),
            "slp_protocol": str(ms.slp_protocol),
            "address": ms.address,
            "port": ms.port,
            "delay": f"{ms.latency}ms",
            "gamemode": ms.gamemode,
            "motd": parse_motd_to_html(ms.motd),
            "players": f'{ms.current_players}/{ms.max_players}',
            "status": f'{ms.connection_status}|{lang_data[lang][str(ms.connection_status)]}',
            "lang": lang_data[lang]
        }
    elif type == 1:
        motd_part = f'\n{lang_data[lang]["motd"]}{parse_motd(ms.motd)}'
        version_part = f'\n{lang_data[lang]["version"]}{parse_motd(ms.version)}'
    elif type == 2:
        motd_part = f'\n{lang_data[lang]["motd"]}{ms.stripped_motd}'
        version_part = f'\n{lang_data[lang]["version"]}{ms.version}'

    base_result = (
        f' {version_part}'
        f'\n{lang_data[lang]["slp_protocol"]}{ms.slp_protocol}'
        f'\n{lang_data[lang]["address"]}{ms.address}'
        f'\n{lang_data[lang]["port"]}{ms.port}'
        f'\n{lang_data[lang]["delay"]}{ms.latency}ms'
    )

    if 'BEDROCK' in str(ms.slp_protocol):
        base_result += f'\n{lang_data[lang]["gamemode"]}{ms.gamemode}'

    result = (
        base_result +
        motd_part +
        f'\n{lang_data[lang]["players"]}{ms.current_players}/{ms.max_players}'
        f'\n{lang_data[lang]["status"]}{status}'
    )

    return result


async def send_message(type, result, favicon, favicon_b64):
    if type == 0:
        await send_html_message(result)
    elif type == 1:
        await send_image_message(result, favicon, favicon_b64)
    elif type == 2:
        await send_text_message(result, favicon, favicon_b64)


async def send_text_message(result, favicon, favicon_b64):
    if favicon is not None:
        await check.finish(UniMessage([
            Text(result),
            Text('\nFavicon:'),
            Image(raw=base64.b64decode(favicon_b64.split(",")[1]))
        ]), at_sender=True)
    else:
        await check.finish(UniMessage(result), at_sender=True)


async def send_html_message(result):
    from nonebot_plugin_htmlrender import template_to_pic
    template_dir = os.path.join(os.path.dirname(__file__), "templates")

    pic = await template_to_pic(
        template_path=template_dir,
        template_name="default.html",
        templates={"data": result},
    )
    await check.finish(UniMessage(Image(raw=pic)), at_sender=True)


async def send_image_message(result, favicon, favicon_b64):
    if favicon is not None:
        await check.finish(UniMessage([
            Image(raw=(await ColoredTextImage(result).draw_text_with_style()).pic2bytes()
                  ),
            Text('Favicon:'),
            Image(raw=base64.b64decode(favicon_b64.split(",")[1]))
        ]), at_sender=True)
    else:
        await check.finish(UniMessage(Image(raw=(await ColoredTextImage(result).draw_text_with_style()).pic2bytes()
                                            )), at_sender=True)


async def handle_exception(e):
    error_type = type(e).__name__
    error_message = str(e)
    error_traceback = traceback.extract_tb(sys.exc_info()[2])[-2]

    result = f' ERROR:\nType: {error_type}\nMessage: {error_message}\nLine: {error_traceback.lineno}\nFile: {error_traceback.filename}\nFunction: {error_traceback.name}'
    logger.error(result)
    try:
        await check.finish(Text(result), at_sender=True)
    except FinishedException:
        pass


@lang_change.handle()
async def _(language: str):
    if language:
        await lang_change.finish(Text(await change_language_to(language)), at_sender=True)
    else:
        await lang_change.finish(Text(" Language?"), at_sender=True)


async def change_language_to(language: str):
    global lang
    try:
        a = lang_data[language]
    except:
        return f' No language named "{language}"!'
    else:
        if language == lang:
            return f' The language is already "{language}"!'
        else:
            lang = language
            return f' Change to "{language}" success!'


@lang_now.handle()
async def _():
    await lang_now.send(Text(f' Language: {lang}.'), at_sender=True)


@lang_list.handle()
async def _():
    i = '\n'.join(list(lang_data.keys()))
    await lang_list.send(Text(f" Language:\n{i}"), at_sender=True)
