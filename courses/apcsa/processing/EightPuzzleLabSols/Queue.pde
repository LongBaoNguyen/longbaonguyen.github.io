/*
  IMPLEMENT THIS CLASS BY FILLING IN CODE ACCORDING TO THE COMMENTS.

  A data structure that enforces the ordering principle known as 
  FIFO, first-in first-out. A new item is added(push) to the end of the line.
  An item is removed from the front of the line(pop). 
  It is also known as “first-come first-served.”
*/

public class Queue{
  ArrayList<Node> queue;
  public Queue(){
    // initialize queue to an empty arraylist of Nodes.
    // BEGIN CODE (about 1 line of code)
    queue = new ArrayList<Node>();
    // END CODE

  }
  
  // add a node to the end of the list.
  public void push(Node s){
    // BEGIN CODE (about 1 line of code)
    queue.add(s);
    // END CODE

  }
  
  // remove a node from the beginning of the list.
  public Node pop(){
    // BEGIN CODE (about 1 line of code)
    return queue.remove(0);
    // END CODE

  }
  
  // returns whether list is empty
  public boolean isEmpty(){
    // BEGIN CODE (about 1 line of code)
    return queue.size() == 0;
    // END CODE
  }
}
