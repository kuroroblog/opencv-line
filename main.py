import cv2
import sys

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread('./sample.jpg')

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img is None:
    sys.exit("Could not read the image.")

# line関数 : 画像内へ線分を描画する関数
# 第一引数(必須) : 多次元配列(numpy.ndarray)
# 第二引数(必須) : 線分の始点の座標。tuple型。
# 第三引数(必須) : 線分の終点の座標。tuple型。
# 第四引数(必須) : 線分の色を指定する。B(Blue)G(Green)R(Red)形式で指定する。tuple型。
# thickness : 線分の太さ(px)を指定する。int型(１以上の整数)。デフォルト(thicknessを指定しない場合)は1が設定される。
cv2.line(img, (200, 200), (150, 100), (255, 0, 0), thickness=4)

# imwrite : 画像の保存を行う関数
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
cv2.imwrite('output.jpg', img)
