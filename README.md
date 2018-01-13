# Google Homeで音声で操作、音声で通知の双方向インターフェースを定義します

## 音声による通知の概要
### google-home-notifierを使う方法

Google Homeで話させる方法はいくつかありますが、有名なのが[google-home-notifiler](https://github.com/noelportugal/google-home-notifier)になるかと思います。
デフォルトでは日本語が喋ることができませんので、このgoogle-home-notiferの作者様の、exampleのコードをこの様に編集する必要があります。  

```python
 24   var language = 'ja'; //  defaultのplをjaに変更
 25   if (req.query.language) {
 26     language;
 27   }
 28
 29   googlehome.ip(ip, language);
 30   googlehome.device(deviceName,language); //　この行を追加しないと、日本語を入力しても何も発話してくれない！！
 31   if (text){
```
