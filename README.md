# このリポジトリについて
このリポジトリは、日本語のテキストや文章を入力し、それらをもとにbotとしての文章を生成するためのリポジトリになります。webサービスとして公開しているわけではなく、OSSとして提供しているものになります。

# 使い方
1. controller.pyを実行し、ローカルホストを立ち上げる

1. ローカルホストへ接続し、webページを表示する

1. テキストエリアへ生成に必要な文章を、ある程度入力する

1. 『生成』ボタンを押して、生成を開始する（テンプレートとして用意している「吾輩は猫である」の作品文章では、文章を生成するのにかなりの時間を要します）

1. 生成された文章が5つ分、webページに表示されるので、あとはお好きに活用してください。

# その使い方
- 『テキスト削除』ボタンを押すと、テキストエリアに入力した文章が削除されます。

# 環境構築
1. Python 3.10.6をインストールする

1. このリポジトリをクローンする

1. ライブラリをインストールする（Bottle,tqdm,Janome）
```
pip install bottle
```
```
pip install tqdm
```
```
pip install janome
```

# 注意事項
- 入力に使用する文章は、利用者の判断のもと、著作権上問題のない文章が入力されることを想定しています。入力される文章は、利用者の判断の下で入力して下さい。
- 生成された文章は、必ずしも正しい日本語や世間一般的な文章になるとは限りません。
- 生成された文章を利用したことによる、生じた被害等に関し、一切、開発者は関与いたしません。

# 動画
アプリケーションの使用状況は、以下の動画から閲覧することができます。<br>
https://youtu.be/bHdPxVX9rSc?feature=shared