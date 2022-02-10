from django.test import TestCase


class TestView(TestCase):
    def test_add_view(self) -> None:
        result = self.client.get("/api/add", {"a": 1, "b": 3})
        self.assertEqual(result.status_code, 200)  # 응답값이 제대로 오는지 확인하는 코드
        self.assertEqual(result.json(), {"result": 4})  # 결과가 4인지 검증함
