# Flash Mental Math (flash_math_class_v1.3)

**簡単な説明**

`flash_math_class_v1.3.py` はフラッシュ暗算（画面に短時間だけ表示される数字を覚えて合計を答える）アプリです。デフォルトで GUI を起動し、オプション `--console` を付けるとコンソール版が起動します。

---

## 主な機能

* GUI（Tkinter）で数字を順に短時間表示
* クラス（級／段）ごとの表示設定を辞書で管理（`class_settings`）
* デフォルトで GUI 起動。コマンドライン引数 `--console` でコンソールモードを実行
* PyInstaller で exe 化しても GUI を起動（`--console` 相当の動作はコマンドライン引数で明示）
* カスタムフォント（例：`ABACUS2.ttf`）を読み込もうとする（無ければ代替フォント）

---

## 必要環境

* Python 3.8 以上（3.13 でも動作確認）
* Tkinter（標準ライブラリに含まれるが、ディストリビューションによっては別途インストールや有効化が必要）

Windows では通常 Python を公式インストーラで入れれば Tkinter が含まれます。Linux の一部ディストリビューションでは `python3-tk` 等のパッケージを追加で入れる必要があります。

---

## ファイル構成（例）

```
flash_math/
├─ flash_math_class_v1.3.py
├─ ABACUS2.ttf   # 任意（フォントを使いたい場合）
└─ README.md
```

---

## インストール（仮想環境推奨）

1. 仮想環境を作成・有効化（Windows の例）:

```powershell
python -m venv venv
venv\Scripts\activate
```

2. 依存は標準ライブラリ中心なので追加インストールは基本不要。

---

## 使い方

### GUI（デフォルト）

カレントディレクトリに `flash_math_class_v1.3.py` がある状態で:

```bash
python flash_math_class_v1.3.py
```

または（Windows でコンソールを表示させたくない場合）:

```powershell
venv\Scripts\pythonw.exe flash_math_class_v1.3.py
```

### コンソール版（開発・デバッグ用）

```bash
python flash_math_class_v1.3.py --console
```

### 実行時オプション（現状）

* `--console` : コンソール版を起動（引数が無ければ GUI）

---

## カスタムフォントについて

スクリプトは `ABACUS2.ttf` のようなフォントを読み込もうとします。フォントファイルを同じフォルダに置くと優先的に使われます。無ければ自動で標準フォント（Arial 等）にフォールバックします。

---

## PyInstaller で exe 化する（Windows の例）

GUI アプリとして exe を作るなら `--noconsole` を付けると実行時にコンソールが出ません。

```powershell
pyinstaller --onefile --noconsole --add-data "ABACUS2.ttf;." flash_math_class_v1.3.py
```

注意: `--add-data` の書式はプラットフォームで異なります（上は Windows の例）。

---

## トラブルシューティング

* **GUI が起動しない・ImportError: No module named 'tkinter'**

  * Python に Tk が含まれていない可能性があります。Windows なら公式インストーラで再インストール、Linux なら `sudo apt install python3-tk`（Debian/Ubuntu 系）などを試してください。

* **フォント読み込みエラー**

  * `ABACUS2.ttf` が無い場合はエラーメッセージが出て、代替フォントで動作します。フォントを使いたい場合は同じフォルダに配置してください。

* **ヘッドレス環境（WSL や サーバ）で起動できない**

  * GUI を表示するディスプレイが無い環境では X サーバやディスプレイ転送の設定が必要です。代わりに `--console` を使ってコンソール版を実行してください。

---

## 主要コードのポイント

* 最後の `if __name__ == "__main__":` ブロックで実行モードを決定しています。

  * デフォルト: GUI 起動
  * `--console` を渡すとコンソール版起動
  * PyInstaller 等で `sys.frozen` が真なら GUI を起動

* クラスごとの設定は `class_settings` 辞書で管理。ここを編集すれば表示時間／桁数／問題数などを調整できます。

---

## 変更履歴（Changelog）

* **v1.3**

  * デフォルトで GUI を起動するように変更。
  * `--console` オプションで従来のコンソール版を起動可能に。
  * PyInstaller での exe 化を想定した挙動を維持。

* **v1.2**

  * (旧) デフォルトはコンソール版、`gui` 引数で GUI を起動する実装。

---

## ライセンス

このプロジェクトのライセンスをここに記載してください（例: MIT ライセンス）。

---

## 連絡・貢献

バグ報告や改善提案は Issue/PR でお送りください。ローカルでの小さな修正は歓迎します。

---

以上です。README の内容を加筆・修正したい箇所があれば教えてください。
