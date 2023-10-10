import java.util.Scanner;
public class CommentIdentifier {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter a line of code (or type 'exit' to quit):");

        while (true) {
            String line = scanner.nextLine();

            if (line.equalsIgnoreCase("exit")) {
                break;
            }

            boolean isComment = isComment(line);
            if (isComment) {
                System.out.println("This line is a comment: " + line);
            } else {
                System.out.println("This line is not a comment: " + line);
            }
        }

        scanner.close();
    }

    public static boolean isComment(String line) {
        line = line.trim();

        // Empty line is not a comment.
        if (line.isEmpty()) {
            return false;
        }

        // Tokenize the line by whitespace
        String[] tokens = line.split("\\s+");

        // No tokens, not a comment.
        if (tokens.length == 0) {
            return false;
        }

        if (tokens[0].startsWith("//")) {
            return true; // Single-line comment.
        } else if (tokens[0].startsWith("/*") && tokens[tokens.length - 1].endsWith("*/")) {
            return true; // Multi-line comment.
        }

        return false;
    }
}