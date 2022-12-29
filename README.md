# jletteraddress.cls + VS Code devcontainer

[ueokande/jletteraddress](https://github.com/ueokande/jletteraddress) に [korosuke613/texlive-ja-devcontainer-template](https://github.com/korosuke613/texlive-ja-devcontainer-template) を加えて簡単に使えるようにしました。

## 使用方法

### 前提条件

- Docker がインストールされている
- VS Code に devcontainer 拡張機能がインストールされている

### 動作方法

以下のコマンドを実行して VS Code でこのリポジトリを開く

```sh
git clone https://github.com/pn11/jletteraddress.git
cd jletteraddress
code .
```

- 左下の><アイコンを押して、Reopen in container を実行する
- Docker Image がビルドされるので待つ
- ワークスペースが開いたら、terminalを開き、latexmk sample.texを実行する
- `example.pdf` が生成される

スタイルファイルの使い方は[README_org.md](README_org.md) または[フォーク元](https://github.com/ueokande/jletteraddress)を参照。
