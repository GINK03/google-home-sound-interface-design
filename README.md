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
[![Vimeo](https://i.vimeocdn.com/video/677206429_100x75.jpg)](vimeo.com/250978500)
