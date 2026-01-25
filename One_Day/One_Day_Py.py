# def Sum_score(score_list):
#     total=sum(score_list)
#     avg=total/len(score_list)
#     return total,avg
#
#
# # 创建学生列表，完成增删改查遍历
# score_list=[85,92,78,90,88]
# print(f"原先的：{score_list}")
# # 在列表末尾增加.append
# score_list.append(42)
#
# print(f"在末尾：{score_list}")
# # 指定位置添加insert
# score_list.insert(2,80)#在78位置上添加80，78之后的数往后移
# print(f"指定的：{score_list}")
# score_list.sort()#默认升序
# print(score_list)
# score_list.sort(reverse=True)
# print(score_list)
#
#
#
# # 创建字典
# stu_dict={"张小三":80,"李四":90,"王二":88,"麻子":92}
# print(stu_dict)
# stu_dict["奥特慢"]=66
# print(stu_dict)
#
# del  stu_dict["麻子"]
# print(stu_dict)
#
# stu_dict["李四"]=100
# print(stu_dict)
#
# print(stu_dict.get("王二"))
# print(stu_dict.get("张一","无"))
#
# for i in stu_dict:
#     print(i)
#
# for i in stu_dict.values():
#     print(i)
#
# for i,j in stu_dict.items():
#     print(i,j)
# 定义函数
# def student_grade_manange():
# #     学生字典
#     student_score={}
#     print("-----学生管理系统-----")
#     print("1.添加学生信息\n"
#           "2.删除学生信息\n"
#           "3.修改学生信息\n"
#           "4.查询\n"
#           "5.退出")
#     while(True):
#         choice=int(input("选择数字(0-5)\n"))
# # 添加学生信息
#
#         if choice==1:
#             name = input("输入姓名")
#             score = float(input("输入成绩"))
#             student_score[name] = score
#             print(student_score)
#
#         elif choice==2:
#             name=input("输入删除的学生姓名")
#             if name in student_score:
#                 del student_score[name]
#             else:
#                 print("学生不存在")
#         elif choice==3:
#             name=input("输入需要修改学生姓名\n")
#             if name in student_score:
#                 try:
#                     new_score=float(input("输入新的成绩"))
#                     old_score=student_score[name]
#                     student_score[name]=new_score
#                     print(f"学生:{name},成绩由{old_score}->{new_score}")
#
#
#                 except:
#                     print("请输入数字")
#         elif choice==4:
# #             查询
#             name_num=int(input("输入查询的数字（1，单个查询"
#                            "2.查询全部)"))
#             if name_num==1:
#                 name=input("请输入查询的姓名\n")
#                 if name in student_score:
#
#                     print(student_score[name])
#
#                 else:
#                     print("不存在该学生")
#             elif name_num==2:
#                 if student_score:
#                     for i, j in student_score.items():
#                         print(i, j)
#
#         elif choice==5:
#             return
#         else:
#             print("无效选择")
#
#
# student_grade_manange()