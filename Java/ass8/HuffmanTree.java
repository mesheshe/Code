import java.io.*;
import java.util.*;

public class HuffmanTree {
    private PriorityQueue<HuffmanNode> q;

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
            HuffmanNode newHuff = new HuffmanNode(left.frequency + right.frequency, left, right);
            q.add(newHuff);
        }
    }

    public void write(PrintStream output){
        traversal(q.peek(), output, "");
    }

    private void traversal(HuffmanNode root, PrintStream output, String str){
        if (root != null){
            if (root.character != null){
                output.println(root.character);
                output.println(str);
            }
            traversal(root.left, output, str + "0");
            traversal(root.right, output, str + "1");
        }
    }

}
