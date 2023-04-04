package ru.gb;

import java.util.ArrayList;

public class App {
  public static void main(String[] args) {
    Person irina = new Person("Ирина");
    Person vasya = new Person("Вася");
    Person masha = new Person("Маша");
    Person jane = new Person("Женя");
    Person ivan = new Person("Ваня");

    GeoTree gt = new GeoTree();
    gt.append(irina, vasya);
    gt.append(irina, masha);
    gt.append(vasya, jane);
    gt.append(vasya, ivan);

    System.out.println(new Research(gt).spend(irina, Relationship.parent));
  }
}

enum Relationship {
  parent,
  children
}

class Person {
  private String fullName;

  public String getFullName() {
    return fullName;
  }

  public Person(String fullName) {
    this.fullName = fullName;
  }

  @Override
  public String toString() {
    return String.format("(%s)", this.fullName);
  }
}

class Node {
  public Node(Person p1, Relationship re, Person p2) {
    this.p1 = p1;
    this.re = re;
    this.p2 = p2;
  }

  Person p1;
  Relationship re;
  Person p2;

  @Override
  public String toString() {
    return String.format("<%s %s %s>", p1, re, p2);
  }
}

class GeoTree {
  private ArrayList<Node> tree = new ArrayList<>();

  public ArrayList<Node> getTree() {
    return tree;
  }

  public void append(Person parent, Person children) {
    tree.add(new Node(parent, Relationship.parent, children));
    tree.add(new Node(children, Relationship.children, parent));
  }
}

class Research {
  ArrayList<Node> tree;

  public Research(GeoTree geoTree) {
    tree = geoTree.getTree();
  }

  public ArrayList<Person> spend(Person p, Relationship re) {
    ArrayList<Person> result = new ArrayList<>();
    for (Node t : tree) {
      if (t.p1.getFullName() == p.getFullName() && t.re == re) {
        result.add(t.p2);
      }
    }
    return result;
  }
}

class Reserch2 {
  // ...
}

class Reserch3 {
  // ...
}

class Printer {
  // ...
}
