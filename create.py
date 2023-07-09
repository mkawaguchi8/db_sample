from db_config import Message


def create_message():
    # インスタンスを作成してから保存 → tableplusに追加されている
    message = Message(user="Bob", content="Hello Tom!")
    message.save()

# インスタンスを生成しないで保存するcreatメソッド
    Message.create(user="Tom", content="Hello Bob!")


if __name__ == "__main__":
    create_message()
