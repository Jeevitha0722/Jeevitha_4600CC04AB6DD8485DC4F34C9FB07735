class player:
  def play(self):
      print("the player is playing cricket")
class batsman(player):
  def play(self):
      print ("the batsmen is batting")
class bowler(player):
    def player(self):
       print("the bowler is bowling")
bat=batsman()
bow=bowler()
bat.play()
bow.play()