public class HuffmanNode implements Comparable<HuffmanNode>{
    public Integer character;
    public Integer frequency;
    public HuffmanNode left;
    public HuffmanNode right;

    public HuffmanNode(Integer character, Integer frequency){
        this.character = character;
        this.frequency = frequency;
    }

    public HuffmanNode(Integer frequency, HuffmanNode left, HuffmanNode right){
        this(null, frequency);
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
