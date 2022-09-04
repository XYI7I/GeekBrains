/**
 * Написать программу вычисления n-ого треугольного числа.
 * http://ru.wikipedia.org/wiki/Треугольное_число
 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Программа вычисления n-ого треугольного числа");
        int var = triangular_num(input_num());
        System.out.println(var);

    }
    static int input_num(){
        Scanner iScaner = new Scanner(System.in);
        System.out.print("Введите целое положительное: ");
        boolean flag = iScaner.hasNextInt();
        System.out.println(flag);
        int var = iScaner.nextInt();
        System.out.printf("n = %s \n", var);

        iScaner.close();
        return var;
    }

    static int triangular_num(int num){
        return num * (num+1)/2;
    }

}