public class Segment{
  float x,y;
  float len;
  float angle;
  public Segment(float x_, float y_, float len_){
    x = x_;
    y = y_;
    len = len_;
    angle = 0;
  }
  public float endX(){
    return x + cos(angle)*len;
  }
  public float endY(){
    return y + sin(angle)*len;
  }
  public void rotateToXY(float X, float Y){
    float dx = X-x;
    float dy = Y-y;
    angle=atan2(dy,dx);
  }
  public void dragToXY(float X, float Y){
    rotateToXY(X,Y);
    x = X-cos(angle)*len;
    y = Y-sin(angle)*len;
  }
  public void display(){
    strokeWeight(3);
    line(x,y,endX(),endY());
  }
  
  
}
