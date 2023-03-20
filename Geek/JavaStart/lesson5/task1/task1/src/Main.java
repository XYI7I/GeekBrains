/**
 *  Полноценное оформление волнового алгоритмаw
 */

import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        System.out.println("Программа показывает последовательность действий для игры “Ханойская башня");
        Scanner ringhtw = new Scanner(System.in);
        System.out.println("Введите кол-во колец: ");
        int rings = ringhtw.nextInt();
        ringhtw.close();
        int fr = 1;
        int sec = 2;
        int thr = 3;
        htw(rings, fr, sec, thr);
    }
    static void htw(int ring, int fs, int sec, int thr){
        if (ring != 0){
            htw(ring - 1, fs, thr, sec);
            System.out.printf("Move from '%d' to '%d'\n", fs, thr);
            htw(ring - 1, sec, fs, thr);
        }

    }
}