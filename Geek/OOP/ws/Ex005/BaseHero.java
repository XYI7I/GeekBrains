package Ex005;

import java.util.Random;

public class BaseHero {
    protected static int number; //protected доступно в текущих классах и в наследуемых
    protected static Random r;

    protected String name;
    protected int hp;
    protected int maxHp;

    static {
        BaseHero.number = 0;
        BaseHero.r = new Random();
    }

    public BaseHero(String name, int hp) { //конструктор класса базовый
        this.name = name;
        this.hp = hp;
        this.maxHp = hp;
    }

    public BaseHero() { //перегрузка конструктора
        this(String.format("BaseHero #%d", ++BaseHero.number),
        BaseHero.r.nextInt(100, 200));
    }

    public String getInfo() {
        return String.format("Name: %s  Hp: %d Type: %s",
                this.name, this.hp, this.getClass().getSimpleName());
    }
    
    public void healed(int Hp) {
        this.hp = Hp + this.hp > this.maxHp ? this.maxHp : Hp + this.hp;
    }

    public void GetDamage(int damage) {
        if (this.hp - damage > 0) {
            this.hp -= damage;
        }
        // else { die(); }
    }

    public void Attack(BaseHero target) {
        int damage = BaseHero.r.nextInt(0, 20);
        target.GetDamage(damage);
    }
}
