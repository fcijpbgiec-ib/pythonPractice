# ライブラリの取り込み
import urllib.request

# URLと保存パスを指定
url = "http://uta.pw/shodou/img/28/214.png"
saveName = "test.png"

# ダウンロード
urllib.request.urlretrieve(url, saveName)
print("保存しました")