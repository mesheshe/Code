import java.io.*;
import java.util.*;

public class QuestionTree {
    private Scanner console;
    private QuestionNode mainRoot;

    public QuestionTree(){
        console = new Scanner(System.in);
        mainRoot = new QuestionNode("computer");
    }
    // Assuming data in file we are reading from is valid. 
    public void read(Scanner input){
        mainRoot = traversal(mainRoot, input);
    }

    private QuestionNode traversal(QuestionNode root, Scanner input){
        if (input.hasNextLine()){
            String query = input.nextLine();
            String queryData = input.nextLine();
            if (query.equals("Q:")){ // creates the question, and each time it is called 
                root = new QuestionNode(queryData, null, null); // a new QuestionNode
                root.left = traversal(root.left, input);        // is created
                root.right = traversal(root.right, input);
            }else{ // creates the answers
                return new QuestionNode(queryData);
            }
        }
        return root; // only for the case where input doesn't have a next line
    }

    public void write(PrintStream output){
        traversal(mainRoot, output);
    }

    private void traversal(QuestionNode root, PrintStream output){
        if (root != null){
            if (root.left != null){
                output.println("Q:");
            }else{
                output.println("A:");
            }
            output.println(root.data);
            traversal(root.left, output);
            traversal(root.right, output); 
        }
    }

    public void askQuestions(){
        mainRoot = ask(mainRoot);
    }

    private QuestionNode ask(QuestionNode root){
        if (root.left == null){
            // game is over if leaf is the object that user is thinking of
            if (yesTo("Would your object happen to be " + root.data +"?")){
                System.out.println("Great, I got it right!");
            }else{ // if no, get the object => get questions that correspond to it => and 
                System.out.print("What is the name of your object? "); // where to place it
                String ans = console.nextLine();                       
                System.out.println("Please give me a yes/no question that");
                System.out.println("distinguishes between your object");
                System.out.print("and mine--> ");
                String ques = console.nextLine();
                if (yesTo("And what is the answer for your object?")){
                    root = new QuestionNode(ques, new QuestionNode(ans), root);
                }else{ // line above and line below, change the current answer node to a question node
                    root = new QuestionNode(ques, root, new QuestionNode(ans)); // with one of the children
                }      // being the current answer node and the other child being the user's answer
            }
        }else{
            // ask the user the question if we are not at root node
            if (yesTo(root.data)){
                root.left = ask(root.left); 
            }else{
                root.right = ask(root.right);
            }
        }
        return root; // Only one of the cases is executed each time 
    }

    // post: asks the user a question, forcing an answer of "y " or "n";
    // returns true if the answer was yes, returns false otherwise
    public boolean yesTo(String prompt) {
        System.out.print(prompt + " (y/n)? ");
        String response = console.nextLine().trim().toLowerCase();
        while (!response.equals("y") && !response.equals("n")) {
            System.out.println("Please answer y or n.");
            System.out.print(prompt + " (y/n)? ");
            response = console.nextLine().trim().toLowerCase();
        }
        return response.equals("y");
    }
   
}
