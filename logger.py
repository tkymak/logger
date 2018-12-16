import logging

# ロガー作成
logger = logging.getLogger('sample')
logger.setLevel(logging.DEBUG)

# コンソールハンドラー作成
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# フォーマット作成
formatter = logging.Formatter('mylog - %(asctime)s - %(name)s - %(levelname)s - %(message)s')

# フォーマットをchに追加
ch.setFormatter(formatter)

# ヘッダーに追加
logger.addHandler(ch)

# ログ出力
logger.debug('debug message')

