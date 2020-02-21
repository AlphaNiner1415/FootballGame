public class test {
    public static void main(String[] args) {
        Player Anon = new Player("Anon", "None");
        Player Opponent_1 = new Player("Opponent 1","Goalie");
        Player Opponent_2 = new Player("Opponent 2","Defender");
        Player Opponent_3= new Player("Opponent 3","Defender");
        Player Opponent_4 = new Player("Opponent 4","Defender");
        Player Opponent_5 = new Player("Opponent 5","Defender");
        Player Opponent_6 = new Player("Opponent 6","Midfielder");
        Player Opponent_7 = new Player("Opponent 7","Midfielder");
        Player Opponent_8 = new Player("Opponent 8","Midfielder");
        Player Opponent_9 = new Player("Opponent 9","Midfielder");
        Player Opponent_10 = new Player("Opponent 10","Striker");
        Player Opponent_11 = new Player("Opponent 11","Striker");

        Anon.levelUp();
   

    
    }
    
    public void sequence1(String playerTeam, String playerName) {
        System.out.printf("And the match is kicking off!!! Ladies and Gentlemen here we go!!! The %s are going to be kicking it off first and oh well it looks like\nthere star player, %s, has the ball!!!! \nHe takes it pass midfield and tries to dribble through the opposing team's defender!!!",playerTeam,playerName);
    
    }
}