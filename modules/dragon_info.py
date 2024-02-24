"""
  _______            __       _______ _______ 
 |   _   .----.---.-|__.-----|       |   _   |
 |.  1   |   _|  _  |  |     |.|   | |.  |___|
 |.  _   |__| |___._|__|__|__`-|.  |-|.  |   |
 |:  1    \                    |:  | |:  1   |
 |::.. .  /                    |::.| |::.. . |
 `-------'                     `---' `-------'
                                              
"""

#  Dragon-Userbot - telegram userbot
#  Copyright (C) 2020-present Dragon Userbot Organization
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
from pyrogram import Client, filters
from pyrogram.types import Message
import random
import datetime

from utils.misc import (
    modules_help,
    prefix,
    userbot_version,
    python_version,
    gitrepo,
)


@Client.on_message(
    filters.command(["support", "repo", "info"], prefix) & filters.me
)
async def info(_, message: Message):
    devs = ["@john_ph0nk", "@fuccsoc2", "@BTG_UB(BrainTG)"]
    random.shuffle(devs)

    commands_count = float(
        len([cmd for module in modules_help for cmd in module])
    )

    await message.edit(
        f"<b>BrainTG/Dragon-Userbot\n\n"
        "GitHub: <a href=https://github.com/BrainTG/Dragon-Userbot>BrainTG/Dragon-Userbot</a>\n"
        "Custom modules repository: <a href=https://github.com/Dragon-Userbot/custom_modules>"
        "Dragon-Userbot/custom_modules</a>\n"
        "License: <a href=https://github.com/Dragon-Userbot/Dragon-Userbot/blob/master/LICENSE>GNU GPL v3</a>\n\n"
        "Channel: @BTG_UB\n"
        "Custom modules: @Dragon_Userb0t_modules\n"
        "Chat [RU]: @Dragon_Userb0t_chat\n"
        f"Main developers: {', '.join(devs)}\n\n"
        f"Python version: {python_version}\n"
        f"Modules count: {len(modules_help) / 1}\n"
        f"Commands count: {commands_count}</b>",
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command(["version", "ver"], prefix) & filters.me)
async def version(client: Client, message: Message):
    changelog = ""
    ub_version = ".".join(userbot_version.split(".")[:2])
    async for m in client.search_messages("BTG_UB", query=ub_version + "."):
        if ub_version in m.text:
            changelog = m.id

    await message.delete()

    remote_url = list(gitrepo.remote().urls)[0]
    commit_time = (
        datetime.datetime.fromtimestamp(gitrepo.head.commit.committed_date)
        .astimezone(datetime.timezone.utc)
        .strftime("%Y-%m-%d %H:%M:%S %Z")
    )

    await message.reply(
        f"<b>BrainTG Dragon-Userbot version: {userbot_version}\n"
        f"Changelog </b><i><a href=https://t.me/BTG_UB/{changelog}>in channel</a></i>.<b>\n"
        + (
            f"<b>Branch: <a href={remote_url}/tree/{gitrepo.active_branch}>{gitrepo.active_branch}</a>\n"
            if gitrepo.active_branch != "master"
            else ""
        )
        + f"Commit: <a href={remote_url}/commit/{gitrepo.head.commit.hexsha}>"
        f"{gitrepo.head.commit.hexsha[:7]}</a> by {gitrepo.head.commit.author.name}\n"
        f"Commit time: {commit_time}</b>",
    )


modules_help["dragon_info"] = {
    "info": "Information about userbot",
    "version": "Check userbot version",
}
