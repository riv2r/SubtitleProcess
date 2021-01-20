# 字幕处理程序

> IECUBE实习任务为：将YouTube上的相关视频下载到本地，并下载自动生成的英文和中文字幕，采用本程序对英文字幕连接为一整个自然段，并翻译为流畅中文，嵌入到新生成的中文字幕文件中

对于YouTube相关视频和字幕的下载，采用如下三个chrome插件：

>- [本地 YouTube 下载器](https://greasyfork.org/zh-CN/scripts/369400-local-youtube-downloader)
>- [Youtube Subtitle Downloader](https://greasyfork.org/zh-CN/scripts/5368-youtube-subtitle-downloader-v28)
>- [Youtube 翻译中文字幕下载](https://greasyfork.org/zh-CN/scripts/38941-youtube-%E7%BF%BB%E8%AF%91%E4%B8%AD%E6%96%87%E5%AD%97%E5%B9%95%E4%B8%8B%E8%BD%BD-v10)

程序中如下几行需要根据自己的使用情景进行调整

```python
pathEn=r''#下载的英文字幕所在路径
pathCn=r''#下载的中文字幕所在路径
pathRstCn=r''#待生成的中文字幕所在路径
```

