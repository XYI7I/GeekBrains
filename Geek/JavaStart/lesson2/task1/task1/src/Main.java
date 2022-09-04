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

//        boolean flag = iScaner.hasNextInt();
//        System.out.println(flag);
        do{
            System.out.print("Введите целое положительное: ");
            return iScaner.nextInt();
        }
        while (!iScaner.hasNextInt());
            }

    static int triangular_num(int num){
        return num * (num+1)/2;
    }

}