from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Diary


class LoggedInTestCase(TestCase):
    def setUp(self):
        # テストユーザ情報をインスタンス変数に格納しておく
        self.password = 'login_password'
        self.test_user = get_user_model().objects.create_user(
            username='login_user_name',
            email='login_email@test.com',
            password=self.password
        )
        # テスト用ユーザーでログインする
        self.client.login(email=self.test_user.email, password=self.password)


class TestDiaryCreateView(LoggedInTestCase):
    def test_create_diary_success(self):
        # 日記作成処理が成功することを検証
        params = {
            'title': 'テストタイトル',
            'content': '本文',
            'photo1': '',
            'photo2': '',
            'photo3': ''
        }
        # 新規日記作成処理(`Post`)を実行
        response = self.client.post(
            reverse_lazy('diary:diary_create'), params)
        # 日記リストページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('diary:diary_list'))
        # 日記データがDBに登録されたかを検証
        self.assertEqual(Diary.objects.filter(title='テストタイトル').count(), 1)


class TestDiaryUpdateView(LoggedInTestCase):
    def test_update_diary_success(self):
        # 日記編集処理が成功することを検証
        # テスト用日記データの作成
        diary = Diary.objects.create(user=self.test_user, title="タイトル編集前")
        # Postパラメータ
        params = {
            'title': 'タイトル編集後',
        }
        # 日記編集処理(`Post`)を実行
        response = self.client.post(
            reverse_lazy('diary:diary_update', kwargs={'pk': diary.pk}), params)
        # 日記詳細ページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy(
            'diary:diary_detail', kwargs={'pk': diary.pk}))
        # 日記データがDBに登録されたかを検証
        self.assertEqual(Diary.objects.filter(title='タイトル編集後').count(), 1)


class TestDiaryDeleteView(LoggedInTestCase):
    def test_delete_diary_success(self):
        # 日記削除処理が成功することを検証
        # テスト用日記データの作成
        diary = Diary.objects.create(user=self.test_user, title="タイトル")
        # 削除前は1件
        self.assertEqual(Diary.objects.filter(pk=diary.pk).count(), 1)
        # 日記削除処理(`Post`)を実行
        response = self.client.post(
            reverse_lazy('diary:diary_delete', kwargs={'pk': diary.pk}))
        # 日記リストページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy(
            'diary:diary_list'))
        # 日記データが削除されたかを検証
        self.assertEqual(Diary.objects.filter(pk=diary.pk).count(), 0)

    def test_delete_diary_failure(self):
        # 存在しないレコードに対して日記削除処理(`Post`)を実行
        response = self.client.post(
            reverse_lazy('diary:diary_delete', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)
