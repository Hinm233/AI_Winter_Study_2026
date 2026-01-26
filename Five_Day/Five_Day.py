# list=[x for x in range(10) if x >=5]
#
#
#
# list1=[x for x in range(1,21) if x%2==0]
#
# score_list=[88,90,75,95,89,92]
#
# new_list=[x for x in score_list if x>=90]
#
#
# ji_list=[x**2 for x in range(1,101) if x%2!=0]
#
#
# dict={key:value for key,value in [("str1",1),("str2",2)]}
#
#
# names=["张三","李四","王五"]
# score=[90,80,89]
#
# dict1={k:v for k,v in zip(names,score)}
# # print(dict1)
#
# add=lambda a,b:a+b
# print(add(10,20))
# score_square=lambda x:x**2
# print(score_square(5))

student_scores={
    "张三":88,
    "李四":92,
    "王五":99,
    "麻子":89,
    "Jame":80
}

dic_stu={name:score for name,score in student_scores.items() if score >=90}


