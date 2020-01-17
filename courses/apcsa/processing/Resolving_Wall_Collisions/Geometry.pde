/* Ignore the use static class here. This won't be on the AP exam.
   Because of the way Processing is set up, we avoid using static methods in objects classes
   in Processing. Making a class static is a way to use static method in the same
   way we talk about in class. */

static class Geometry{
  /**
   Given two Sprite objects, return true if the objects collide. 
   This is a rectangle-rectangle collision. 
   Hint: Two ways to do this. It might be easier logically to think about
   when they are NOT colliding. Do this in each component(horizontal, vertical).
   The solutions to both methods are posted below.
 */ 
 public static boolean check_for_collision(Sprite sprite1, Sprite sprite2){
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
