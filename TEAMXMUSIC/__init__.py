from TEAMXMUSIC.core.bot import TEAMX
from TEAMXMUSIC.core.dir import dirr
from TEAMXMUSIC.core.git import git
from TEAMXMUSIC.core.userbot import Userbot
from TEAMXMUSIC.misc import dbb, heroku
from pyrogram import Client
from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = TEAMX()
api = SafoneAPI()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
