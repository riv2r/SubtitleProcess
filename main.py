from google_trans_new import google_translator
import os

#构建翻译器
translator = google_translator()

pathEn=r'C:\Users\jungle\Desktop\曾益慧创视频\en'
pathCn=r'C:\Users\jungle\Desktop\曾益慧创视频\cn'
pathRstCn=r'C:\Users\jungle\Desktop\曾益慧创视频\rstcn'

enFiles=os.listdir(pathEn)
cnFiles=os.listdir(pathCn)
rstCnFiles=cnFiles
'''
print(enFiles)
print(cnFiles)
'''
numOfFiles=len(enFiles)

for I in range(numOfFiles):
    # 打开英文字幕文件
    enFile = open(pathEn+'\\'+enFiles[I],'r',encoding='utf-8')
    # 打开中文字幕文件（读）
    cnFile = open(pathCn+'\\'+cnFiles[I],'r',encoding='utf-8')
    # 打开中文字幕文件（写）
    cnWFile =open(pathRstCn+'\\'+rstCnFiles[I],'w',encoding='utf-8')

    enLines = enFile.readlines()
    enStrList = []
    i = 2
    while i < len(enLines):
        enStrList.append(enLines[i][:-1])
        i = i+4
    # 合并字符串
    enStr = ' '.join(enStrList)
    # 翻译字符串
    trdStr = translator.translate(enStr, lang_tgt='zh-cn')
    cnStrList=trdStr.split('，')
    #print(translated)
    cnLines = cnFile.readlines()
    #print(len(cnLines)/4)
    #最终字符串
    rst=[]
    #控制长度标准字
    flag=0

    while(True):
        cnList=[]
        i=0
        while i < len(cnStrList):
            if len(cnStrList[i]) <= flag:
                if i+1==len(cnStrList):
                    cnList.append(cnStrList[i])
                else:
                    cnList.append(cnStrList[i]+'，'+cnStrList[i+1])
                i = i + 2
            else:
                cnList.append(cnStrList[i])
                i = i + 1
        if len(cnList) <= len(cnLines)/4:
            rst=cnList
            break
        else:
            flag=flag+1
    i=2
    j=0
    while i < len(cnLines):
        if j >= len(rst):
            cnLines[i] = '\n'
            i=i+4
            continue
        else:
            cnLines[i]=rst[j]+'\n'
            i=i+4
            j=j+1

    print(len(rst))
    cnWFile.writelines(cnLines)