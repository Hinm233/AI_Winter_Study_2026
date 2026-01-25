#创建类
# class AiModel:
#     def __init__(self,model_name="LinearRegression",version="v1.0"):
#         self.model_name=model_name
#         self.version=version
#         self.train_times=0
#     def train(self,data):
#         self.train_times+=1
#         print(f"模型{self.model_name},v{self.version},正在训练,数据集：{len(data)},当前训练次数{self.train_times}")
#
#     def evaluate(self,acc):
#         print(f"模型评估准确率：{acc}%")
#
#         if acc >=90:
#             print("模型训练优秀")
#
#         else:
#             print("模型需要优化")
#
# test_data=[1,2,3,4,5]
# acc1=87
# acc2=98
#
# model=AiModel()
# model.train(test_data)
# model.evaluate(acc1)
#
# #实例化对象2：自定义参数
# model1=AiModel("Aimodel_2","v2.0")
#
# model1.train(test_data)
# model1.evaluate(acc2)


# 定义模型

class Aimodel:
    def __init__(self,model_name="Ai_model",version="v1.0.0"):
        self.model_name=model_name
        self.version=version
        self.train_ecpo=0

    def train(self,data):
        self.train_ecpo+=1
        print(f"模型{self.model_name},v{self.version},训练次数{self.train_ecpo}")

    def evaluate(self,acc):
        print(f"模型准确率为{acc}")

        if acc>=90:
            print("模型可以")

        else:
            print("模型还需调整")


model=Aimodel()

test_data=[1,2,3,4,5,6,7,8,9,10]
acc1=89
acc2=98

model.train(test_data)
model.evaluate(acc1)

model1=Aimodel("Ai_Model_one","v2.0.1")
model1.train(test_data)
model1.evaluate(acc2)
