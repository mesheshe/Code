public class QuestionNode {
    public String data; 
    public QuestionNode left;
    public QuestionNode right;

    // Constructs an answer node. An answer node is defined by the fact that 
    // it is a leaf node, that means it has no children and so it only has the
    // answer
    public QuestionNode(String answer){
        data = answer;
        left = null;
        right = null;
    }
    // Constructs a question node. A question node is defined by the fact that it
    // has a data and two children with the left referring to the yes and the right
    // to no 
    public QuestionNode(String question, QuestionNode left, QuestionNode right){
        data = question;
        this.left = left;
        this.right = right;
    }
}


