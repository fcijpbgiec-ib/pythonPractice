# ライブラリの取り込み
import urllib.request

# URLと保存パスを指定
url = "http://uta.pw/shodou/img/28/214.png"
saveName = "test.png"

# ダウンロード
mem = urllib.request.urlopen(url).read()

# ファイルへ保存
with open(saveName, mode="wb") as f:
    f.write(mem)
    print("保存しました")