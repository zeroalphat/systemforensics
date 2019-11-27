# 監査ログから攻撃者の行動を分析してみよう

## 仮想マシンの用意

- Host 環境に VMware, VirtualBox のインストールをしてください[VMware のインストール方法](https://qiita.com/qiita_mona/items/066d8f662409dd84c0d3).
- 仮想環境に攻撃用の Kali Linux, やられ役の Windows10 のインストールをしてください.(Windows は評価版で大丈夫です．)
- Windows10 と Kali Linux 間で ping ができるようにお願いします[内部ネットワークの構築の仕方](https://turningp.jp/virtualization/virtual_box/virtual-box-internal-networking)

## Kali Linux にインストールするソフトウェア

- [Powershell Empire](https://github.com/EmpireProject/Empire)
- [Docker](https://docs.docker.com/install/linux/docker-ce/debian/)
- [MailHog](https://github.com/mailhog/MailHog)

### 参考になりそうな URL

- [GitHub からプログラムをダウンロード・インストール](http://rnakato.hatenablog.jp/entry/2018/08/04/151041)
- [Docker 初めての人向け説明メモ](https://qiita.com/miyasakura_/items/87ccb6d4a52d4a00a999)
- [Docker でよく使うコマンドまとめ](https://morizyun.github.io/docker/about-docker-command.html)
- [MailHog を利用してメール送信テスト環境を docker コンテナ上に作る](https://qiita.com/kobatei/items/1b8b0ca5e8737235dccd)

## Windows にインストールするソフトウェア

- [sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon) インストール
- Office のインストール(各大学で Office のインストーラの貸し出しが行われていると思います．)
- Windows Update は行わないでください.

## できれば読んできてほしい

- [Backtracking Intrusions](https://www2.cs.duke.edu/courses/cps210/spring06/papers/p190-king.pdf)
