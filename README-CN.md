# Astrospec

用来将[扫描成像光谱仪](https://en.wikipedia.org/wiki/Spectroheliograph)拍摄的原始素材，重建为图像。

优势：
- 基于亚像素插值的波长校正算法
- 附加功能，如颜色映射
- 通过算法拟合并去除杂散光

## 算法

[astrospec](https://github.com/liangchen-harold/astrospec)     - 核心算法库

astrospec-gui - 当前库，是对astrospec的简单封装，可以通过图形界面使用

## 参考
1. [SolEx](http://www.astrosurf.com/solex/sol-ex-presentation-en.html) - 法国友人Valerie Desnoux的开源光谱仪，提供了3D打印文件，另外还有非常详细的介绍，值得细读
2. [DIY迷你太阳光谱仪](https://www.bilibili.com/video/BV1um421j7co) by 阴天wnova酱 - up进行了包括小型化在内的改进，提供了3D打印件STL文件和所有物料表的淘宝链接
3. [Solex_ser_recon](https://github.com/Vdesnoux/Solex_ser_recon) - 法国友人Valerie Desnoux的开源重建软件
4. [SHG](https://github.com/thelondonsmiths/Solex_ser_recon_EN)
5. [又能看光谱又能拍摄太阳的太阳光谱仪](https://www.bilibili.com/video/BV1fw411W7HJ) by 摄日者天文
6. [太阳光谱扫描成像](https://lcsky.org/3.0/2024/05/19/spectroheliograph-1/) by 梁晨 - 拍摄注意事项

## License

本项目基于MIT许可证发布，详见[LICENSE](LICENSE)。

包含本项目代码的二进制发布，请保留指向本项目的链接、作者信息和License，并对最终用户可见。
