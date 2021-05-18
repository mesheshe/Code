import java.util.*;
public class Test{
   public static void main(String[] args){
      int i = 5555;
      int j = 372;
      //System.out.println(maxDigits(i,j));
      Stack<Integer> s = new Stack<>();
      s.push(1);
      s.push(2);
      s.push(3);
      s.push(4);
      s.push(5);
      s.push(6);
      s.push(7);
      s.push(8);
      alternatingReverse(s);
      

    } 
   // 54321 = 1 + 10*2 + 100*3 + 1000*4 + 10000*5
   // So with each instance you are just picking 
   // which ever number to pair up with the 10 factor
   public static int maxDigits(int i, int j){
      if (i < 0 || j < 0){
         throw new IllegalArgumentException();
      }
      int iDigit = i % 10;
      int jDigit = j % 10;
      if (i != 0 || j != 0){
         if (iDigit >= jDigit){
            return iDigit + 10*maxDigits(i/10, j/10);
         }else{
            return jDigit + 10*maxDigits(i/10, j/10);
         }
      }else{
         return 0;
      }
   }
   
   public static void alternatingReverse(Stack<Integer> s){
      if (!(s.size() % 2 == 0)){
         throw new IllegalArgumentException();
      }
      if (s.isEmpty()){
         return;
      }
      int size = s.size(); 
      Queue<Integer> q = new LinkedList<>();
      for (int i = 0; i < size; i++){
         q.add(s.pop());
      }
      for (int i = 0; i < size; i++){
         int val =  q.remove();
         q.add(val);
         s.push(val);
      }
      for (int i = 0; i < size/2; i++){
         q.add(q.remove());
         q.add(s.pop());
         q.remove();
         s.pop();
      }
      q2s(q,s,size);
      s2q(s,q,size);
      q2s(q,s,size);      
      System.out.println("Queue =" + q);
      System.out.println("Stack = " + s);
   }
   public static void s2q(Stack<Integer> s, Queue<Integer> q, int size){
      for (int i = 0; i < size; i++){
         q.add(s.pop());
      } 
      
   }
   public static void q2s(Queue<Integer> q, Stack<Integer> s, int size){
      for (int i = 0; i < size; i++){
         s.push(q.remove());
      } 
      
   }
      
}

/*
   1) 
        p.next = q.next;
        q.next = null;
   2)   
        ListNode temp = p;
        p = p.next;
        temp.next = q;
        q = temp;
   3)
   
   
   4)

*/

/*

public ArrayIntList sublist(int start, int end){
      int newSize = end - start;
      ArrayIntList returnList = new ArrayIntList();
      for (int i = start; i != end; i++){
         returnList.elementData[i - start] = elementData[i];
      }
      returnList.size = newSize;
      return returnList; 
     }
*/
/*
      int size = s.size(); 
      Queue<Integer> q = new LinkedList<>();
      s2q(s,q,size);
      q.add(q.remove());
      q2s(q,s, size);
      s2q(s,q, size);
      s.push(q.remove());
      s.push(q.remove());
      //2
      q2s(q,s, q.size());
      s2q(s,q, s.size() - 2);
      q.add(q.remove());
      s.push(q.remove());
      //3
      q2s(q,s, q.size());
      s2q(s,q, size - 3);
      q.add(q.remove());
      q.add(q.remove());
      s.push(q.remove());
      //4
      q2s(q,s, q.size());
      s2q(s,q, size - 4);
      q.add(q.remove());
      q.add(q.remove());
      q.add(q.remove());
      s.push(q.remove());
      //5
      q2s(q,s, q.size());
      s2q(s,q, size - 5);
      q.add(q.remove());
      q.add(q.remove());
      q.add(q.remove());
      s.push(q.remove());
      //6
      q.add(q.remove());
      s.push(q.remove());
      s.push(q.remove());
      
      s2q(s,q,size);
      q2s(q,s, size);
*/