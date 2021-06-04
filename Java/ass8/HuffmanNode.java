public class HuffmanNode implements Comparable<HuffmanNode>{
    public int character;
    public int frequency;
    public HuffmanNode left;
    public HuffmanNode right;

    public HuffmanNode(int character, int frequency){
        this.character = character;
        this.frequency = frequency;

    }

    public HuffmanNode(int frequency, HuffmanNode left, HuffmanNode right){
        this(-1, frequency);
        this.left = left;
        this.right = right;
    }
    
    public int compareTo(HuffmanNode other) {
        if (this.frequency < other.frequency){
            return -1;
        }else if (this.frequency == other.frequency){
            return 0;
        }else{
            return 1;
        }
    }
}
