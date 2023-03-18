import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.headers
        params = {"path": disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, path_to_file: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = self._get_upload_link(disk_file_path=path_to_file).get("href", "")
        response = requests.put(url, data=open('test2.txt', 'rb'))

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите путь до файла на ЯндексДиске: ')
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)