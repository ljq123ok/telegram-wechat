master_channel = 'plugins.eh_telegram_master', 'TelegramChannel'
slave_channels = [('plugins.eh_wechat_slave', 'WeChatChannel')]

eh_telegram_master = {
    "token": "6094168203:AAGmaLW1YWOBGb8ZiNg4cj1bF_5kR40hILU", # YOUR_TELEGRAM_BOT_TOKEN
    "admins": [1271109936],       # YOUR_TELEGRAM_ID
    "bing_speech_api": ["xxx", "xxx"],
    "baidu_speech_api": {
        "app_id": 0,
        "api_key": "xxx",
        "secret_key": "xxx"
    }
}
