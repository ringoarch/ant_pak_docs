# 下载

从下面的地址下载Airpak的插件，目前支持Windows平台。
[下载地址](xxx.com)

然后解压缩代码到本地，得到`ant_pak`文件夹。

# 安装依赖

- Rhino 7.21及以上版本
- Airpak 3.0.16
- Paraview 5.10

# 安装Ant pak插件

- 解压缩后，将`ant_pak`文件夹放到本机`c:\Users\xxxx\AppData\Roaming\McNeel\Rhinoceros\7.0\scripts\`，其中`xxxx`为你的用户名。
- 将ant_pak文件夹中的`UserObjects`的所有`.ghuser`文件，全部拷贝到`c:\Users\xxxx\AppData\Roaming\Grasshopper\UserObjects\`，其中`xxxx`为你的用户名。
- 重新打开Rhino，打开Grasshopper，即可看到Airpak插件。

# 学习案例

## 案例1，卧室通风模型

- 使用模板，在Rhino中新建一个文件，然后打开`Template`文件夹中的`03 Airpak Model.gh`文件，可以参考案例文件进行建模。
- 模拟按照建模-转换为objects-设置-集成模型-模型设置-模拟-后处理流程来搭建电池组。

## 案例2，多房间通风模型

- 使用模板，在Rhino中新建一个文件，然后打开`Template`文件夹中的`04 Multi Domain.gh`文件，可以参考案例文件进行建模。
- 模拟按照建模-转换为objects-设置-集成模型-模型设置-模拟-后处理流程来搭建电池组。
