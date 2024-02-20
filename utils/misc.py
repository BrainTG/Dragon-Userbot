"""
  _______            __       _______ _______ 
 |   _   .----.---.-|__.-----|       |   _   |
 |.  1   |   _|  _  |  |     |.|   | |.  |___|
 |.  _   |__| |___._|__|__|__`-|.  |-|.  |   |
 |:  1    \                    |:  | |:  1   |
 |::.. .  /                    |::.| |::.. . |
 `-------'                     `---' `-------'
                                              
"""
# Dragon-Userbot - telegram userbot
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

from sys import version_info
from .db import db
import git

__all__ = [
    "modules_help",
    "requirements_list",
    "python_version",
    "prefix",
    "gitrepo",
    "userbot_version",
]


modules_help = {}
requirements_list = []

python_version = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"

prefix = db.get("core.main", "prefix", ".")

logo = """
  _______            __       _______ _______ 
 |   _   .----.---.-|__.-----|       |   _   |
 |.  1   |   _|  _  |  |     |.|   | |.  |___|
 |.  _   |__| |___._|__|__|__`-|.  |-|.  |   |
 |:  1    \                    |:  | |:  1   |
 |::.. .  /                    |::.| |::.. . |
 `-------'                     `---' `-------'
                                              
"""

try:
    gitrepo = git.Repo(".")
except git.exc.InvalidGitRepositoryError:
    repo = git.Repo.init()
    origin = repo.create_remote(
        "origin", "https://github.com/BrainTG/Dragon-Userbot"
    )
    origin.fetch()
    repo.create_head("master", origin.refs.master)
    repo.heads.master.set_tracking_branch(origin.refs.master)
    repo.heads.master.checkout(True)
    gitrepo = git.Repo(".")

commit_count = len(list(gitrepo.iter_commits('HEAD')))
userbot_version = f"4.2.{commit_count}-BrainTG"