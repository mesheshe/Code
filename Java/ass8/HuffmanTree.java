import java.io.*;
import java.util.*;

public class HuffmanTree {
    private Queue<HuffmanNode> q;

    public HuffmanTree(Scanner input){
        q = new PriorityQueue<>();
        HuffmanNode mainRoot = new HuffmanNode(-1, null, null);
        while (input.hasNextLine()){
            int n = Integer.parseInt(input.nextLine());  
            String code = input.nextLine();
            mainRoot = build(mainRoot, n, code, "");
        }
        q.add(mainRoot);
    }
    // Taking advantage of the fact we are only adding leaves. 
    public HuffmanNode build(HuffmanNode root, int n, String code, String build){
        if (build.length() <= code.length()){
            if (root == null){
                if (build.length() == code.length()){
                    return new HuffmanNode(n, -1);
                }else{ // build.length() is valid if we get to here
                    root = new HuffmanNode(-1, null, null);
                }
            }

            char val = code.charAt(build.length());

            if (val == '0'){
                root.left = build(root.left, n, code, build + val);
            }else{
                root.right = build(root.right,n, code, build + val);
            }
        }       
        return root;
    }

    public void decode(BitInputStream input, PrintStream output, int eof){
        HuffmanNode root = q.peek();
        boolean x = true;
        while (x){// Asumes a properly defined eof and valid tree
            root = traversal(q.peek(), input);
            if (root.character != eof){
                output.write(root.character);
            }else{
                x = false;
            }
        }
    }
    
    private HuffmanNode traversal(HuffmanNode root, BitInputStream in){
        if (root != null){
            if (root.character != -1){
                return root;
            }
            int readbit = in.readBit();
            if (readbit != -1){
                if (readbit == 0){
                    root = traversal(root.left, in);
                }else{
                    root = traversal(root.right, in);
                }
            }
        }
        return root;
    }
   
    public HuffmanTree(int[] count){
        q = new PriorityQueue<>();
        for(int i = 0; i < count.length; i++){
            if (count[i] != 0){
                q.add(new HuffmanNode(i, count[i]));
            }
        }
        q.add(new HuffmanNode(count.length, 1));
            
        compressQueue();
        
    }
    
    private void compressQueue(){
        while (q.size() != 1){
            HuffmanNode left = q.remove();
            HuffmanNode right = q.remove();
            q.add(new HuffmanNode(left.frequency + right.frequency, left, right));
        }
    }

    public void write(PrintStream output){
        traversal(q.peek(), output, "");
    }

    private void traversal(HuffmanNode root, PrintStream output, String str){
        if (root != null){
            if (root.character != -1){
                output.println(root.character);
                output.println(str);
            }
            traversal(root.left, output, str + "0");
            traversal(root.right, output, str + "1");
        }
    }

}
