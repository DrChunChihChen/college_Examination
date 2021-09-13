# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np
df = pd.read_excel("110考試分發考生成績-一般生.xlsx")

df['總分'] = np.where(df['錄取學系中文名稱'] == '中國文學系', df['指考國文'] + df['指考英文']+ df['指考歷史'],
            np.where(df['錄取學系中文名稱'] == '外國語文學系', df['指考國文'] + df['指考英文']+ df['指考歷史'],
            np.where(df['錄取學系中文名稱'] == '歷史學系', df['指考國文'] + df['指考英文']+ df['指考歷史'],
            np.where(df['錄取學系中文名稱'] == '日本語言文化學系', df['指考國文'] + df['指考英文']+ df['指考歷史'],
            np.where(df['錄取學系中文名稱'] == '哲學系', df['指考國文'] + df['指考英文']+ df['指考歷史']+ df['指考數學乙']+ df['指考公民與社會'],
            np.where(df['錄取學系中文名稱'] == '應用物理學系(A組)', df['指考國文'] + df['指考英文']+ df['指考數學甲'],
            np.where(df['錄取學系中文名稱'] == '應用物理學系(B組)', df['指考國文'] + df['指考英文']+ df['指考數學乙'],
            np.where(df['錄取學系中文名稱'] == '化學系化學組', df['指考物理'] + df['指考化學']+ df['指考英文']+ df['指考數學甲'],
            np.where(df['錄取學系中文名稱'] == '化學系化學生物組(A組)', df['指考物理'] + df['指考化學']+ df['指考英文']+ df['指考數學甲'],
            np.where(df['錄取學系中文名稱'] == '化學系化學生物組(B組)', df['指考生物'] + df['指考化學']+ df['指考英文']+ df['指考數學甲'],
            np.where(df['錄取學系中文名稱'] == '生命科學系生物醫學組', df['指考生物'] + df['指考化學']+  df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '生命科學系生態暨生物多樣性組', df['指考生物'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '應用數學系(A組)', df['指考數學甲'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '應用數學系(B組)', df['指考數學乙'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '化學工程與材料工程學系(製程及能源工程組)', df['指考數學甲'] + df['指考化學'] + df['指考英文']+df['指考物理'],
            np.where(df['錄取學系中文名稱'] == '化學工程與材料工程學系(材料工程組)', df['指考數學甲'] + df['指考國文'] + df['指考英文']+df['指考物理']+ df['指考化學'],
            np.where(df['錄取學系中文名稱'] == '化學工程與材料工程學系(生化工程組)', df['指考數學甲'] + df['指考國文'] + df['指考英文']+df['指考生物']+ df['指考化學'],
            np.where(df['錄取學系中文名稱'] == '工業工程與經營資訊學系(智慧設計與生產組)', df['指考數學甲'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '工業工程與經營資訊學系(智慧經營與管理組)', df['指考數學乙'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '環境科學與工程學系(自然A組)', df['指考數學甲'] + df['指考國文'] + df['指考英文']+ df['指考化學'],
            np.where(df['錄取學系中文名稱'] == '環境科學與工程學系(自然B組)', df['指考數學甲'] + df['指考國文'] + df['指考英文']+ df['指考生物'],
            np.where(df['錄取學系中文名稱'] == '資訊工程學系(資電工程組)', df['指考數學甲'] + df['指考物理'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '資訊工程學系(人工智慧組)', df['指考數學甲'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '資訊工程學系(軟體工程組)', df['指考數學乙'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '電機工程學系', df['指考數學甲'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '企業管理學系', df['指考數學乙'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '國際經營與貿易學系', df['指考數學乙'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '會計學系', df['指考數學乙'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '財務金融學系', df['指考數學乙'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '統計學系(巨量資料管理組)', df['指考數學甲'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '統計學系(決策管理組)', df['指考數學乙'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '資訊管理學系(物聯網與大數據應用組)', df['指考數學乙'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '資訊管理學系(數位行銷與電子商務應用組)', df['指考數學乙'] + df['指考國文'] + df['指考英文']+ df['指考公民與社會'],
            np.where(df['錄取學系中文名稱'] == '經濟學系一般經濟組', df['指考數學乙'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '經濟學系產業經濟組', df['指考數學乙'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '政治學系政治理論組', df['指考公民與社會'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '政治學系國際關係組', df['指考公民與社會'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '行政管理暨政策學系', df['指考公民與社會'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '社會學系', df['指考公民與社會'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '社會工作學系', df['指考公民與社會'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '畜產與生物科技學系(A組)', df['指考生物'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '畜產與生物科技學系(B組)', df['指考化學'] + df['指考國文'] + df['指考英文'],
            np.where(df['錄取學系中文名稱'] == '食品科學系(A組)', df['指考化學']+df['指考生物'] + df['指考國文'] + df['指考英文']+df['指考數學甲'] ,
            np.where(df['錄取學系中文名稱'] == '食品科學系(B組)', df['指考化學']+df['指考生物'] + df['指考國文'] + df['指考英文']+df['指考數學乙'] ,
            np.where(df['錄取學系中文名稱'] == '餐旅管理學系', df['指考歷史']+df['指考地理'] + df['指考國文'] + df['指考英文']+df['指考數學乙'] ,
            np.where(df['錄取學系中文名稱'] == '建築學系',  df['指考化學']+df['指考物理'] + df['指考國文'] + df['指考英文']+df['指考數學甲'] ,
            np.where(df['錄取學系中文名稱'] == '工業設計學系',  df['指考物理'] + df['指考國文'] + df['指考英文']+df['指考數學甲'] ,
            np.where(df['錄取學系中文名稱'] == '高齡健康與運動科學學士學位學程',  df['指考國文'] + df['指考英文']+df['指考數學乙'] ,
            np.where(df['錄取學系中文名稱'] == '景觀學系',  df['指考國文'] + df['指考英文']+df['指考生物'] ,
            np.where(df['錄取學系中文名稱'] == '法律學系',  df['指考國文'] + df['指考英文']+df['指考數學乙']+df['指考歷史']+ df['指考公民與社會'] ,
            np.where(df['錄取學系中文名稱'] == '國際學院國際經營管理學位學程',  df['指考國文'] + df['指考英文']+df['指考數學乙'] ,
            np.where(df['錄取學系中文名稱'] == '永續科學與工程學士學位學程',  df['指考化學'] + df['指考英文']+df['指考數學甲']++df['指考生物'] ,
                    10000000))))))))))))))))))))))))))))))))))))))))))))))))))))

df.to_excel (r'D:\pythonProject5_指考\df指考狀況.xlsx', index = False, header=True)



