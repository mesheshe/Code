import java.util.*;
public class AnagramSolver {

    private Map<String, LetterInventory> master;
    private List<String> orderMaster;
    
    public AnagramSolver(List<String> list){
        // Assumes no repeating words 
        master = new HashMap<>(); //hashmap does not keep the order 
        orderMaster = new ArrayList<String>(list.size()); // purpose of keeping the order
        for (String s : list) {
            master.put(s, new LetterInventory(s));
            orderMaster.add(s);
        }
    }

    public void print(String s, int max){
        if (max < 0){throw new IllegalArgumentException();}
        LetterInventory branch = new LetterInventory(s);
        List<String> orderCopy = new ArrayList<>(); //dynamic array 
        Map<String, LetterInventory> copy = new HashMap<>();
        // following prunes the dictonary
        for (String z: orderMaster){
            // subtraction and addition does not modify LetterInventory
            // will return null if any subtraction results in negative indexes
            // or in other words, if subtraction is not possible
            if (branch.subtract(master.get(z)) != null){
                orderCopy.add(z);
                copy.put(z, master.get(z));
            }
        }
        Stack<String> answer = new Stack<>();
        for(String str: orderCopy){
            LetterInventory copyBranch = branch.subtract(copy.get(str));
            answer.push(str);
            recBack(orderCopy, copy, answer, copyBranch, max);
            answer.pop();
        }
        if (orderCopy.isEmpty() && max == 0){
            printOutput(new Stack<>());
        }         
    }
    
    private void recBack(List<String> orderCopy, Map<String, LetterInventory> copy,Stack<String> answer, LetterInventory branch, int max){
        if ((max == 0) || (max != 0  && answer.size() <= max)){
            if (branch.isEmpty()){
                printOutput(answer);
            }else{
                for (String s: orderCopy){
                    if (branch.subtract(copy.get(s)) != null){
                        answer.push(s);
                        branch = branch.subtract(copy.get(s));
                        recBack(orderCopy, copy, answer, branch, max);
                        branch = branch.add(copy.get(s));
                        answer.pop();
                    }
                }

            }
        }
    }
    
    private void printOutput(Stack<String> answer){
        int size = answer.size();
        List<String> q = new ArrayList<String>(size);

        while(!answer.isEmpty()){
            q.add(answer.pop());
        } 
        String str = "[";
        for (int i = q.size() - 1; i >= 0; i--){
            String value = q.get(i);
            if ( i == q.size() - 1){
                str += value;
            }else{
                str += ", " + value;
            }
        }
        System.out.println(str + "]");

        for (int i = q.size()  - 1; i >= 0; i--){
            answer.push(q.get(i));
        }
    }
}
