public class PersonBuilder {
    private String name;
    private int age;
    private Gender gender;

    public PersonBuilder setName(String name) {
        this.name = name;
        return this;
    }

    public PersonBuilder setAge(int age) {
        this.age = age;
        return this;
    }

    public PersonBuilder setGender(Gender gender) {
        this.gender = gender;
        return this;
    }

    public Person build() {
        return new Person(name, age, gender);
    }
}

