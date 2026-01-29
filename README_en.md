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

> update synchronously with [https://github.com/molanp/zhenxun_plugin_mccheck/](https://github.com/molanp/zhenxun_plugin_mccheck).

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
In the plug-in directory of the nonebot2 project, open the command line and enter the installation command.

```shell
pip install nonebot-plugin-mccheck
```

Open the `pyproject.toml` file in the root directory of the nonebot2 project, and write in the `[tool.nonebot]` section.

```toml
plugins = ["nonebot_plugin_mccheck"]
```

</details>

## 📈 Implemented functions

- [x] IPv6 support
- [x] Support for all platform adapters
- [x] Support for all Unicode fonts and glyphs
- [x] Motd-style rendering
- [x] Support for double queries to interconnected servers
- [x] Multilingual
- [x] SRV support

## 📑 Future functions

- [ ] And more...

## 🖼️ Test screenshot

v0.1.45
![Image_31020983743694.png](https://github.com/user-attachments/assets/2db47c9a-7ba1-4ce7-a31c-b65f6e848308)
![image](https://github.com/user-attachments/assets/d0830fe9-c690-4017-b601-f46a1d7e1894)

### 🎈 Special Notes

Querying an IPv6 server

```
mcheck [2001:db8:85a3::8a2e:370:7334]:25565  <- IPv6 server address and port, the port and colon can be omitted
```

or

```
mcheck [2001:db8:85a3::8a2e:370:7334]  <- IPv6 server address
```

## ⚙️ Configuration

Add the required configuration in the following table to the `.env` file of the nonebot2 project.

| Configuration Item | Required | Default Value |                                         Description                                          |
| :----------------: | :------: | :-----------: | :------------------------------------------------------------------------------------------: |
|  `MCC__LANGUAGE`   |  False   |    `zh-cn`    | Languages used by the plugin to render images<br>Available languages: [`zh-cn`,`zh-tw`,`en`] |
|    `MCC__TYPE`     |  False   |      `0`      |              The type of message the plugin sends (`0` for HTML, `1` for text)               |

## 🎲 Comparison of message types

| Type | Special Styles | Favicon | Fully colored underline/strikethrough | Full Unicode font support |
| :--: | :------------: | :-----: | :-----------------------------------: | :-----------------------: |
| Text |       ❌       |   ⭕    |                  ❌                   |            ⭕             |
| HTML |       ⭕       |   ⭕    |                  ⭕                   |            ⭕             |

## 🎉 Usage

|   Command   |        Parameter        |       Scope        |                            Description                            |
| :---------: | :---------------------: | :----------------: | :---------------------------------------------------------------: |
|  `mcheck`   | `[ip]:[port]` or `[ip]` | Private/Group Chat |                   Check Minecraft server status                   |
| `set_lang`  |      Language name      | Private/Group Chat |     Set the language used by the plugin for rendering images      |
| `lang_now`  |          None           | Private/Group Chat | View the current language used by the plugin for rendering images |
| `lang_list` |          None           | Private/Group Chat |        View the list of languages supported by the plugin         |
