public class ConsoleOutput {
    public void print(String message) {
        System.out.println(message);
    }
}

public class GenealogyStorage {
    private Genealogy genealogy;

    public GenealogyStorage() {
        genealogy = new Genealogy();
    }

    public void save(String fileName) throws IOException {
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(fileName));
        out.writeObject(genealogy);
        out.close();
    }

    public void load(String fileName) throws IOException, ClassNotFoundException {
        ObjectInputStream in = new ObjectInputStream(new FileInputStream(fileName));
        genealogy = (Genealogy) in.readObject();
        in.close();
    }
}

