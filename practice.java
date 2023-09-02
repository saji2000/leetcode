import java.io.Console;
import java.util.Stack;

import javax.swing.tree.TreeNode;

public class practice {
    public static void main(String[] args) {
        Stack nodes = new Stack();
        nodes.Push(root);
        while (nodes.Count > 0) {
            TreeNode node = (TreeNode) nodes.Pop();
            Console.WriteLine(node.Text);
            for (int i = node.Nodes.Count - 1; i >= 0; i--)
                nodes.Push(node.Nodes[i]);
        }
    }
}
