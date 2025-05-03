from random import randint
import requests
import datetime

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.power = randint(1, 5)
        self.hp = randint(10, 20)
        self.song = self.get_song()
        self.last_feed_time = datetime.datetime.now()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["sprites"]["other"]["official-artwork"]["front_default"]
        else:
            return "https://static.wikia.nocookie.net/anime-characters-fight/images/7/77/Pikachu.png/revision/latest/scale-to-width-down/700?cb=20181021155144&path-prefix=ru"
    
    #Метод для получения звука покемона через API
    def get_song(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json() 
            
            return data["cries"]["latest"]
        else:
            return "Звук отсутствует у покемона"
        
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return {
            "Фото": self.img,
            "Название": self.name,
            "Сила": self.power,
            "Здоровье": self.hp,
            "Звук": self.song
        }

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def attack(self, enemy):
        if self.hp >= 0:
            enemy.hp -= self.power
            if enemy.hp > 0:
                return f"Вы нанесли урон. Здоровье врага: {enemy.hp}"
            else:
                return "Вы победили!"
        else:
            return "Ваш покемон мертв"
        
    def feed(self, feed_interval = 20, hp_increase = 10):
        current_time = datetime.datetime.now()
        delta_time = datetime.timedelta(seconds=feed_interval)
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"
        
    
        
