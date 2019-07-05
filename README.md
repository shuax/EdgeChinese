# EdgeChinese
新版edge汉化工具

# 停止更新
新版edge已经加上了中文，并且质量越来越高，本项目已经没有必要继续更新。
——2019年7月5日

# 依赖
pak_tools.exe (pak_tools \[mac版] ) 可以解包打包pak文件，我写的

python3

# 原理
使用词典，翻译英文到中文。

# 成品
我会把汉化好的成品打包发布，另外集成了Edge++增强软件，在这里下载。这里仅提供Windows版,Mac版需要自行汉化

https://tools.shuax.com/edge/

# 使用

*特别注意，不同版本pak不通用！即使是同一个版本的64位和32位也不通用！所以每个版本都要重新生成*
*建议使用最新版的chromium中的语言文件(pak)文件*
*Mac和Windows的语言文件可能不通用*

## 解释
为了避免全部手工翻译，我最开始用了chrome金丝雀的资源来制作词典。 

##### Windows系统
1. 将chromium中的Locales下面的en-US.pak和zh-CN.pak复制到chrome目录下,覆盖已有文件
2. 进入chrome目录，使用unpack.bat解包en-us.pak，zh-CN.pak为en-US.json，zh-CN.json
    + 同时会运行dict.py并会生成en_cn_dict.json这个词典文件
3. 将Edge中Locales下面的en-US.pak放到项目根目录    
4. 运行build.bat得到zh-CN.pak
5. (可选) 可在manual.json中补全一些存在于not_translate.json中的未翻译的内容
6. (可选) 再次运行build.bat生成zh-CN.pak
7. 将生成的zh-CN.pak放回到Locales下面即可得到汉化版
    + 如果不行就把原始的en-us.pak删掉。

##### Mac系统

*此处测试是macOS X 10.14.4,由于安装了python2和python3,因此sh命令用python3来运行py文件,这点请注意*
*类似 /Contents/ 的路径省略了一段, 直接在Finder中打开左侧 应用程序 目录,在App上点击鼠标右键->显示包内容即进入到该目录前置目录*
1. 将chromium中 /Contents/Versions/版本号/XXXX.framework/Versions/A/Resources 下的en.lproj,zh_CN.lproj这两个文件夹复制到chrome目录下,覆盖已有文件
    + XXXX根据你使用的是chrome还是chromium,可能会不一样
2. 进入chrome目录,使用unpack.sh解包语言包,解包后的json文件在各自的文件夹下
    + 注意:需要设置sh文件的打开方式为终端(sh文件上右键->打开方式->其他->选择终端(要修改启用为 启用\:所有应用程序 )->确定)
    + 同时会运行dict.py并会生成en_cn_dict.json这个词典文件
3. 将Edge中 /Contents/Versions/版本号/Microsoft Edge Framework.framework/Versions/A/Resources 下的en.lproj文件夹复制到项目根目录
4. 双击build.sh得到zh_CN.lproj文件夹
5. (可选) 可在manual.json中补全一些存在于not_translate.json中的未翻译的内容
6. (可选) 再次运行build.sh生成zh_CN.lproj文件夹
7. 将生成的zh_CN.lproj文件夹放到 /Contents/Versions/版本号/Microsoft Edge Framework.framework/Versions/A/Resources 下
8. (若已经处理过,则无须此操作) 修改 mac版专用/zh_CN.lproj/InfoPlist.strings文件,修改方法见 mac版专用/说明.txt文件
9. (若已经处理过,则无须此操作) 将修改好的 mac版专用/zh_CN.lproj 文件夹放回到 /Contents/Resources

---

translate.py会根据词典en_cn_dict.json自动的把en-US.json翻译成zh-CN.json。

因为词典不会100%全，所以准备了一个手动词典manual.json，可以手动翻译不全的部分。

经过多次添加以后，词典就会越来越全。

未翻译部分会写入not_translate.json，方便查看翻译有多少缺失。

放入最新版edge的en-us.pak(en.lproj/locale.pak)，运行build.bat(build.sh)会执行三个动作。

1. 解包en-us.pak(en.lproj/locale.pak)为en-us.json(en.lproj/locale.json)
2. 调用translate.py把en-us.json(en.lproj/locale.json)汉化为zh-CN.json(zh_CN.lproj/locale.json)
3. 打包zh-CN.json(zh_CN.lproj/locale.json)成zh-CN.pak(zh_CN.lproj/locale.pak)
