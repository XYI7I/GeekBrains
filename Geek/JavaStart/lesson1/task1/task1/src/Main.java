import java.util.Scanner;
import java.io.FileWriter;
import java.io.IOException;

/**
 * Реализовать функцию возведения числа а в степень b. a, b ∈ Z.
 * Сводя количество выполняемых действий к минимуму.
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("Программа возводит число в любую целочисленную степень.");
        int numa = input_num();
        file_wr(String.valueOf(numa), "input.txt", "a");
        int numb = input_num();
        file_wr(String.valueOf(numb), "input.txt", "b");
        file_wr(String.valueOf(pow_num(numa, numb)), "output.txt", "a^b =");
        System.out.printf("%s^%s = %s", numa, numb, pow_num(numa, numb));
    }

    static int input_num(){
        Scanner iScaner = new Scanner(System.in);

//        boolean flag = iScaner.hasNextInt();
//        System.out.println(flag);
        do{
            System.out.print("Введите число: ");
            return iScaner.nextInt();
        }
        while (!iScaner.hasNextDouble());
    }

    static float pow_num(int num, int pow){
        float var = num;
        if (pow == 0){
            var = 1;
        }
        if (pow > 0){
            for (int i = 1; i < pow; i++){
                var *= num;
            }
        }
        if (pow < 0) {
            for (int i = -1; i > pow; i--) {
                var *= num;
            }
            var = 1 / var;
        }
        return var;
    }

    static void file_wr(String input, String filename, String var) {
        try (FileWriter fw = new FileWriter(filename, true)) {
            fw.write(var + " " + input);
            fw.append('\n');
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }

    }

}