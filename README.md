# Qv2ray_transparent_proxy  
## 用途  
实现Qv2ray自动透明代理，驯服某些就是不用系统代理的程序。  
这只是一块py胶水，本质是自动调用tun2socks。  
## 安装步骤  
1. 安装QvPlugin-Command  
  https://github.com/Qv2ray/QvPlugin-Command/releases  
  插件安装方法详见Qv2ray指南  
2. 安装透明代理  
  - 安装py文件  
    首先安装python  
    然后在Qv2ray的plugins文件夹中创建一个名为QvTP的文件夹，向其中放入本仓库的QvTP.py  
    再去将另外3个外部程序放入这个文件夹：  
    - Wintun中的wintun.dll [下载地址](https://www.wintun.net/)  
    - tun2socks [下载地址](https://github.com/xjasonlyu/tun2socks/releases)  
    - gsudo [下载地址](https://github.com/gerardog/gsudo/releases)  
    
    在QvPlugin-Command插件设定的Post-Connection一栏中填入`.\plugins\QvTP\gsudo python .\plugins\QvTP\QvTP.py`  
  - 安装打包  
    同样在Qv2ray的plugins文件夹中创建一个名为QvTP的文件夹  
    下载本仓库release中的压缩包，将其中的一大堆文件解压到这个QvTP文件夹中。Wintun、tun2socks、gsudo已包含在打包中  
    在QvPlugin-Command插件设定的Post-Connection一栏中填入`.\plugins\QvTP\gsudo .\plugins\QvTP\QvTP`  
3. Enjoy!  
  此透明代理会自动开关：当你在首选项-入站设置中勾选“设置系统代理”，透明代理不会生效；取消勾选“设置系统代理”，即可打开透明代理。  
  注意：某些时候，在连接后一小段时间会涌入大量的请求，导致Qv2ray界面卡死，这时只需耐心等待，静待花开（误）  
## 可能更好的选择
试试v2rayA？  
