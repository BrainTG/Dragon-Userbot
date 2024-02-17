"""
  _______            __       _______ _______ 
|   _   .----.---.-|__.-----|       |   _   |
|.  1   |   _|  _  |  |     |.|   | |.  |___|
|.  _   |__| |___._|__|__|__`-|.  |-|.  |   |
|:  1    \                    |:  | |:  1   |
|::.. .  /                    |::.| |::.. . |
`-------'                     `---' `-------'

"""                                           

import ast

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix


def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


async def exec_code(code, env={}):
    try:
        fn_name = "_eval_expr"
        cmd = "\n".join(f" {i}" for i in code.splitlines())
        body = f"async def {fn_name}():\n{cmd}"
        parsed = ast.parse(body)
        body = parsed.body[0].body
        insert_returns(body)
        env = {'__import__': __import__, **env}
        exec(compile(parsed, filename="<ast>", mode="exec"), env)
        return await eval(f"{fn_name}()", env)
    except Exception as error:
        return error


@Client.on_message(filters.command(["e", "exec", "py", "eval"], prefix) & filters.me)
async def evaluator(client: Client, message: Message):
    code = message.text.split(maxsplit=1)[1]

    await message.edit("<b>Executing...</b>")

    result = await exec_code(
        code,
        {
            "message": message,
            "reply": message.reply_to_message,
            "client": client,
            "pyrogram": __import__("pyrogram"),
            "filters": filters
        }
    )
    text = (
        "<b>Code:</b>\n"
        f"<pre language=python>{code}</pre>\n"
        "<b>Result:</b>\n"
        f"<pre language=python>{result}</pre>"
    )
    await message.edit(text)

modules_help["eval"] = {
    "eval": "eval python code"
}
