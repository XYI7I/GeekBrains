/**
 * Написать программу, показывающую последовательность действий для игры “Ханойская башня”
 * Ханойская башня является одной из популярных головоломок XIX века.
 * Даны три стержня, на один из которых нанизаны восемь колец, причём кольца отличаются размером и лежат меньшее на большем.
 * Задача состоит в том, чтобы перенести пирамиду из восьми колец за наименьшее число ходов на другой стержень. За один раз разрешается переносить только одно кольцо, причём нельзя класть большее кольцо на меньшее.
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