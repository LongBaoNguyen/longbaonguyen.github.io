public class Trail{
  float x,y;
  int len;//number of Segments 
  Segment[] trail;
  public Trail(int numSeg, int segLength){
    len = numSeg;
    x = width/4;
    y = height/2;
    trail = new Segment[len];    
    trail[0] = new Segment(x,y,segLength);
    for(int i = 1;i <= len - 1;i++){
      Segment prev = trail[i-1];
      trail[i] = new Segment(prev.endX(),prev.endY(),segLength);
    }
  }
  
  public void drag(float x, float y){
    Segment last = trail[len-1];
    last.dragToXY(x,y);
    for(int i = len-2;i >= 0;i--){
      Segment current = trail[i];
      Segment parent = trail[i+1];
      current.dragToXY(parent.x,parent.y); 
    }
    
  }
  public void display(){
    for(int i=0;i<len;i++)
    {
      trail[i].display();
    }
  }

  
}
