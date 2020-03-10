// YOU DO NOT NEED TO IMPLEMENT ANY CODE FOR THIS CLASS
// READ IT SO THAT YOU CAN USE IT CORRECTLY.

public class Cell{
  private int player; // 0 is red, 1 blue
  boolean isEmpty;
  public Cell(){
    player = -1;
    isEmpty = true; 
  }
  public int getPlayer(){
    return player;
  }
  public void setPlayer(int p){
    player = p;
  }
}
