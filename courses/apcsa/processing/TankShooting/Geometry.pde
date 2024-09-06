/* 
  YOU DO NOT NEED TO MODIFY THIS FILE FOR THIS LAB.
*/

static class Geometry{
/**
   This method accepts a Sprite sprite and an arraylist of Sprites and returns
   the collision list(arraylist) which consists of Sprite that collides with the given Sprite. 
*/ 
 public static ArrayList<Sprite> checkForCollisionWithList(Sprite sprite, ArrayList<Sprite> list){
  ArrayList<Sprite> collision_list = new ArrayList<Sprite>();
  for(Sprite s: list){
    if(s != sprite && checkForCollision(s, sprite))
      collision_list.add(s);
  }
  return collision_list;
}
/**
   Given two Sprite objects, return true if the objects collide. 
   This is a rectangle-rectangle collision. 
   Hint: Two ways to do this. It might be easier logically to think about
   when they are NOT colliding. Do this in each component(horizontal, vertical).
   The solutions to both methods are posted below.
*/ 
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
