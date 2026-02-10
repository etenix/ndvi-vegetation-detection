# NDVI Vegetation Detection

Pythonによる衛星画像を用いた植生抽出システム

---

## 概要

本プロジェクトは、衛星画像データを活用し、NDVI（正規化植生指数）を算出することで、
植生エリアを抽出・可視化するPythonプロジェクトです。

リモートセンシング分野で培った知識と、プログラミング技術を組み合わせ、
研究用途だけでなく実務での活用も意識して開発しました。

---

## 使用技術

- Python  
- NumPy  
- Rasterio  
- Matplotlib  

---

## NDVIについて

NDVI（Normalized Difference Vegetation Index）は、
植生の活性度を評価するための代表的な指標です。

計算式：NDVI = (NIR - RED) / (NIR + RED)

- NIR：近赤外バンド  
- RED：赤色バンド  

---

## 主な機能

- 衛星画像データの読み込み
- NDVIの算出
- Min-Max正規化処理
- 植生分布の可視化
- 結果の出力

---

## ディレクトリ構成

- ndvi-vegetation-detection/
- ├ data/        # 衛星画像データ
- ├ src/         # ソースコード
- ├ output/      # 出力結果
- ├ requirements.txt
- └ README.md

---

## 実行方法

### 1. 環境構築

```bash
pip install -r requirements.txt
```

### 2. NDVI計算

```bash
python src/ndvi.py
```

### 3. 可視化

```bash
python src/visualize.py
```

## 正規化処理について

- 本プロジェクトでは、Min-Max正規化を用いてNDVI値を0〜1の範囲にスケーリングしています。
```bash
normalized = (x - min) / (max - min)
```

## 開発の目的
- 衛星データ解析スキルの向上
- Pythonによる画像処理の習得
- 実務レベルのコード設計の習得
- クラウド・AI分野への応用を見据えた基盤構築

## 今後の改善予定
- AWS上でのデータ処理対応
- 深層学習モデルとの連携
- 時系列NDVI解析機能の追加
- Webアプリケーション化

## 作成者
- etenix
