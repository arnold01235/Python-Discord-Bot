from discord.ext import commands
from discord.ext.commands import Context
import pyautogui
import time

class Template(commands.Cog, name="template"):
    def __init__(self, bot) -> None:
        self.bot = bot
        
        self.x = 0
        self.y = 0

        self.x2 = 0
        self.y2 = 0


    @commands.hybrid_command(
        name="skip",
        description="Moves the mouse to a specified position and clicks.",
    )
    async def move_and_click(self, context: Context) -> None:
        pyautogui.moveTo(self.x-5, self.y-40)
        time.sleep(0.5)
        pyautogui.moveTo(self.x, self.y)
        pyautogui.click()
        await context.send(f"Moved the mouse to ({self.x}, {self.y}) and clicked.")

    @commands.hybrid_command(
        name="skipintro",
        description="Moves the mouse to a specified position and clicks.",
    )
    async def skipintro(self, context: Context) -> None:
        pyautogui.moveTo(self.x2-5, self.y2-40)
        time.sleep(0.5)
        pyautogui.moveTo(self.x2, self.y2)
        pyautogui.click()
        await context.send(f"Moved the mouse to ({self.x}, {self.y}) and clicked.")


    @commands.hybrid_command(
        name="info",
        description="Posts the current position of the cursor.",
    )
    async def info(self, context: Context) -> None:
        x, y = pyautogui.position()
        await context.send(f"Current cursor position: ({x}, {y})")


async def setup(bot) -> None:
    await bot.add_cog(Template(bot))
