import cloudscraper
from kickapi.channel_data import ChannelData
from kickapi.video_data import VideoData
from kickapi.chat_data import ChatMessage

class KickAPI:
    def __init__(self):
        # Inicializa CloudScraper
        print("Inicializando CloudScraper...")
        self.scraper = cloudscraper.create_scraper()

    def channel(self, username):
        # Obtener datos del canal por nombre de usuario
        
        response = self.scraper.get(f'https://kick.com/api/v1/channels/{username}', timeout=10)
        if response.status_code == 200:
            try:
                data = response.json()
                
                return ChannelData(data)
            except ValueError:
                print("Failed to parse JSON response.")
                return None
        else:
            
            return None
        
    def video(self, video_id):
        # Obtener datos del video por ID de video
        
        response = self.scraper.get(f"https://kick.com/api/v1/video/{video_id}", timeout=10)
        
        if response.status_code == 200:
            try:
                data = response.json()
                
                return VideoData(data)
            except ValueError:
                print("Failed to parse JSON response.")
                return None
        else:
            
            return None
        
    """def chat(self, channel_id, datetime):
        # Obtener datos de chat por ID de canal
        
        response = self.scraper.get(f"https://kick.com/api/v2/channels/{channel_id}/messages?start_time={datetime}", timeout=10)
        
        if response.status_code == 200:
            try:
                data = response.json()
                
                return ChatData(data)
            except ValueError:
                print("Failed to parse JSON response.")
                return None
        else:
            
            return None"""
    
    def chat(self, channel_id, datetime):
        # Obtener datos de chat por ID de canal
        response = self.scraper.get(f"https://kick.com/api/v2/channels/{channel_id}/messages?start_time={datetime}", timeout=10)
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data and data.get("data") and data["data"].get("messages"):
                    # Obtener solo el primer mensaje
                    first_message = data["data"]["messages"][0]
                    return ChatMessage(first_message)
                else:
                    print("No messages found.")
                    return None
            except ValueError:
                print("Failed to parse JSON response.")
                return None
        else:
            return None

