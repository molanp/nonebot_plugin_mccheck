<div align="center">
<a href="https://v2.nonebot.dev/store"><img src="https://github.com/KomoriDev/nonebot-plugin-kawaii-status/raw/master/docs/NoneBotPlugin.svg" alt="NoneBotPluginLogo"></a>
</div>

<div align="center">

# nonebot-plugin-mccheck

_✨ Minecraft Server Query Plug-in_

<a href="./LICENSE">
<img src="https://img.shields.io/github/license/molanp/nonebot_plugin_mccheck.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-mccheck">
<img src="https://img.shields.io/pypi/v/nonebot-plugin-mccheck.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">
<img src="https://img.shields.io/pypi/dm/nonebot-plugin-mccheck" alt="pypi-download-count">
</div>

English|[简体中文](README.md)

## 📖 Introduction

Minecraft server status query, supporting IPv6.

> update synchronously with [https://github.com/molanp/zhenxun_check_minecraft/](https://github.com/molanp/zhenxun_check_minecraft).

## 💿 Installation

One of the methods mentioned below can be selected.

<details open>
<summary>[recommended] install using nb-cli</summary>
Open the command line in the root directory of Bot and enter the following instructions to install.

```shell
nb plugin install nonebot-plugin-mccheck
```

</details>

<details>
<summary> install using package manager </summary>
In the plug-in directory of the nonebot2 project, open the command line and enter the corresponding installation command according to the package manager you use.

```shell
pip install nonebot-plugin-mccheck
# or
pdm add nonebot-plugin-mccheck
# or
poetry add nonebot-plugin-mccheck
# or
conda install nonebot-plugin-mccheck
```

Open the `pyproject.toml` file in the root directory of the nonebot2 project, and write in the ` [tool.nonebot] ` section.
```toml
plugins = ["nonebot_plugin_mccheck"]
```
</details>

## 📈 Implemented functions

- [x] Adapted unicode full fonts and glyphs
- [x] Render Motd styles
- [x] Query server nickname
- [x] Query the maximum number of servers, the current number of people
- [x] Query server motd
- [x] returns the server address and port
- [x] Returns the server online status
- [x] Query server latency
- [x] More precise delay
- [x] UDP server is supported
- [x] Error message feedback
- [x] Port autocompletion
- [x] Wisdom~~Barrier~~ can determine whether the IP address is correct
- [x] Get the JSON version of the server motd (only if the server motd is set to JSON format)
- [x] Does not depend on any external API :)
- [x] Support special port queries (e.g. `2`, `80`, `443` etc.)
- [x] Query server favicon
- [x] Multilingual
- [x] SRV support 

## 📑 Future functions

- [ ] Get server protocol number
- [ ] Get server official website (if any)
- [ ] And more...

## 🖼️ Test screenshot

Picture Message
![pic](https://github.com/user-attachments/assets/abcda34f-0783-4c1e-b5c1-de9228047a69)

HTML Message
![html](https://github.com/user-attachments/assets/18069f2a-4f7e-4994-837b-2b9e0cbf1f74)

## ⚙️ Configuration

Add the required configuration in the following table to the `.env` file of the nonebot2 project.

| Configuration Item | Required | Default Value | Description |
|:-----:|:----:|:----:|:----:|
| `MCC__LANGUAGE` | False | `zh-cn` | Languages used by the plugin to render images<br>Available languages: [`zh-cn`,`zh-tw`,`en`] |
| `MCC__TYPE` | False | `0` | The type of message the plugin sends (`0` for HTML, `1` for image, `2` for text) |


## 🎉 Usage
| Command | Parameter | Scope | Description |
|:-------:|:---------:|:-----:|:-----------:|
| `mcheck` | `[ip]:[port]` or `[ip]` | Private/Group Chat | Check Minecraft server status |
| `set_lang` | Language name | Private/Group Chat | Set the language used by the plugin for rendering images |
| `lang_now` | None | Private/Group Chat | View the current language used by the plugin for rendering images |
| `lang_list` | None | Private/Group Chat | View the list of languages supported by the plugin |
