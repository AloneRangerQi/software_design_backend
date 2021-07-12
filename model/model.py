from tortoise import Model, fields
from tortoise.contrib.pydantic import pydantic_model_creator

class Information(Model):
    '''
    Usernmae:用户名（手机号）
    Password:密码
    Identyty:身份编号
    '''
    Username = fields.CharField(pk = True, max_length = 20)
    Password = fields.CharField(max_length = 20)
    Identity = fields.CharField(max_length = 20)


class Shop(Model):
    '''
    Shop_id:商家编号（自然增长主键）
    Belong:所属餐厅
    Name:档口名称
    Manager:档口负责人手机号
    '''
    Shop_id = fields.IntField(pk = True)
    Belong = fields.CharField(max_length = 20)
    Name = fields.CharField(max_length = 20)
    Manager = fields.ForeignKeyField('models.Information', to_field = 'Username', on_delete = fields.CASCADE)


class Menu(Model):
    '''
    Menu_id:菜品编号（自然增长主键）
    Shop_id:所属档口
    Menu_name:菜品名称
    Price:菜品单价

    菜品描述
    '''
    Menu_id = fields.IntField(pk = True)
    Shop_id = fields.ForeignKeyField('models.Shop', on_delete = fields.CASCADE)
    Menu_name = fields.CharField(max_length = 20)
    Menu_des = fields.CharField(max_length = 50)
    Price = fields.IntField()


class OrderSet(Model):
    '''
    Order_id:订单编号（自增主键）
    Create_time:订单创建时间
    Last_change_time:订单最后修改时间
    Total_price:订单总价
    Shop_id:档口编号
    Username:消费者用户名

    待加入
    address:收货地址
    detail:字符字段、把订单信息全部记录
    '''
    Order_id = fields.IntField(pk = True)
    Create_time = fields.DatetimeField(auto_now_add = True)
    Last_change_time = fields.DatetimeField(auto_now_add = True)
    Total_price = fields.IntField()
    Shop_id = fields.ForeignKeyField('models.Shop', on_delete = fields.CASCADE)
    Username =  fields.ForeignKeyField('models.Information', to_field = 'Username', on_delete = fields.CASCADE)
    Address = fields.CharField(max_length = 20)
    detail = fields.CharField(max_length = 40)
    Order_status = fields.CharField(max_length = 20)


# class Detail(Model):
#     '''
#     ID:自然增长主键
#     Order_id:订单号
#     Menu_name:菜品编号
#     Times:购买数量
#     '''
#     ID = fields.IntField(pk = True)
#     Order_id = fields.ForeignKeyField('models.OrderSet', to_field = 'Order_id', on_delete  = fields.CASCADE)
#     Menu_id = fields.ForeignKeyField('models.Menu', to_field = 'Menu_id', on_delete =fields.CASCADE)
#     Times = fields.IntField()
