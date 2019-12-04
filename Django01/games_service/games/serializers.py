from rest_framework import serializers
from games.models import Game

from rest_framework import serializers 
from games.models import Game 
 
 
class GameSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Game 
        fields = ('id',  
                  'name',  
                  'release_date', 
                  'esrb_rating',  
                  'played_once', 
                  'played_times',)

