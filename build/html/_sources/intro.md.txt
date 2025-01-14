# Airpak支持的Objects

Airpak是基于`object`的建模方式，这些`object`包括:

- 房间 `Domain`
- 人体 `persons`
- 块 `blocks`
- 风扇 `fans`
- 通风孔 `openings`
- 墙壁 `walls`
- 隔板 `partitions`
- 热负荷源 `source`
- 阻尼板（块） `resistances`
- 排烟罩 `hoods`
- 热交换器 `exchanges`

另外，Airpak还提供了各式各样的`diffuser`模型，以及用于计算大气边界层的模型。  

# 支持的几何形状

Airpak提供了与CAD软件的接口，可以通过`IGES`和`DXF`格式导入`CAD`软件的几何。但导入后，还需要重新描图重新转换为模型，因此建模速度相当受限。 常规建模方式可参考：[airpak精讲课2-建模](https://www.bilibili.com/video/BV1L8411s7Rq/?vd_source=6c183c6a7ab72d7497f506752c5e8071)  
Airpak一般支持的简单的几何形状建模，同时也支持复杂网格建模，但其默认的网格划分工具不支持，大部分时候都是不可以用的。因此，对于异性体建模，可以通过简化成多个上述支持的简单几何形状来表示。

# 建模原理

Airpak的模型文件是保存在一个项目文件夹里面的，包括如下文件：

- `model`——模型文件
- `problem`——项目设置文件
- `post_objects`——后处理文件

上述文件均是文本文件，可以通过编辑文本的方式建立模型，因此，只要将模型几何图形和软件设置翻译为文本格式，就可以通过例如`Rhino`、`AutoCAD`等第三方建模工具进行建模。本插件为基于Rhino的实现方法。

# Why Rhino

Rhino本身建模相对比较简单强大，可以快速进行几何建模工作，此外，利用Grasshopper插件进行Airpak建模，还有如下优势：

- 参数化建模，对于有规律布置的组件，可以通过参数化快速进行建模，在优化过程中，通过调节参数，可以实现快速批量化建模；
- 批量化参数设置，对多个组件可以进行批量化设置风速、温度、热量、污染物扩散率等参数设置；
- 通过简单设置，可以快速进行后处理切片设置；
- 快速对常规的模拟设置进行修改；
- 可视化编程，自定义功能强大。

# 插件功能特性

- 支持简单几何体建模，不支持复杂网格建模。具体包括如下几何体：
  - 三维几何体
    - 正六面体`prism`
    - 圆柱体   `cylinder`
    - 球体 `sphere`
    - 多边体 `polyhedron`
  - 二维集合体
    - 矩形`rectangle`
    - 圆形 `circular`
    - 多边形 `polygon`
    - 倾斜面 `inclined`
- 支持模型在Rhino界面的可视化。
- 支持下述Object建模：
  - 房间 `Domain`
  - 人体 `persons`
  - 块 `blocks`
  - 风扇 `fans`
  - 通风孔 `openings`
  - 墙壁 `walls`
  - 隔板 `partitions`
  - 热负荷源 `source`
  - 阻尼板（块） `resistances`
- 支持下述Object属性设置：
  - 温度`temperature`
  - 压力`pressure`
  - 污染物`species`
  - 发热量`total heat`
  - 人员MET `met`
  - 阻力 `loss coefficient`
- 支持后处理设置，包括：
  - 物体面 `object face`
  - 切面 `cut`
  - ISO面 `iso`
  - 监测点 `point`
- 模拟设置，包括：
  - 湍流模型设置  `turbulent model`
  - 污染物设置 `species`
  - 模拟步长 `steps`
  - 后处理设置 `post`
  - 初始温度设置 `ambient temperature`