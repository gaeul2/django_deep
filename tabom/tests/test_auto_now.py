# from django.test import TestCase #장고의 테스트에서 TestCase를 불러와야함
# from tabom.models import User
# from django.db import connection
# from time import sleep
# from datetime import datetime
#
#
# class TestAutoNow(TestCase):
#     def test_auto_now_field_is_set_when_save(self) -> None: #얘는 None을 리턴한다. testcase는 리턴하는게 없어야함.
#         user = User(name='test')
#         user.save()
#         self.assertIsNotNone(user.updated_at)
#         self.assertIsNotNone(user.created_at)
#
#     def test_auto_now_field_not_set_when_raw_sql_update_executed(self) -> None:
#         # Given
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 "INSERT INTO tabom_user(id, name, updated_at, created_at) "
#                 "VALUES (1, 'hihi', '1999-01-01 10:10:10', '1999-01-01 10:10:10')"
#             )
#
#             # When
#             sleep(1)
#             cursor.execute(
#                 "UPDATE tabom_user SET name='changed' WHERE id=1"
#             )
#
#         # Then
#         user = User.objects.filter(id=1).get()
#         self.assertEqual(user.updated_at, datetime(year=1999, month=1, day=1, hour=10, minute=10, second=10))
