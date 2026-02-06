import pandas as pd
import numpy as np
import random
from datetime import datetime,timedelta

# 设置随机种子，保证结果可复现
np.random.seed(666)
random.seed(666)

n=1000

user_id=np.random.randint(1000,2000,n)
order_id=np.random.randint(10000,99999,n)

# 构造下单时间
start_time=datetime(2025,1,1)
order_time=[start_time+timedelta(days=random.randint(0,364),
                                 hours=random.randint(0,23),
                                 minutes=random.randint(0,59))
            for _ in range(n)]
order_time=[t.strftime("%Y-%m-%d %H:%M:%S")for t in order_time]
# 支付金额
pay_amout = np.random.uniform(10,5000,n)
pay_amout[np.random.choice(n,int(n*0.05),replace=False)]=np.nan
# 商品品类：5类随机

product_type=random.choices(["家电","服装","食品","数码","美妆"],k=n)
pay_type=random.choices(["微信","支付宝","银行卡"],k=n)
# 组合成DataFrame
df=pd.DataFrame({
    "user_id":user_id,
    "order_id":order_id,
    "order_time":order_time,
    "pay_amount":pay_amout,
    "product_type":product_type,
    "pay_type":pay_type
})

df=pd.concat([df,df.head(5)],ignore_index=True)

df.to_csv("D:\\寒假学习计划_Linux\\Pandas_Project\\user_consumer.csv",index=False,encoding="utf-8")

print("数据生成完成！文件名为：user_consumer.csv")
print(f"数据形状：{df.shape}（行×列）")