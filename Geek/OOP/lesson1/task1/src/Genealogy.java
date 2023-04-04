public class Genealogy {
    private Map<Person, List<Person>> relations;

    public Genealogy() {
        relations = new HashMap<>();
    }

    public void addRelation(Person parent, Person child) {
        List<Person> children = relations.get(parent);
        if (children == null) {
            children = new ArrayList<>();
        }
        children.add(child);
        relations.put(parent, children);
    }

    public List<Person> getChildren(Person parent) {
        return relations.get(parent);
    }
}

