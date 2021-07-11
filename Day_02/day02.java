package Day_02;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class day02 {
    public static void main(String[] args) {
        firstPart();
        secondPart();
    }

    public static void firstPart() {
        var br = new BufferedReader(new InputStreamReader(day02.class.getResourceAsStream("input.txt")));
        String line;
        int valids = 0;
        try {

            while ((line = br.readLine()) != null) {
                var input = line.split(":");
                var rule = input[0];
                var password = input[1];
                var ruleParts = rule.split(" ");
                var min = Integer.parseInt(ruleParts[0].split("-")[0]);
                var max = Integer.parseInt(ruleParts[0].split("-")[1]);
                var ch = ruleParts[1].charAt(0);

                var times = password.codePoints().filter(i -> i == ch).count();

                if (min <= times && times <= max) {
                    valids++;
                }
            }

            System.out.println("A valid jelszavak száma: " + valids);
            br.close();

        } catch (Exception e) {
            // TODO: handle exception
        }

    }

    public static void secondPart() {
        var br = new BufferedReader(new InputStreamReader(day02.class.getResourceAsStream("input.txt")));
        String line;
        int valids = 0;
        try {
            while ((line = br.readLine()) != null) {
                var input = line.split(":");
                var rule = input[0];
                var password = input[1];
                var ruleParts = rule.split(" ");
                var min = Integer.parseInt(ruleParts[0].split("-")[0]);
                var max = Integer.parseInt(ruleParts[0].split("-")[1]);
                var ch = ruleParts[1].charAt(0);
                int found = 0;

                if (password.charAt(min) == ch) {
                    found++;
                }
                if(password.charAt(max) == ch) {
                    found++;
                }

                if(found == 1) {
                    valids++;
                }
            }

            System.out.println("2. A valid jelszavak száma: " + valids);
            br.close();
        } catch (Exception e) {
            // TODO: handle exception
        }
    }
}
