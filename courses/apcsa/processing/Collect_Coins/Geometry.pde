/*
  Implement checkForCollisionWithList below. 
*/

static class Geometry{
  /**
   This method accepts a Sprite sprite and an arraylist of Sprites and returns
   the collision list(arraylist) which consists of Sprite that collides with the given Sprite. 
   MUST CALL THE METHOD checkForCollision BELOW!
 */ 
 public static ArrayList<Sprite> checkForCollisionWithList(Sprite sprite, ArrayList<Sprite> list){
  
  // create and initialize arraylist collision_list.
  
  // for loop through each sprite s in list
  //   if s is not sprite and s and sprite does collide(call checkForCollision below)
  //      add s to collision_list
  // return collision_list

  return null; // remove this when you implement your code
}

 public static boolean checkForCollision(Sprite sprite1, Sprite sprite2){
   if(sprite1.getRight() <= sprite2.getLeft())
     return false;
   else if(sprite2.getRight() <= sprite1.getLeft())
     return false;
   else if(sprite1.getBottom() <= sprite2.getTop())
     return false;
   else if(sprite2.getBottom() <= sprite1.getTop())
     return false;
   else 
     return true;
 }
 
/* ALTERNATIVE SOLUTION: CHECK FOR COLLISION INSTEAD.
   public static boolean check_for_collision(Sprite sprite1, Sprite sprite2){
     boolean x_overlap = sprite2.getRight() > sprite1.getLeft() && sprite2.getLeft() < sprite1.getRight();
     boolean y_overlap = sprite2.getBottom() > sprite1.getTop() && sprite2.getTop() < sprite1.getBottom();
     return x_overlap && y_overlap;
    }
*/



}
