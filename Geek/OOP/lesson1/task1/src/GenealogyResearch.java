public class GenealogyResearch {
    private Genealogy genealogy;

    public GenealogyResearch(Genealogy genealogy) {
        this.genealogy = genealogy;
    }

    public List<Person> getChildren(Person parent) {
        return genealogy.getChildren(parent);
    }
}

