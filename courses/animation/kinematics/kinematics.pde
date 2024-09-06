Trail a;


void setup(){
  size(500,500);
  a=new Trail(30,5);//number of Segments=30
                      //each segment=20 pixels
}


void draw()
{
  background(255);
  a.drag(mouseX,mouseY);
  a.display();
  
}
