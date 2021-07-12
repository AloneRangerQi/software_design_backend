from fastapi import FastAPI, Request, Form, HTTPException, Path
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise

from model.model import Information, Menu, OrderSet, Shop


import uvicorn
from pydantic import BaseModel

from typing import Optional, List, Dict

app = FastAPI()

templates = Jinja2Templates(directory = 'templates')

register_tortoise(app,
                  db_url = 'mysql://root:slide1223@localhost/fastapi',
                  modules = {'models':['model.model']},
                  add_exception_handlers = True,
                  generate_schemas = True)

map = {
    '234':1,
    '345':2,
    '456':3
}

class Item(BaseModel):
    '''
    注册-登陆请求响应类
    username: 用户手机号
    password: 用户明码
    Identity: 用户身份: （str）
    '''
    username: str
    password: str
    identity: str

class Change_Item(BaseModel):
    '''
    修改密码响应类
    '''
    username: str
    old_password: str
    new_password: str

class Order_Item(BaseModel):
    '''
    订单查看响应类
    '''
    username: str


@app.post("/enroll/", response_model=Item)
async def Enroll(request_data: Item):
    '''
    必须传json的post接口
    :param request_data: json字段（Item类）
    '''
    usr = request_data.username
    pas = request_data.password
    ide = request_data.identity

    Enroll_result = await Information.filter(Username = usr)
    if Enroll_result:
        raise HTTPException(status_code = 400, detail = 'Username already Registered')
    await Information(Username = usr, Password = pas, Identity = ide).save()
    return request_data



@app.post("/Login/")
async def Login(request_data: Item):
    '''
    用户名在就返回结果
    '''
    usr = request_data.username
    pas = request_data.password
    ide = request_data.identity

    Login_result = await Information.filter(Username = usr).first()
    if Login_result:
        for item in Login_result:
            if item[0] == 'Username':
                USR_DB = item[1]
            elif item[0] == 'Password':
                PAS_DB = item[1]
            elif item[0] == 'Identity':
                IDE_DB =  item[1]

        # if usr in map.keys():
        #     Login_dict ={
        #         'username': USR_DB,
        #         'password': PAS_DB,
        #         'identity': IDE_DB,
        #         'shop': map[usr]
        #     }

        # else:
        Login_dict = {
            'username': USR_DB,
            'password': PAS_DB,
            'identity': IDE_DB
            }
        return Login_dict
    else:
        Login_dict = {
            'username':'',
            'password':'',
            'identity':''
        }
        return Login_dict



@app.post('/Change/', response_model = Change_Item)
async def Change(request_data: Change_Item):
    usr = request_data.username
    old_pas = request_data.old_password
    new_pas = request_data.new_password

    Serach_result = await Information.filter(Username = usr).first()
    if Serach_result:
        for item in Serach_result:
            if item[0] == 'Username':
                USR_DB = item[1]
            elif item[0] == 'Password':
                PAS_DB = item[1]
            elif item[0] == 'Identity':
                IDE_DB = item[1]
        if PAS_DB == old_pas:
            '''
            删除原先记录
            创建新纪录
            '''
            await Information.filter(Username = usr).delete()
            await Information(Username = usr, Password = new_pas, Identity = IDE_DB).save()
            print('Change Successful, The new password is:', new_pas)
            return request_data
        else:
            raise HTTPException(status_code = 400, detail = 'Password Wrong')
    else:
        raise HTTPException(status_code = 400, detail = 'Username not Exsits')


@app.post('/Student_Query/')
async def Query(request_data: Order_Item):
    '''
    查询订单
    '''
    usr = request_data.username
    Query_result = await OrderSet.filter(Username_id = usr)
    Query_dict = {}
    Query_list = []
    for Query_item in Query_result:
        item = {
            # 除了最后修改时间、订单号、状态都要
            # 'username': Query_item.Username_id,
            # 'address': Query_item.Address,
            # 'shopId': Query_item.Shop_id_id,
            'price': Query_item.Total_price,
            'detail': Query_item.Detail,
            'createTime': str(Query_item.Create_time)[0:10],
            # 'name': Query_item.Name,
            # 'phonenum': Query_item.Phonenum,
            # 'studentnum': Query_item.Studentnum
        }
        Query_list.append(item)
    Query_dict['data'] = Query_list
    # print(Query_dict)
    return Query_dict



class Add_Item(BaseModel):
    '''
    添加订单请求类
    '''
    Username: str
    Name: str
    Studentnum: str
    Phonenum:  str
    Total_price: int
    Shop_id: int
    Address: str
    Detail: str

@app.post('/Add_Order/')
async def Add_order(request_data: Add_Item):
    '''
    提交订单
    '''
    username = request_data.Username
    name = request_data.Name
    studentnum  = request_data.Studentnum
    phonenum =  request_data.Phonenum
    total_price = request_data.Total_price
    shop_id = request_data.Shop_id
    address = request_data.Address
    detail = request_data.Detail

    await OrderSet(Username_id = username, Name = name, Studentnum = studentnum, Phonenum = phonenum, Detail = detail, Address = address, Shop_id_id = shop_id, Total_price = total_price, Order_status = 'Nomal').save()


class Add_Shop_Item(BaseModel):
    Belong: str
    Name: str
    Manager: str

@app.post('/Add_Shop/')
async def Add_Shop(request_data: Add_Shop_Item):
    '''
    餐厅（Belong）提前写死
    '''
    Belong = request_data.Belong
    Name = request_data.Name
    Manager = request_data.Manager
    # if await Shop.filter(Belong = Belong):
    #     if await Shop.filter(Name = Name, Belong = Belong):
    #         raise HTTPException(status_code = 400, detail = 'Shop has exsits')
    #     else:
    #         await Shop(Belong = Belong, Name = Name, Manager_id = Manager).save()
    # else:
    #     raise HTTPException(status_code = 400, detail = 'Canteen not exsits')
    await Shop(Belong = Belong, Name = Name, Manager_id = Manager).save()



class Add_Menu_Item(BaseModel):
    Shop_id: int
    Menu_name: str
    Menu_des: str
    price: str
    Package: str

@app.post('/Add_Menu/')
async def Add_Menu(request_data: Add_Menu_Item):
    Shop_id = request_data.Shop_id
    Menu_name = request_data.Menu_name
    Menu_des = request_data.Menu_des
    Price = int(request_data.price)
    Package = request_data.Package

    if await Shop.filter(Shop_id = Shop_id):
        if await Menu.filter(Shop_id_id = Shop_id, Menu_name = Menu_name):
            raise HTTPException(status_code = 400, detail = 'Menu has exsits')
        else:
            await Menu(Shop_id_id = Shop_id, Menu_name = Menu_name, Menu_des = Menu_des, Price = Price, Package = Package).save()
    else:
        raise HTTPException(status_code = 400, detail = 'Shop not exsits')



class Delete_Menu_Item(BaseModel):
    Shop_id: int
    Menu_name: str

@app.post('/Delete_Menu/')
async def Delete_Menu(request_data: Delete_Menu_Item):
    Shop_id = request_data.Shop_id
    Menu_name = request_data.Menu_name
    await Menu.filter(Shop_id_id = Shop_id, Menu_name = Menu_name).delete()


# @app.get('/{Canteen_name}')
# async def Select_canteen(Canteen_name):
#     '''
#     选择餐厅返回该餐厅的档口及其编号
#     '''
#     Select_canteen_result = await Shop.filter(Belong = Canteen_name)
#     if Select_canteen_result:
#         canteen_dict = {}
#         # count = 0
#         for canteen in Select_canteen_result:
#             canteen_dict[canteen.Shop_id] = canteen.Name
#             # count = count + 1
#             # print(canteen_dict)
#         print(canteen_dict)
#         return canteen_dict
#     else:
#         raise HTTPException(status_code = 400, detail = 'Canteen does not exsits')


class Select_Menu_Item(BaseModel):
    Shop_id: int
@app.post('/StudentMenu/')
async def Select_Shop_Student(request_data: Select_Menu_Item):
    Shop_id = request_data.Shop_id
    Shop_Menu = await Menu.filter(Shop_id = Shop_id, Package = 'false')
    Shop_dict_final = {}
    Shop_list = []
    for menu in Shop_Menu:
        Shop_dict = {}
        Shop_dict['quantity'] = 0
        Shop_dict['title'] = menu.Menu_name
        Shop_dict['price'] = menu.Price
        Shop_list.append(Shop_dict)
    Shop_dict_final['data'] = Shop_list
    print(Shop_dict_final)
    return Shop_dict_final


@app.post('/getherMenu/')
async def Select_Shop_teacher(request_data: Select_Menu_Item):
    Shop_id = request_data.Shop_id
    Shop_Menu = await Menu.filter(Shop_id = Shop_id, Package = 'true')
    Shop_dict_final = {}
    Shop_list = []
    for menu in Shop_Menu:
        Shop_dict = {}
        Shop_dict['quantity'] = 0
        Shop_dict['title'] = menu.Menu_name
        Shop_dict['price'] = menu.Price
        Shop_list.append(Shop_dict)
    Shop_dict_final['data'] = Shop_list
    print(Shop_dict_final)
    return Shop_dict_final


class Delete_Order_Item(BaseModel):
    Order_id: int

@app.post('/Delete_Order/')
async def Delete_Order(request_data: Delete_Order_Item):
    order_id = request_data.Order_id
    await OrderSet.filter(Order_id = order_id).update(Order_status = 'Cancel')



# @app.get('/Order/{Order_id}')
# async def Delete_Order(Order_id):
#     await OrderSet.filter(Order_id = Order_id).update(Order_status = 'Cancel')
