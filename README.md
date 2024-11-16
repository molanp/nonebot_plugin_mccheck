<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/KomoriDev/nonebot-plugin-kawaii-status/raw/master/docs/NoneBotPlugin.svg" alt="NoneBotPluginLogo"></a>
</div>

<div align="center">

# nonebot-plugin-mccheck


_✨ Minecraft 服务器查询插件 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/molanp/nonebot_plugin_mccheck.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-mccheck">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-mccheck.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">
<img src="https://img.shields.io/pypi/dm/nonebot-plugin-mccheck" alt="pypi-download-count">
</div>

简体中文|[English](README_en.md)

## 📖 介绍

Minecraft服务器状态查询，支持IPv6

> 与[https://github.com/molanp/zhenxun_check_Minecraft/](https://github.com/molanp/zhenxun_check_Minecraft)同步更新

## 💿 安装

以下提到的方法任选 **其一** 即可

<details open>
<summary>[推荐]使用 nb-cli 安装</summary>
在 Bot 的根目录下打开命令行, 输入以下指令即可安装

```shell
nb plugin install nonebot-plugin-mccheck
```

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

```shell
pip install nonebot-plugin-mccheck
# or
pdm add nonebot-plugin-mccheck
# or
poetry add nonebot-plugin-mccheck
# or
conda install nonebot-plugin-mccheck
```

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入
```toml
    plugin["nonebot_plugin_mccheck"]
```
</details>

## 📈 已实现的功能

- [x] 支持全平台适配器
- [x] 适配Unicode全字体与字形
- [x] 渲染Motd样式
- [x] 查询服务器昵称
- [x] 查询服务器最大人数,当前人数
- [x] 查询服务器motd
- [x] 返回服务器地址及端口
- [x] 返回服务器在线状态
- [x] 查询服务器延迟
- [x] 更精确的延迟
- [x] 支持UDP服务器
- [x] 错误信息反馈
- [x] 端口自动补全
- [x] 智~~障~~能判断IP地址是否正确
- [x] 获取服务器motd的json版本(仅当服务器motd设置为json格式时)
- [x] 不依赖任何外部api
- [x] 支持特殊端口查询(如`2`,`80`,`443`等)
- [x] 查询服务器favicon
- [x] 多语言
- [x] SRV支持
- [x] 完全彩色下划线/删除线

## 📑 未来的功能

- [ ] 获取服务器协议号
- [ ] 获取服务器官网[如果存在]
- [ ] 敬请期待

## 🖼️ 效果图

v0.1.22

文本消息
![0.1.22 text](https://github.com/user-attachments/assets/7099ded9-9c8c-482f-89e5-a68bd014e67a)

图片消息
![0.1.22 pic](https://github.com/user-attachments/assets/3ba422a4-bc41-4401-85c7-f5da2f693b03)

HTML消息
![0.1.22 html](https://github.com/user-attachments/assets/09396694-16a4-4907-8b25-3863b181a725)

互通服(不止支持HTML消息，此处仅展示一种)
![0.1.22 geyser](https://github.com/user-attachments/assets/3982c18a-7cc5-4eb2-9f0f-9ec2a16fed2f)


## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| `MCC__LANGUAGE` | 否 | `zh-cn` | 插件渲染图片所使用的语言<br>可用语言:[`zh-cn`,`zh-tw`,`en`] |
| `MCC__TYPE` | 否 | `0` | 插件发送的消息类型(`0`为HTML渲染图片, `1`为图片, `2`为文本) |

## 🎲 消息类型对比

| 类型 | 特殊样式 | Favicon | 完全彩色下划线/删除线 | 全Unicode字体支持 |
|:-----:|:-----:|:-----:|:-----:|:-----:|
| 文本 | ❌ | ⭕ | ❌ | ⭕ |
| 图片 | ⭕ | ⭕ | ⭕ | ❌ |
| HTML | ⭕ | ⭕ | ⭕ | ⭕ |

## 🎉 使用

|命令|参数|范围|说明|
|:---:|:---:|:---:|:---:|
|`查服/mcheck`|`[ip]:[端口]` 或 `[ip]`|私聊/群聊|查询服务器状态|
|`设置语言/set_lang`|语言名称|私聊/群聊|设置插件渲染图片所使用的语言|
|`当前语言/lang_now`|无|私聊/群聊|查看当前插件渲染图片所使用的语言|
|`语言列表/lang_list`|无|私聊/群聊|查看插件支持的语言列表|

