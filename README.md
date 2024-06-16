# Astrospec

[[English](README.md)] [[中文](README-CN.md)]

This project is used to reconstruct image from raw video captured by the [spectroheliograph](https://en.wikipedia.org/wiki/Spectroheliograph)

**Highlights**
- Algorithm with sub-pixel interpolation for wavelength correction 
- Additional features such as color mapping
- Advanced algorithm to remove stray light ([view comparison](#Stray-light-remove))


## Algorithm

[astrospec](https://github.com/liangchen-harold/astrospec)     - core algorithm
astrospec-gui - current repo, a GUI wrapper for astrospec

## Stray light remove
![correct stray light](docs/2024-05-28_1306.gif)
![correct stray light](docs/2024-05-28-0549_3.gif)

## Reference
1. [SolEx](http://www.astrosurf.com/solex/sol-ex-presentation-en.html) - The design of a DIY spectroheliograph by Valerie Desnoux, with very detailed introduction, which is worth reading carefully.
2. [DIY迷你太阳光谱仪](https://www.bilibili.com/video/BV1um421j7co) by 阴天wnova酱 - The design of another DIY mini-spectroheliograph
3. [Solex_ser_recon](https://github.com/Vdesnoux/Solex_ser_recon) - An open-source reconstruct software made by Valerie Desnoux
4. [SHG](https://github.com/thelondonsmiths/Solex_ser_recon_EN) - Another open-source reconstruct software
5. [又能看光谱又能拍摄太阳的太阳光谱仪](https://www.bilibili.com/video/BV1fw411W7HJ) by 摄日者天文
6. [太阳光谱扫描成像](https://lcsky.org/3.0/2024/05/19/spectroheliograph-1/) by Harold Liang - My DIY and observation records

## License

Astrospec has a MIT-style license, as found in the [LICENSE](LICENSE) file.
