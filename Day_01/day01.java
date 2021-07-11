package Day_01;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;


public class day01 {
    public static void main(String[] args) {
       firstPart();
       secondPart();
    }

    public static void firstPart() {
        BufferedReader br = new BufferedReader(new InputStreamReader(day01.class.getResourceAsStream("input.txt")));

        HashMap<Integer,Integer> pairs = new HashMap<>();
        String currentLine;

        try {
            while((currentLine = br.readLine()) != null) {
                var val = Integer.parseInt(currentLine);
                var key = pairs.get(val);
                if(key == null) {
                    pairs.put(2020-val, val);
                }
                else {
                    System.out.printf("A keresett szorzat: %d * %d = %d", val, key, val*key);
                    break;
                }
            
            }            
            br.close();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    public static void secondPart() {
        BufferedReader br = new BufferedReader(new InputStreamReader(day01.class.getResourceAsStream("input.txt")));

        HashMap<Integer,Integer> pairs = new HashMap<>();
        HashSet<Integer> dumpster = new HashSet<>();
        
        String currentLine;

        try {
            while((currentLine = br.readLine()) != null) {                                
                var num = Integer.parseInt(currentLine);
                var value = pairs.get(num);

                if(value != null) {
                    System.out.printf("\nA 2. keresett szorzat: %d", num*value);
                    return;
                }
                for(Integer i : dumpster) {
                    pairs.put(2020-(num+i), num*i);
                }
                dumpster.add(num);
            }

            br.close();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}