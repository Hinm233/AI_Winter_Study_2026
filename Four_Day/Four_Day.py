# def read_nonfound_fild():
#     try:
#         with open("C:\\Users\\HinmY\\Documents\\双拷.CSV","r",encoding="GBK") as f:
#             read_nei=f.read()
#             print(f"内容{read_nei}")
#     except FileNotFoundError:
#         print("文件不存在")
#     except Exception as e:
#         print(f"程序出错:{错误信息}".format(错误信息=str(e)))
#     finally:
#         print("文件操作结束")
#
# read_nonfound_fild()


# def read_csv():
#     try:
#         with open("C:\\Users\\HinmY\\Documents\\双拷.CSV","r",encoding="GBK")as f:
#             read_num=f.read()
#             print(read_num)
#
#     except FileNotFoundError:
#         print("文件不存在")
#     finally:
#         print("程序结束")
# read_csv()

# TXT文件读写
# def Txt_File_wr():
#
# #     待写入列表
#     score_list=["张三：80","李四：90","王二: 99"]
#
#     try :
#         # 写入
#         with open("D:\\寒假学习计划_Linux\\Four_Day\\新建 文本文档.txt","w",encoding="utf-8") as f:
#             for line in score_list:
#                 f.write(line+"\n")
#
#             print("文件写入完毕")
#
#
#
#         with open("D:\\寒假学习计划_Linux\\Four_Day\\新建 文本文档.txt","r",encoding="utf-8") as f:
#             for line in f:
#                 clean_line=line.strip()
#                 print(clean_line)
#
#
#     except PermissionError:
#         print("权限错误：没有读写文件权限")
#     except Exception as e:
#         print(f"TXT 操作出错：{str(e)}")
#     finally:
#         print("文件操作完成")
#
#
# Txt_File_wr()


# CSV文件读写
#
# import csv
#
# def csv_file_operation():
#     csv_data=[
#         ["name","math","Python"],
#         ["Jame",90,80],
#         ["Daly",99,88],
#         ["Lily",78,89]
#     ]
#
#     with open("stu_score.csv","w",encoding="utf-8",newline="") as f:
#         writer=csv.writer(f)#创建csv写入器
#         writer.writerows(csv_data)
#
#     print("CSV文件写入完成")
#     with open("stu_score.csv","r",encoding="utf-8") as f:
# #         创建CSV读入器
#         reader=csv.reader(f)
#         for line in reader:
#             print(line)








#
# import csv
# def csv_file():
#     #数据
#     csv_data=[
#         ["name","math","Python"],
#         ["Jame",80,90],
#         ["Donk",90,88],
#         ["Nik0",88,88]
#     ]
#     try:
#         with open("D:\\寒假学习计划_Linux\\Four_Day\\stu_score.csv","w",encoding="utf-8",newline="") as f:
#             #创建csv读入器
#             writer=csv.writer(f)
#             writer.writerows(csv_data)
#         print("写入完毕")
#         with open("D:\\寒假学习计划_Linux\\Four_Day\\stu_score.csv","r",encoding="utf-8") as f:
#             #创建csv写入器
#             reader=csv.reader(f)
#             for line in reader:
#                 print(line)
#     except PermissionError:
#         print("权限错误")
#     except Exception as e:
#         print(f"csv 操作出错:{str(e)}")
#     finally:
#         print("操作完成")
# csv_file()

# 综合练习

import csv

def file_Read_and_Write():

#数据
    txt_data=["Jame:80","Donk:90","Niko:88"]
    csv_data=[
        ["Name","Math","Python"],
        ["Jame",80,90],
        ["Donk",88,99],
        ["Niko",99,88]
    ]
    # woxiangkankan
    #TXT读写
    try:
        with open("D:\\寒假学习计划_Linux\\Four_Day\\新建 文本文档.txt","w",encoding="utf-8")as f:
            # f.write(txt_data),写入是str，不能是列表的形式
            for line in txt_data:
                f.write(line+"\n")
        print("写入完成")
        with open("D:\\寒假学习计划_Linux\\Four_Day\\新建 文本文档.txt","r",encoding="utf-8") as f:
            print(f.read())

    except FileNotFoundError:
        print("文件不存在")
    except Exception as e:
        print(f"程序错误：{str(e)}")

    finally:
        print("程序执行完成")



    try:
        with open("D:\\寒假学习计划_Linux\\Four_Day\\stu_score.csv","w",encoding="utf-8",newline="") as f:
            #创建csv写入器
            writer=csv.writer(f)
            writer.writerows(csv_data)

        print("CSV文件写入完毕")
        with open("D:\\寒假学习计划_Linux\\Four_Day\\stu_score.csv","r",encoding="utf-8")as f:
            #创建csv写入器
            reader=csv.reader(f)
            for line in reader:
                print(line)
    except PermissionError:
        print("权限不足")
file_Read_and_Write()