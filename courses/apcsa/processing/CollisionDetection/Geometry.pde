/* Ignore the use static class here. This won't be on the AP exam.
   Because of the way Processing is set up, we avoid using static methods in objects classes
   in Processing. Making a class static is a way to use static method in the same
   way we talk about in class, e.g, Geometry.check_for_collision(sprite1, sprite2). */

static class Geometry{
 /**
   Given two Sprite objects, return true if the objects collide. 
   This is a rectangle-rectangle collision. 
   Hint: Two ways to do this. It might be easier logically to think about
   when they are NOT colliding. Do this in each component(horizontal, vertical).
 */ 
 public static boolean check_for_collision(Sprite sprite1, Sprite sprite2){
  return true;  // change this
 }
 
  
}
