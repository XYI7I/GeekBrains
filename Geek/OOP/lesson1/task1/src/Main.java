public class Main {
  public static void main(String[] args) throws IOException, ClassNotFoundException {
    PersonBuilder builder = new PersonBuilder();
    Person john = builder.setName("John").setAge(30).setGender(Gender.MALE).build();
    Person alice = builder.setName("Alice").setAge(25).setGender(Gender.FEMALE).build();
    Person bob = builder.setName("Bob").setAge(5).setGender(Gender.MALE).build();
    Person eve = builder.setName("Eve").setAge(3).setGender(Gender.FEMALE).build();

    GenealogyStorage storage = new GenealogyStorage();
    Genealogy genealogy = storage.load("genealogy.txt");

    GenealogyResearch research = new GenealogyResearch(genealogy);
    List<Person> children = research.getChildren(john);

    ConsoleOutput consoleOutput = new ConsoleOutput();
    for (Person child : children) {
      consoleOutput.print(child.getName());
    }
  }
}