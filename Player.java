import java.util.Scanner;

public class Player {
    protected int attribute_points = 10;
    protected String name = "";
    protected int speed = 5;
    protected int dribble = 5;
    protected int passing = 5;
    protected int tackle = 5;
    protected int kickblock = 5;
    protected int shooting = 5;
    protected int goalie_save = 0;
    protected int level = 1;

    public Player(String name, String position) {
        this.name = name;
        if (position.toLowerCase() == "attacker" || position.toLowerCase() == "striker"){
            this.shooting += 2;
            this.dribble += 1;
            this.tackle -= 1;
            this.kickblock -= 1;
        }
        if (position.toLowerCase() == "midfielder"){
            this.dribble += 2;
            this.passing += 2;
            this.tackle -= 2;
            this.kickblock -= 1;
            this.speed += 2;
            this.shooting -= 1;
        }
        if (position.toLowerCase() == "defender"){
            this.shooting -= 3;
            this.dribble -= 1;
            this.tackle += 2;
            this.kickblock += 2;
        }
        if (position.toLowerCase() == "goalie"){
            this.speed -= 5;
            this.dribble -= 5;
            this.passing -= 5;
            this.tackle -= 5;
            this.kickblock -= 5;
            this.shooting -= 5;
            this.goalie_save += 2;
        }
    }
    public void levelUp(){
        while (this.attribute_points != 0){
            Scanner sc = new Scanner(System.in);
            System.out.printf("Speed          %d\n", this.speed);
            System.out.printf("Dribble        %d\n" , this.dribble);
            System.out.printf("Tackle         %d\n", this.tackle);
            System.out.printf("Kickblock      %d\n", this.kickblock);
            System.out.printf("Pass           %d\n", this.passing);
            System.out.println("You have " + this.attribute_points + " left.");
            System.out.print("Please enter what attribute you want to spend your points on: ");
            String playerChoice = sc.nextLine().toLowerCase();
            boolean inputIsValid = true;
            switch (playerChoice) {
                case "speed":
                    this.speed += 1;
                    break;
                case "dribble":
                    this.dribble += 1;
                    break;
                case "passing":
                    this.passing += 1;
                    break;
                case "tackle":
                    this.tackle += 1;
                    break;
                case "kickblock":
                    this.speed += 1;
                    break;
                case "shooting":
                    this.shooting += 1;
                    break;
                case "goalie_save":
                    this.goalie_save += 1;
                    break;
                default:
                    System.out.println("Please enter a valid attribute!!!");
                    inputIsValid = false;
                    break;
            }
            if (inputIsValid) {
                System.out.println(playerChoice + " has increased by one!!");
            }
            
        }
    }

}