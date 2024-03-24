from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # 添加一些 Menu 实例到数据库中
        Menu.objects.create(title='Item 1', price='10.99', inventory=20)
        Menu.objects.create(title='Item 2', price='15.99', inventory=15)

    def test_getall(self):
        # 发起 GET 请求以获取所有 Menu 对象
        response = self.client.get('/restaurant/menu/')  # 假设 URL 是 /api/menu/

        # 检查响应状态码是否为 200
        self.assertEqual(response.status_code, 200)

        # 序列化 Menu 对象
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        print(response.data)

        # 检查响应的数据是否与序列化后的数据一致
        self.assertEqual(response.data, serializer.data)