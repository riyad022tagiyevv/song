import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6109967361:AAEXZWE1hSoeHeadEDCiEyZMMuIoF7BDH8w
")
    API_ID = int(os.environ.get("API_ID", "26712413"))
    API_HASH = os.environ.get("API_HASH", "3298034eb7cec614ef852fda02536153")
    BOT_OWNER = os.environ.get("BOT_OWNER", "RiyadAndMe ")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ModernSongBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "https://t.me/NewModernBlog")
    CHANNEL = os.environ.get("CHANNEL", "NewModernBlog")
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001852516406"))
