# Google Homeで音声で操作、音声で通知の双方向インターフェースを定義します

## 音声による通知の概要
### google-home-notifierを使う方法

Google Homeで話させる方法はいくつかありますが、有名なのが[google-home-notifiler](https://github.com/noelportugal/google-home-notifier)になるかと思います。

#### Nodejsのinstall
Ubuntu, Debianの利用を想定しています  
```console
$ wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash
$ source .bashrc
$ nvm install node
...
$ node --version
v9.4.0
```

#### google-home-notifierの日本語設定と、パッケージのインストール
```console
$ sudo apt install git-core libnss-mdns libavahi-compat-libdnssd-dev
$ git clone https://github.com/noelportugal/google-home-notifier
$ cd google-home-notifier
$ npm install
...(dns解決系の依存のバイナリのコンパイルが行われる様です)

$ vim example.js # 後述のコードの箇所を変更します
...
```

デフォルトでは日本語が喋ることができませんので、この[google-home-notiferの作者様の、example](https://github.com/noelportugal/google-home-notifier)のコードをこの様に編集する必要があります。  

```python
  8   var deviceName = '部屋1'; // Google Homeのセットアップに使用した名前を設定します
  9   var ip = '192.168.14.87'; // Google HomeのIPアドレスを入れる様です。Google Homeをセットアップしたアプリで確認できます
...
 24   var language = 'ja'; //  defaultのplをjaに変更
 25   if (req.query.language) {
 26     language;
 27   }
 28
 29   googlehome.ip(ip, language);
 30   googlehome.device(deviceName,language); //　この行を追加しないと、日本語を入力しても何も発話してくれない！！
 31   if (text){
```

#### 実行の確認
実際に話させてみます  
nodejsでexample.jsを起動します  
```console
$ node example.js
```
ローカルホストにクエリを送ります  
(必要ならば、IPアドレスをnodeを起動したサーバに記します)
```console
$ curl -X GET localhost:8091/google-home-notifier?text=Hello+Google+Home
```
[![Vimeo](https://i.vimeocdn.com/video/677206429_100x75.jpg)](https://vimeo.com/250978500)

#### 任意の言葉をpythonのrequestsモジュールで話させる  
GETメソッドでデータを送る以外にも、POSTでデータを送信して話させることができます  
```python
requests.post("http://192.168.14.31:8091/google-home-notifier", data={'text': "ここに何か話させるテキストを入れる"})
```

#### 例1:銀行の預金残高を定期的に話させる
Visa Bebitカードというものがありまして、その場ですぐ引き落とさせるので便利なので、ネットでの買い物や食事などに利用しているのですが、おこずかい用に口座を利用しているので、あまり大金を入れていないので枯渇しがちです。  

数回アナウンスシステムを組みました  

Seleniumで自動で銀行にログインして、口座の金額を取得して話させます  
[![Vimeo](https://i.vimeocdn.com/video/677209382_100x75.jpg)](https://vimeo.com/250980847)

金銭感覚があまりしっかりしていないので、便利です  

#### 例2:AWSの予想値を話させる  
AWSの料金は、クラウドという性質上、会社などの組織で使うにはある程度の大きな予算枠を最初に設定し、そこから消化して使っていくスタイルです　　
誰もが経験があるかと思いますが、AWSやGCPを使いすぎて怒れられるということがあったかと思います。。。  

メールによるアラートにとてもじゃないけど全部気づけないので、話させることができます  

AWSだとリソース監視にCloud Watchが使えるのでbotoなどの便利なモジュールで参照ができ、その結果を夕方に話させて、予算感の把握できます  

[![Vimeo](https://i.vimeocdn.com/video/677210785_100x75.jpg)](https://vimeo.com/250981887)

## 音声によるグーグルホームから操作する
OutputができればInputをできるはずです。  

この二つが揃うと、コンピュータのインターフェースが全て揃うのでなんでもできます  

いろいろやり方がありますが、IFTTTと連携させ、IFTTTからweb hookを利用することで、任意のAWS LambdaやGCPのCloud Functionやオンプレのサーバにつなぐことができます  
