# custom_persistence.py

from telegram.ext.persistence import BasePersistence
import pickle

class CustomPicklePersistence(BasePersistence):
    def __init__(self, filepath):
        self.filepath = filepath

    def get_chat_data(self):
        try:
            with open(self.filepath, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return {}

    def update_chat_data(self, chat_id, data):
        chat_data = self.get_chat_data()
        chat_data[chat_id] = data
        with open(self.filepath, 'wb') as f:
            pickle.dump(chat_data, f)

    def get_user_data(self):
        try:
            with open(self.filepath, 'rb') as f:
                chat_data = pickle.load(f)
                return chat_data.get('user_data', {})
        except FileNotFoundError:
            return {}

    def update_user_data(self, user_id, data):
        chat_data = self.get_chat_data()
        chat_data['user_data'] = data
        with open(self.filepath, 'wb') as f:
            pickle.dump(chat_data, f)
