import requests
# res = requests.post("http://127.0.0.1:8000/post_info1", json={"username":"abcaada", "password":"slide1223"})


# res_login = requests.post("http://127.0.0.1:8000/Login", json={'username':'abcda','password':'asjkdia','identity':'jahfha'})
# print(res_login.json())

# res_login = requests.post("http://127.0.0.1:8000/Login", json={'username':'abcda','password':'pond1223'})
# print(res_login.json())





# reg_change = requests.post("http://127.0.0.1:8000/Change", json={'username':'abcda', 'old_password':'slide1223', 'new_password':'pond1223'})
# print(reg_change.json())


# res_order =  requests.post('http://127.0.0.1:8000/Query', json={'username':'qixuanlong'})
# print(res_order.json())

# add_order = requests.post('http://127.0.0.1:8000/Add_order', json={'create_time':14, 'username':'qixuanlong', 'menu_id':177})
# print(add_order.json())


res_login = requests.post("http://127.0.0.1:8000/StudentMenu", json={'Shop_id':1})
print(res_login.json())

# res_login = requests.post("http://127.0.0.1:8000/Add_Shop", json={'Shop_id':1})
# print(res_login.json())
