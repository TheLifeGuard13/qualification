from rest_framework import status
from rest_framework.test import APITestCase

from application.models import NetworkChain, Product, Contact
from users.models import User


class ApplicationTestCaseCSU(APITestCase):
    def setUp(self) -> None:
        """Создание тестовых пользователя, поставщика, контактов, продукта"""
        self.user = User.objects.create(email="test_email", is_staff=True, is_superuser=True, password="123")
        self.client.force_authenticate(user=self.user)
        self.network = NetworkChain.objects.create(name="TestNetwork", debt_amount="100.00")
        self.product = Product.objects.create(name="TestProduct", market_date="2024-12-31", seller=self.network)
        self.contact = Contact.objects.create(
            email="email@test.ru", country="Russia", city="Moscow", seller=self.network
        )

    def test_list_network(self) -> None:
        """Тестирование вывода списка поставщиков"""
        response = self.client.get("/network/")
        data = response.json()
        data["results"][0].pop("created")  # убираем автогенерируемую дату
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.network.id,
                    "products": [
                        {
                            "id": self.product.id,
                            "name": "TestProduct",
                            "model": None,
                            "market_date": "2024-12-31",
                            "seller": self.network.id,
                        }
                    ],
                    "contacts": [
                        {
                            "id": self.contact.id,
                            "email": "email@test.ru",
                            "country": "Russia",
                            "city": "Moscow",
                            "street": None,
                            "building": None,
                            "seller": self.network.id,
                        }
                    ],
                    "name": "TestNetwork",
                    "debt_amount": "100.00",
                    "supplier": None,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_create_network(self) -> None:
        """Тестирование создания поставщика"""
        data = {"name": "TestNetwork2", "debt_amount": "500.00"}

        response = self.client.post("/network/", data=data)
        data = response.json()
        data.pop("created")  # убираем автогенерируемую дату
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            data,
            {
                "id": response.json().get("id"),
                "products": [],
                "contacts": [],
                "name": "TestNetwork2",
                "debt_amount": "500.00",
                "supplier": None,
            },
        )

        self.assertTrue(NetworkChain.objects.all().exists())

    def test_retrieve_network(self) -> None:
        """Тестирование вывода отдельного поставщика"""
        response = self.client.get(f"/network/{self.network.pk}/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.network.name)

    def test_update_network(self) -> None:
        """Тестирование обновления поставщика"""
        data = {"name": "TestNetwork15"}
        response = self.client.patch(f"/network/{self.network.id}/", data=data)

        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get("name"), "TestNetwork15")

    def test_update_network_debt(self) -> None:
        """Тестирование обновления поставщика c попыткой изменения суммы задолженности"""
        data = {"name": "TestNetwork13", "debt_amount": "200.00"}
        response = self.client.patch(f"/network/{self.network.pk}/", data=data)

        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get("debt_amount"), self.network.debt_amount)

    def test_delete_network(self) -> None:
        """Тестирование удаления поставщика"""
        response = self.client.delete(f"/network/{self.network.pk}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(NetworkChain.objects.all().count(), 0)
